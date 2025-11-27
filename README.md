# Day 6 - Fraud Alert Voice Agent 🏦🔒

A professional fraud detection voice agent for SecureBank that verifies suspicious transactions through natural voice conversations.

## 🎯 Overview

This agent simulates a bank's fraud prevention department calling customers about suspicious transactions. It uses voice AI to:
- Load fraud cases from a database
- Verify customer identity with security questions
- Review suspicious transaction details
- Mark transactions as safe or fraudulent
- Save resolution details to JSON files

## ✨ Features

- ✅ **SQLite Database** - 6 pre-loaded fraud cases with diverse scenarios
- ✅ **Identity Verification** - Security questions from database
- ✅ **Transaction Review** - Clear reading of suspicious transaction details
- ✅ **Case Resolution** - Mark as safe or fraudulent with automatic card blocking
- ✅ **JSON Export** - Automatically saves resolved cases to JSON files
- ✅ **Professional UI** - Clean, minimal fraud alert interface
- ✅ **Voice Pipeline** - AssemblyAI (STT) + Google Gemini (LLM) + Murf AI (TTS)

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- LiveKit Server
- API Keys: Google Gemini, AssemblyAI, Murf AI

### 1. Start LiveKit Server

```bash
livekit-server --dev
```

### 2. Start Backend Agent

```bash
cd Day6/backend

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run agent
uv run python src/agent.py dev
```

### 3. Start Frontend

```bash
cd Day6/frontend

# Install dependencies (if needed)
pnpm install

# Run frontend
pnpm dev
```

### 4. Open Browser

Navigate to: http://localhost:3000

## 🎤 Demo Script

### Quick Test - Michael Chen (IRS Scam)

1. **Click** "Connect to Fraud Prevention"
2. **Say:** "Michael Chen"
3. **Say:** "54321"
4. **Say:** "1111"
5. **Say:** "Blue"
6. **Say:** "This is fraud" or "No"
7. **Done!** Case marked as fraud, saved to database

### Alternative Quick Test - John Smith (Wire Transfer)

1. **Click** "Connect to Fraud Prevention"
2. **Say:** "John Smith"
3. **Say:** "12345"
4. **Say:** "4242"
5. **Say:** "Johnson"
6. **Say:** "This is fraud"
7. **Done!** ✅

### View Results

```bash
# Show updated database
cd Day6/backend
uv run python view_cases.py

# Show JSON files
ls -la resolved_cases/
cat resolved_cases/case_3_michael_chen_*.json
```

## 📊 Sample Fraud Cases (All Suspicious)

| Customer | Account | SSN | Security Answer | Amount | Transaction Type |
|----------|---------|-----|-----------------|--------|------------------|
| **John Smith** | 12345 | 4242 | **Johnson** | **$9,999.99** | **Wire Transfer Scam** |
| Sarah Williams | 67890 | 8765 | Boston | $15,750.00 | Crypto Investment Scam |
| **Michael Chen** | 54321 | 1111 | **Blue** | **$8,500.00** | **IRS Impersonation** |
| Emily Rodriguez | 98765 | 3333 | Max | $12,499.99 | Luxury Goods Scam |
| David Thompson | 11111 | 7777 | Pizza | $4,999.00 | Tech Support Scam |
| Lisa Anderson | 22222 | 5555 | Honda | $7,800.00 | Romance Scam |
| Robert Martinez | 33333 | 9999 | Inception | $3,299.99 | Phishing Site |
| Jennifer Lee | 44444 | 2222 | Wilson | $2,500.00 | Lottery Scam |

## 🎬 Conversation Flow Example

### Michael Chen - IRS Impersonation Scam

```
Agent: "Welcome to SecureBank fraud prevention. We've detected suspicious 
        activity on your account. May I have your name please?"

You:   "Michael Chen"

Agent: "Thank you, Michael Chen. Can you please provide your account number?"

You:   "54321"

Agent: "Thank you. Please provide the last 4 digits of your social 
        security number."

You:   "1111"

Agent: "For security verification, what is your favorite color?"

You:   "Blue"

Agent: "Thank you for verifying your identity. I found a suspicious 
        transaction on your account. Let me read you the details.
        
        A charge of $8,500.00 was made to 'Fake IRS Tax Payment' from 
        irs-payment-urgent.cn in Beijing, China. The transaction occurred 
        on November 26th at 11:12 PM.
        
        Did you authorize this transaction?"

You:   "No, this is fraud"

Agent: "I understand. I've marked this transaction as fraudulent. We'll 
        block the charge immediately and issue you a new card within 3-5 
        business days. Your account is now secure. Is there anything else 
        I can help you with?"

You:   "No, thank you"

Agent: "Thank you for your time. Your account is now secure. Have a great day!"
```

## 🛠️ Tech Stack

### Backend
- **Python** - Core language
- **LiveKit Agents** - Voice AI framework
- **SQLite** - Fraud case database
- **Google Gemini 2.5 Flash** - LLM for conversation
- **AssemblyAI** - Speech-to-text
- **Murf AI** - Text-to-speech (en-US-natalie)

### Frontend
- **Next.js 15** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **LiveKit Components** - Voice interface
- **Framer Motion** - Animations

## 📁 Project Structure

```
Day6/
├── backend/
│   ├── src/
│   │   ├── agent.py              # Main fraud alert agent
│   │   └── fraud_database.py     # SQLite database management
│   ├── resolved_cases/           # JSON files of resolved cases
│   ├── fraud_cases.db            # SQLite database
│   ├── view_cases.py             # View dashboard
│   ├── test_database.py          # Test database
│   ├── reset_cases.py            # Reset all cases
│   ├── add_raju_case.py          # Add Raju's case
│   └── pyproject.toml            # Python dependencies
├── frontend/
│   ├── app/                      # Next.js app
│   ├── components/               # React components
│   └── package.json              # Node dependencies
├── DEMO_SCRIPT.md                # Full demo script
├── QUICK_DEMO.txt                # Quick reference
└── README.md                     # This file
```

## 🔧 Utilities

### View All Cases
```bash
uv run python view_cases.py
```

### Reset All Cases
```bash
python reset_cases.py
```

### Test Database
```bash
uv run python test_database.py
```

### Add Custom Case
Edit `add_raju_case.py` and run:
```bash
python add_raju_case.py
```

## 🎯 Agent Tools

The agent uses 4 function tools:

1. **load_fraud_case(name)** - Loads pending fraud case by customer name
2. **verify_customer(answer)** - Verifies identity with security answer
3. **mark_transaction_safe()** - Marks transaction as authorized
4. **mark_transaction_fraudulent()** - Marks as fraud and blocks card

## 📝 JSON Output

After each conversation, a JSON file is saved to `resolved_cases/`:

```json
{
  "case_id": 6,
  "resolution_timestamp": "2025-11-27T14:45:30.123456",
  "final_status": "confirmed_fraud",
  "customer": {
    "name": "Raju",
    "card_ending": "5678"
  },
  "transaction": {
    "amount": "$25,000.00",
    "merchant": "International Wire Transfer",
    "source": "unknown-sender.com",
    "location": "Dubai, UAE",
    "time": "2025-11-27 05:30:00",
    "category": "wire-transfer"
  },
  "verification": {
    "security_question": "What city are you from?",
    "verified": true
  },
  "outcome": "Customer Raju denied transaction. Card blocked..."
}
```

## 🔐 Security Notes

⚠️ **This is a demo application with fake data only!**

- No real card numbers, PINs, or passwords
- Security questions use non-sensitive fake answers
- All data is clearly demo/sandbox
- Never use this pattern with real customer data without proper security measures

## 🎥 Video Demo Tips

1. **Show Before State** - Run `view_cases.py` to show all pending
2. **Have Conversation** - Follow the demo script
3. **Show After State** - Run `view_cases.py` to show status changed
4. **Show JSON File** - Display the resolved case JSON
5. **Keep it Short** - 2-3 minutes is perfect

## 🐛 Troubleshooting

### Agent Not Responding
- Ensure LiveKit server is running: `livekit-server --dev`
- Check backend logs for errors
- Verify API keys in `.env`

### Wrong Security Question
- Agent now asks the exact question from database
- Restart agent if you made changes: Stop and start `agent.py`

### Database Issues
- Reset cases: `python reset_cases.py`
- Test database: `uv run python test_database.py`

## 📚 Resources

- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [Google Gemini API](https://ai.google.dev/)
- [AssemblyAI Docs](https://www.assemblyai.com/docs)
- [Murf AI Voices](https://docs.livekit.io/agents/models/tts/murf/)

## ✅ MVP Checklist

- [x] Sample fraud database with 6 cases
- [x] Professional bank fraud agent persona
- [x] Customer name lookup
- [x] Identity verification with database security questions
- [x] Transaction details reading
- [x] Safe/fraudulent marking
- [x] Database persistence
- [x] JSON export of resolved cases
- [x] Professional minimal UI
- [x] Complete documentation

## 🚀 Future Enhancements

- [ ] LiveKit Telephony for real phone calls
- [ ] DTMF input (press 1 for yes, 2 for no)
- [ ] Multiple fraud cases per customer
- [ ] Email/SMS notifications
- [ ] Admin dashboard
- [ ] Call recording and transcription

---

**Built with ❤️ for Day 6 of the LiveKit Agents Challenge**

© 2025 SecureBank • Demo Application
