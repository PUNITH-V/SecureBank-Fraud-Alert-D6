"""Simple script to view fraud cases in a formatted way."""
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent / "src"))

from fraud_database import get_all_fraud_cases


def format_status(status):
    """Add emoji to status."""
    status_map = {
        'pending_review': '⏳ Pending Review',
        'confirmed_safe': '✅ Confirmed Safe',
        'confirmed_fraud': '🚨 Confirmed Fraud',
        'verification_failed': '❌ Verification Failed'
    }
    return status_map.get(status, status)


def view_cases():
    """Display all fraud cases in a nice format."""
    cases = get_all_fraud_cases()
    
    print("\n" + "=" * 80)
    print("🏦 SECUREBANK FRAUD CASES DASHBOARD")
    print("=" * 80)
    print(f"\nTotal Cases: {len(cases)}")
    
    # Count by status
    pending = sum(1 for c in cases if c['status'] == 'pending_review')
    safe = sum(1 for c in cases if c['status'] == 'confirmed_safe')
    fraud = sum(1 for c in cases if c['status'] == 'confirmed_fraud')
    
    print(f"  ⏳ Pending: {pending}")
    print(f"  ✅ Safe: {safe}")
    print(f"  🚨 Fraud: {fraud}")
    print("\n" + "-" * 80)
    
    for i, case in enumerate(cases, 1):
        print(f"\n📋 Case #{case['id']} - {format_status(case['status'])}")
        print("-" * 80)
        print(f"👤 Customer:        {case['userName']}")
        print(f"💳 Card:            ****{case['cardEnding']}")
        print(f"💰 Amount:          ${case['transactionAmount']:,.2f}")
        print(f"🏪 Merchant:        {case['transactionName']}")
        print(f"🌐 Source:          {case['transactionSource']}")
        print(f"📍 Location:        {case['transactionLocation']}")
        print(f"🕐 Time:            {case['transactionTime']}")
        print(f"🏷️  Category:        {case['transactionCategory']}")
        print(f"🔐 Security Q:      {case['securityQuestion']}")
        print(f"🔑 Security A:      {case['securityAnswer']}")
        
        if case['outcomeNote']:
            print(f"📝 Outcome:         {case['outcomeNote']}")
        
        if case['updatedAt'] and case['updatedAt'] != case['createdAt']:
            print(f"🔄 Last Updated:    {case['updatedAt']}")
    
    print("\n" + "=" * 80)
    print("\n💡 To test a case:")
    print("   1. Start agent: uv run python src/agent.py dev")
    print("   2. Say customer name from above")
    print("   3. Answer security question")
    print("   4. Confirm or deny transaction")
    print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    view_cases()
