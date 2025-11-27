#!/bin/bash

# Day 6 - Fraud Alert Voice Agent Backend Starter Script

echo "🏦 Starting Day 6 - Fraud Alert Voice Agent Backend"
echo "=================================================="
echo ""

# Check if we're in the right directory
if [ ! -f "backend/src/agent.py" ]; then
    echo "❌ Error: Please run this script from the Day6 directory"
    exit 1
fi

cd backend

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found"
    echo "📝 Creating .env from .env.example..."
    cp .env.example .env
    echo ""
    echo "⚠️  Please edit backend/.env with your API keys before continuing!"
    echo ""
    echo "Required keys:"
    echo "  - LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET"
    echo "  - GOOGLE_API_KEY (Gemini)"
    echo "  - ASSEMBLYAI_API_KEY"
    echo "  - MURF_API_KEY"
    echo ""
    read -p "Press Enter after you've configured .env, or Ctrl+C to exit..."
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Installing dependencies..."
    uv sync
    echo ""
fi

# Test database
echo "🧪 Testing fraud database..."
uv run python test_database.py
echo ""

# Start the agent
echo "🚀 Starting fraud alert agent..."
echo "=================================================="
echo ""
echo "💡 Tips:"
echo "  - Connect via frontend voice interface"
echo "  - Say a customer name: John Smith, Sarah Williams, etc."
echo "  - Answer the security question"
echo "  - Confirm or deny the transaction"
echo ""
echo "Press Ctrl+C to stop the agent"
echo ""

uv run python src/agent.py dev
