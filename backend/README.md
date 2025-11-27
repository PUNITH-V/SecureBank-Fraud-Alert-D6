# Day 6 - Fraud Alert Voice Agent 🏦🔒

A professional fraud detection voice agent that helps bank customers verify suspicious transactions through natural voice conversations.

## 🎯 Features

- **SQLite Fraud Database** - Pre-populated with 5 sample fraud cases
- **Identity Verification** - Safe security questions (no sensitive data)
- **Transaction Review** - Clear reading of suspicious transaction details
- **Case Resolution** - Mark transactions as safe or fraudulent
- **Professional Persona** - Calm, reassuring bank fraud representative
- **Persistent Storage** - All case updates saved to database

## 🗄️ Sample Fraud Cases

The database includes 5 pre-loaded fraud cases:

1. **John Smith** - $2,499.99 from alibaba.com (China)
2. **Sarah Williams** - $8,750.00 from luxury watch site (Russia)
3. **Michael Chen** - $15,000.00 from crypto exchange (Nigeria)
4. **Emily Rodriguez** - $3,299.50 from electronics site (China)
5. **David Thompson** - $599.99 from gaming service

Each case includes:
- Customer name
- Security identifier
- Masked card number (last 4 digits)
- Transaction details (amount, merchant, location, time)
- Security question/answer for verification
- Status tracking

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd Day6/backend
uv sync
```

### 2. Configure Environment

Copy `.env.example` to `.env` and add your API keys:

```bash
cp .env.example .env
```

Required API keys:
- **LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET** - From LiveKit Cloud
- **GOOGLE_API_KEY** - For Gemini LLM
- **ASSEMBLYAI_API_KEY** - For speech-to-text
- **MURF_API_KEY** - For text-to-speech

### 3. Run the Agent

```bash
uv run python src/agent.py dev
```

The database will automatically initialize with sample fraud cases on first run.

## 💬 Conversation Flow

### Example Interaction:

**Agent:** "Hello, this is the SecureBank Fraud Prevention Department. May I please have your name to pull up your account?"

**Customer:** "John Smith"

**Agent:** "Thank you, John Smith. I've pulled up your account. I can see we have a fraud alert on your card ending in 4242. Before we proceed, I need to verify your identity. What is your mother's maiden name?"

**Customer:** "Johnson"

**Agent:** "Perfect, thank you. Now, regarding the suspicious transaction: We detected a charge of $2,499.99 to ABC Industry Ltd from alibaba.com in Shanghai, China on November 27th at 2:34 AM. Did you authorize this transaction?"

**Customer:** "No, I didn't make that purchase."

**Agent:** "I understand, John Smith. I've immediately blocked your card ending in 4242 to prevent any further unauthorized charges. You will NOT be charged for this $2,499.99 transaction. We'll mail you a replacement card within 3 to 5 business days..."

## 🛠️ Agent Tools

The agent uses 4 function tools:

1. **load_fraud_case(name)** - Loads pending fraud case by customer name
2. **verify_customer(answer)** - Verifies identity with security answer
3. **mark_transaction_safe()** - Marks transaction as authorized
4. **mark_transaction_fraudulent()** - Marks transaction as fraud and blocks card

## 📊 Database Schema

```sql
CREATE TABLE fraud_cases (
    id INTEGER PRIMARY KEY,
    userName TEXT NOT NULL,
    securityIdentifier TEXT NOT NULL,
    cardEnding TEXT NOT NULL,
    status TEXT DEFAULT 'pending_review',
    transactionName TEXT NOT NULL,
    transactionAmount REAL NOT NULL,
    transactionTime TEXT NOT NULL,
    transactionCategory TEXT NOT NULL,
    transactionSource TEXT NOT NULL,
    transactionLocation TEXT NOT NULL,
    securityQuestion TEXT NOT NULL,
    securityAnswer TEXT NOT NULL,
    outcomeNote TEXT,
    createdAt TEXT,
    updatedAt TEXT
);
```

## 🔍 Testing Different Cases

To test different fraud cases, use these customer names:
- "John Smith"
- "Sarah Williams"
- "Michael Chen"
- "Emily Rodriguez"
- "David Thompson"

Each has a unique security question and transaction scenario.

## 🔐 Security Notes

⚠️ **This is a demo application with fake data only!**

- No real card numbers, PINs, or passwords are used
- Security questions use non-sensitive fake answers
- All data is clearly marked as demo/sandbox
- Never use this pattern with real customer data without proper security measures

## 📁 Project Structure

```
Day6/backend/
├── src/
│   ├── agent.py              # Main fraud alert agent
│   └── fraud_database.py     # SQLite database management
├── fraud_cases.db            # SQLite database (auto-created)
├── pyproject.toml            # Python dependencies
├── .env                      # API keys (not in git)
└── README.md                 # This file
```

## 🎨 Voice Configuration

- **Voice**: Murf AI "en-US-natalie" (professional, trustworthy)
- **Style**: Conversation (calm and professional)
- **LLM**: Google Gemini 2.5 Flash
- **STT**: AssemblyAI

## 📝 Viewing Database

To inspect the fraud cases database:

```bash
sqlite3 fraud_cases.db "SELECT * FROM fraud_cases;"
```

Or use a SQLite browser tool to view the database visually.

## 🎯 MVP Checklist

✅ Sample fraud database with multiple cases  
✅ Professional bank fraud agent persona  
✅ Customer name lookup  
✅ Identity verification with security questions  
✅ Transaction details reading  
✅ Safe/fraudulent marking  
✅ Database persistence  
✅ Professional conversation flow  

## 🚀 Advanced Goals (Optional)

- [ ] LiveKit Telephony integration for real phone calls
- [ ] DTMF input support (press 1 for yes, 2 for no)
- [ ] Multiple fraud cases per customer
- [ ] Email notifications
- [ ] SMS verification codes
- [ ] Call recording and transcription
- [ ] Admin dashboard for fraud ops team

## 📚 Resources

- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [LiveKit Telephony](https://docs.livekit.io/agents/telephony/)
- [Python SQLite Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [Murf AI Voices](https://docs.livekit.io/agents/models/tts/murf/)

---

Built with ❤️ using LiveKit Agents, Google Gemini, AssemblyAI, and Murf AI
