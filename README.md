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

### Quick Test (2 minutes)

1. **Click** "Connect to Fraud Department"
2. **Say:** "Raju"
3. **Say:** "Nellore"
4. **Say:** "No"
5. **Done!** Card blocked, case marked as fraud

### View Results

```bash
# Show updated database
cd Day6/backend
uv run python view_cases.py

# Show JSON file
cat resolved_cases/case_6_Raju_*.json
```

## 📊 Sample Fraud Cases

| Customer | Security Answer | Amount | Transaction | Location |
|----------|----------------|--------|-------------|----------|
| **Raju** | **Nellore** | **$25,000** | Wire Transfer | Dubai, UAE |
| Sarah Williams | Boston | $8,750 | Luxury Watch | Moscow, Russia |
| Michael Chen | Blue | $15,000 | Crypto Exchange | Lagos, Nigeria |
| John Smith | Johnson | $2,499 | E-commerce | Shanghai, China |
| Emily Rodriguez | Max | $3,299 | Electronics | Shenzhen, China |
| David Thompson | Pizza | $599 | Gaming | Unknown |

## 🎬 Conversation Flow

```
Agent: "Hello, this is the SecureBank Fraud Prevention Department. 
        May I please have your name?"

You:   "Raju"

Agent: "Thank you, Raju. I've pulled up your account. I can see we 
        have a fraud alert on your card ending in 5678. Before we 
        proceed, I need to verify your identity. What city are you from?"

You:   "Nellore"

Agent: "Perfect, thank you. Now, regarding the suspicious transaction: 
        We detected a charge of $25,000.00 to International Wire Transfer 
        from unknown-sender.com in Dubai, UAE on November 27th at 5:30 AM. 
        Did you authorize this transaction?"

You:   "No"

Agent: "I understand, Raju. I've immediately blocked your card ending 
        in 5678 to prevent any further unauthorized charges. You will 
        NOT be charged for this $25,000.00 transaction. We'll mail you 
        a replacement card within 3 to 5 business days..."
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
