"""Test script to verify fraud database setup and operations."""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from fraud_database import (
    get_fraud_case_by_username,
    update_fraud_case_status,
    get_all_fraud_cases
)


def test_database():
    """Test database operations."""
    print("🧪 Testing Fraud Database\n")
    print("=" * 60)
    
    # Test 1: Get all cases
    print("\n📊 All Fraud Cases:")
    print("-" * 60)
    all_cases = get_all_fraud_cases()
    print(f"Total cases in database: {len(all_cases)}\n")
    
    for case in all_cases:
        print(f"ID: {case['id']}")
        print(f"Customer: {case['userName']}")
        print(f"Card: ****{case['cardEnding']}")
        print(f"Transaction: ${case['transactionAmount']:.2f} to {case['transactionName']}")
        print(f"Location: {case['transactionLocation']}")
        print(f"Status: {case['status']}")
        print(f"Security Q: {case['securityQuestion']}")
        print(f"Security A: {case['securityAnswer']}")
        print("-" * 60)
    
    # Test 2: Load specific case
    print("\n🔍 Testing Case Lookup:")
    print("-" * 60)
    test_name = "John Smith"
    case = get_fraud_case_by_username(test_name)
    
    if case:
        print(f"✅ Found case for {test_name}")
        print(f"   Transaction: ${case['transactionAmount']:.2f}")
        print(f"   Merchant: {case['transactionName']}")
        print(f"   Source: {case['transactionSource']}")
        print(f"   Location: {case['transactionLocation']}")
        print(f"   Time: {case['transactionTime']}")
    else:
        print(f"❌ No case found for {test_name}")
    
    # Test 3: Test case-insensitive lookup
    print("\n🔍 Testing Case-Insensitive Lookup:")
    print("-" * 60)
    test_name_lower = "john smith"
    case_lower = get_fraud_case_by_username(test_name_lower)
    
    if case_lower:
        print(f"✅ Found case for '{test_name_lower}' (lowercase)")
    else:
        print(f"❌ Case-insensitive lookup failed")
    
    # Test 4: Update case status (optional - commented out to preserve data)
    print("\n⚠️  Status Update Test (Skipped)")
    print("-" * 60)
    print("To test status updates, uncomment the code in test_database.py")
    print("This will mark a case as 'confirmed_safe' for testing.")
    
    # Uncomment to test status updates:
    # if case:
    #     print(f"Updating case {case['id']} to 'confirmed_safe'...")
    #     success = update_fraud_case_status(
    #         case['id'],
    #         'confirmed_safe',
    #         'Test update - customer confirmed transaction'
    #     )
    #     if success:
    #         print("✅ Status update successful")
    #         updated_case = get_fraud_case_by_username(test_name)
    #         print(f"   New status: {updated_case['status']}")
    #     else:
    #         print("❌ Status update failed")
    
    print("\n" + "=" * 60)
    print("✅ Database tests complete!")
    print("\nTo use in agent:")
    print("1. Start the agent: uv run python src/agent.py dev")
    print("2. Connect via frontend")
    print("3. Say a customer name like 'John Smith'")
    print("4. Answer the security question")
    print("5. Confirm or deny the transaction")


if __name__ == "__main__":
    test_database()
