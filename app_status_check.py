#!/usr/bin/env python3
"""
Quick application status check after fixing the skills_new.py NameError
"""

import sys
import os
sys.path.append('.')

def check_application_status():
    """Check if application is ready to run"""
    print("🔍 APPLICATION STATUS CHECK")
    print("=" * 40)
    
    try:
        # Test critical imports
        print("1️⃣ Testing critical imports...")
        import views.dashboard
        import views.skills_new  
        import views.degen_test
        import views.degen_explorer
        import views.profile
        import utils.time_utils
        print("   ✅ All critical modules import successfully")
        
        # Test time utilities
        print("\n2️⃣ Testing timestamp functionality...")
        from utils.time_utils import calculate_relative_time, get_current_timestamp
        current_time = get_current_timestamp()
        relative_time = calculate_relative_time(current_time)
        print(f"   ✅ Time utilities working: {relative_time}")
        
        # Test user data loading
        print("\n3️⃣ Testing user data...")
        from data.users import load_user_data, get_current_user_data
        users_data = load_user_data()
        print(f"   ✅ User data loaded: {len(users_data)} users")
        
        # Test data integrity
        print("\n4️⃣ Checking timestamp implementation...")
        users_with_test = sum(1 for u in users_data.values() if u.get('test_taken'))
        users_with_timestamp = sum(1 for u in users_data.values() if 'test_completion_date' in u)
        print(f"   📊 Users with completed test: {users_with_test}")
        print(f"   📊 Users with timestamps: {users_with_timestamp}")
        print(f"   📊 Legacy users: {users_with_test - users_with_timestamp}")
        
        print("\n✅ APPLICATION STATUS: READY!")
        print("\n🚀 Ready to run:")
        print("   streamlit run main.py")
        print("\n🎯 Fixes applied:")
        print("   ✅ Timestamp fix: Dynamic timestamps in dashboard")
        print("   ✅ Skills fix: NameError resolved") 
        print("   ✅ All imports: Working correctly")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = check_application_status()
    if success:
        print("\n🎉 APPLICATION IS READY TO RUN!")
    else:
        print("\n💥 APPLICATION HAS ISSUES!")
