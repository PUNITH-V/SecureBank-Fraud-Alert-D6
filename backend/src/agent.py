import logging
import json
from datetime import datetime
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    WorkerOptions,
    cli,
    metrics,
    tokenize,
    function_tool,
    RunContext
)
from livekit.plugins import murf, silero, google, assemblyai, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from fraud_database import (
    get_fraud_case_by_username,
    update_fraud_case_status
)

logger = logging.getLogger("fraud_agent")
load_dotenv(".env")

# JSON output directory
RESOLVED_CASES_DIR = Path(__file__).parent.parent / "resolved_cases"
RESOLVED_CASES_DIR.mkdir(exist_ok=True)


class FraudAlertAgent(Agent):
    def __init__(self) -> None:
        self.current_case = None
        self.verification_passed = False
        self.customer_name = None
        
        instructions = """You are a professional fraud detection representative for SecureBank. Your role is to help customers verify suspicious transactions on their accounts.

🏦 YOUR IDENTITY:
- You work for SecureBank's Fraud Prevention Department
- You are calling about a suspicious transaction alert
- You are calm, professional, and reassuring
- You NEVER ask for full card numbers, PINs, passwords, or sensitive credentials

📋 CONVERSATION FLOW:

1. GREETING & INTRODUCTION:
   - Greet warmly: "Hello, this is the SecureBank Fraud Prevention Department."
   - Ask: "May I please have your name to pull up your account?"
   - Wait for their name

2. LOAD FRAUD CASE:
   - Once you have their name, IMMEDIATELY call load_fraud_case(name)
   - This will load their pending fraud case
   - If no case found, politely explain and end the call

3. VERIFICATION:
   - Explain: "For security purposes, I need to verify your identity with a quick security question."
   - Ask the security question from the loaded case
   - Wait for their answer
   - Call verify_customer(answer) with their response
   - If verification fails: Politely end the call and explain you cannot proceed

4. TRANSACTION REVIEW:
   - Once verified, explain: "Thank you. I'm calling about a suspicious transaction on your card ending in [card_ending]."
   - Read the transaction details clearly:
     * Merchant name
     * Amount
     * Date and time
     * Location
     * Transaction source/website
   - Example: "We detected a charge of $2,499.99 to ABC Industry Ltd from alibaba.com in Shanghai, China on November 27th at 2:34 AM."

5. CUSTOMER CONFIRMATION:
   - Ask directly: "Did you authorize this transaction?"
   - Listen carefully for YES or NO
   - If they say YES: Call mark_transaction_safe()
   - If they say NO: Call mark_transaction_fraudulent()

6. RESOLUTION & CLOSING:
   - Explain what action was taken
   - If fraudulent: "I've marked this as fraudulent. Your card has been blocked and we'll issue a replacement within 3-5 business days. You won't be charged for this transaction."
   - If safe: "Perfect! I've marked this transaction as authorized. No further action is needed. Thank you for confirming."
   - Close professionally: "Is there anything else I can help you with today? Thank you for banking with SecureBank. Have a great day!"

⚠️ CRITICAL RULES:
- NEVER ask for full card numbers, PINs, or passwords
- ALWAYS call load_fraud_case() after getting the customer's name
- ALWAYS call verify_customer() with their security answer
- ALWAYS call mark_transaction_safe() or mark_transaction_fraudulent() based on their response
- Keep responses conversational and concise for voice
- Be empathetic - fraud is stressful for customers
- Stay professional and reassuring throughout

🎯 YOUR TOOLS:
You have 3 function tools that you MUST use at the right time:
1. load_fraud_case(name) - Call this immediately after getting customer name
2. verify_customer(answer) - Call this with their security answer
3. mark_transaction_safe() - Call if customer confirms transaction
4. mark_transaction_fraudulent() - Call if customer denies transaction

Remember: You're here to protect the customer and resolve the fraud alert efficiently!"""

        super().__init__(instructions=instructions)

    @function_tool
    async def load_fraud_case(self, context: RunContext, name: str):
        """Load a pending fraud case for the customer by their name.
        
        Args:
            name: Customer's name to look up their fraud case
        """
        logger.info(f"🔍 Loading fraud case for: {name}")
        
        fraud_case = get_fraud_case_by_username(name)
        
        if not fraud_case:
            logger.warning(f"❌ No pending fraud case found for: {name}")
            return f"I apologize, but I don't see any pending fraud alerts for {name} in our system. This might have been resolved already, or there may be a name mismatch. Could you verify the spelling of your name?"
        
        self.current_case = fraud_case
        self.customer_name = name
        logger.info(f"✅ Loaded fraud case ID {fraud_case['id']} for {name}")
        logger.info(f"📊 Transaction: ${fraud_case['transactionAmount']} to {fraud_case['transactionName']}")
        
        return f"Thank you, {name}. I've pulled up your account. I can see we have a fraud alert on your card ending in {fraud_case['cardEnding']}. Before we proceed, I need to verify your identity. {fraud_case['securityQuestion']}"

    @function_tool
    async def verify_customer(self, context: RunContext, answer: str):
        """Verify the customer's identity using their security answer.
        
        Args:
            answer: Customer's answer to the security question
        """
        if not self.current_case:
            return "I need to load your fraud case first. Could you please provide your name?"
        
        correct_answer = self.current_case['securityAnswer']
        customer_answer = answer.strip()
        
        logger.info(f"🔐 Verifying customer answer: '{customer_answer}' vs correct: '{correct_answer}'")
        
        # Case-insensitive comparison
        if customer_answer.lower() == correct_answer.lower():
            self.verification_passed = True
            logger.info("✅ Verification PASSED")
            
            case = self.current_case
            return f"Perfect, thank you. Now, regarding the suspicious transaction: We detected a charge of ${case['transactionAmount']:.2f} to {case['transactionName']} from {case['transactionSource']} in {case['transactionLocation']} on {case['transactionTime']}. Did you authorize this transaction?"
        else:
            logger.warning("❌ Verification FAILED")
            return "I'm sorry, but that answer doesn't match our records. For your security, I cannot proceed with this call. Please visit your nearest branch with a valid ID, or call our main customer service line. Thank you."

    @function_tool
    async def mark_transaction_safe(self, context: RunContext):
        """Mark the transaction as safe/authorized by the customer."""
        if not self.current_case:
            return "I need to load your fraud case first."
        
        if not self.verification_passed:
            return "I need to verify your identity first before I can update the case."
        
        case_id = self.current_case['id']
        outcome_note = f"Customer {self.customer_name} confirmed transaction as legitimate on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        update_fraud_case_status(case_id, "confirmed_safe", outcome_note)
        
        logger.info(f"✅ Case {case_id} marked as SAFE")
        
        # Save to JSON file
        self._save_case_to_json("confirmed_safe", outcome_note)
        
        return f"Excellent! I've marked this transaction as authorized. No further action is needed on your part. Your card remains active and you can continue using it normally. Thank you for confirming, {self.customer_name}."

    @function_tool
    async def mark_transaction_fraudulent(self, context: RunContext):
        """Mark the transaction as fraudulent/unauthorized."""
        if not self.current_case:
            return "I need to load your fraud case first."
        
        if not self.verification_passed:
            return "I need to verify your identity first before I can update the case."
        
        case_id = self.current_case['id']
        case = self.current_case
        outcome_note = f"Customer {self.customer_name} denied transaction. Card blocked. Dispute initiated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        update_fraud_case_status(case_id, "confirmed_fraud", outcome_note)
        
        logger.info(f"🚨 Case {case_id} marked as FRAUDULENT")
        
        # Save to JSON file
        self._save_case_to_json("confirmed_fraud", outcome_note)
        
        return f"I understand, {self.customer_name}. I've immediately blocked your card ending in {case['cardEnding']} to prevent any further unauthorized charges. You will NOT be charged for this ${case['transactionAmount']:.2f} transaction. We'll mail you a replacement card within 3 to 5 business days to your address on file. You'll also receive an email with dispute details and next steps."

    def _save_case_to_json(self, final_status: str, outcome_note: str):
        """Save the resolved fraud case to a JSON file."""
        if not self.current_case:
            return
        
        case = self.current_case
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        case_data = {
            "case_id": case['id'],
            "resolution_timestamp": datetime.now().isoformat(),
            "final_status": final_status,
            "customer": {
                "name": self.customer_name,
                "card_ending": case['cardEnding']
            },
            "transaction": {
                "amount": f"${case['transactionAmount']:.2f}",
                "merchant": case['transactionName'],
                "source": case['transactionSource'],
                "location": case['transactionLocation'],
                "time": case['transactionTime'],
                "category": case['transactionCategory']
            },
            "verification": {
                "security_question": case['securityQuestion'],
                "verified": self.verification_passed
            },
            "outcome": outcome_note
        }
        
        # Save to JSON file
        filename = f"case_{case['id']}_{self.customer_name.replace(' ', '_')}_{timestamp}.json"
        filepath = RESOLVED_CASES_DIR / filename
        
        with open(filepath, 'w') as f:
            json.dump(case_data, f, indent=2)
        
        logger.info(f"💾 Saved case to: {filepath}")


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    session = AgentSession(
        stt=assemblyai.STT(),
        llm=google.LLM(model="gemini-2.5-flash"),
        tts=murf.TTS(
            voice="en-US-natalie",  # Professional, trustworthy female voice
            style="Conversation",  # Calm and professional
            tokenizer=tokenize.basic.SentenceTokenizer(min_sentence_len=2),
            text_pacing=True
        ),
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        preemptive_generation=True,
    )

    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    await session.start(
        agent=FraudAlertAgent(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
