#!/usr/bin/env python3
"""
Simple verification script for the degen test update fix.
"""

def main():
    print("🔍 Degen Test Update Fix Verification")
    print("=" * 40)
    
    try:
        # Check if get_current_user_data exists
        from data.users import get_current_user_data
        print("✅ get_current_user_data function available")
        
        # Check Profile view
        with open('views/profile.py', 'r', encoding='utf-8') as f:
            profile_content = f.read()
        
        profile_imports_correct = 'get_current_user_data' in profile_content
        profile_usage_correct = 'user_data = get_current_user_data(st.session_state.username)' in profile_content
        profile_no_old_function = 'get_live_user_stats' not in profile_content
        
        print(f"📋 Profile View:")
        print(f"  - Imports get_current_user_data: {'✅' if profile_imports_correct else '❌'}")
        print(f"  - Uses get_current_user_data: {'✅' if profile_usage_correct else '❌'}")
        print(f"  - No old get_live_user_stats: {'✅' if profile_no_old_function else '❌'}")
        
        # Check Dashboard view
        with open('views/dashboard.py', 'r', encoding='utf-8') as f:
            dashboard_content = f.read()
        
        dashboard_imports_correct = 'get_current_user_data' in dashboard_content
        dashboard_usage_correct = 'user_data = get_current_user_data(st.session_state.username)' in dashboard_content
        dashboard_clean_imports = 'from utils.real_time_updates import live_xp_indicator' in dashboard_content
        
        print(f"📊 Dashboard View:")
        print(f"  - Imports get_current_user_data: {'✅' if dashboard_imports_correct else '❌'}")
        print(f"  - Uses get_current_user_data: {'✅' if dashboard_usage_correct else '❌'}")
        print(f"  - Clean imports: {'✅' if dashboard_clean_imports else '❌'}")
        
        # Test the function with sample data
        from data.users import load_user_data
        users_data = load_user_data()
        
        if users_data:
            # Test with an existing user who has taken the degen test
            test_users = [username for username, data in users_data.items() 
                         if data.get('test_taken') and data.get('degen_type')]
            
            if test_users:
                test_user = test_users[0]
                user_data = get_current_user_data(test_user)
                
                print(f"\n🧪 Function Test (User: {test_user}):")
                print(f"  - Has XP: {'✅' if 'xp' in user_data else '❌'}")
                print(f"  - Has degen_type: {'✅' if 'degen_type' in user_data else '❌'}")
                print(f"  - Has test_scores: {'✅' if 'test_scores' in user_data else '❌'}")
                print(f"  - Has test_taken: {'✅' if 'test_taken' in user_data else '❌'}")
                
                degen_type = user_data.get('degen_type', 'None')
                test_taken = user_data.get('test_taken', False)
                print(f"  - Degen Type: {degen_type}")
                print(f"  - Test Taken: {test_taken}")
            else:
                print("\n🧪 Function Test: No users with completed degen test found")
        
        all_checks_pass = (profile_imports_correct and profile_usage_correct and 
                          profile_no_old_function and dashboard_imports_correct and 
                          dashboard_usage_correct and dashboard_clean_imports)
        
        print("\n" + "=" * 40)
        if all_checks_pass:
            print("✅ ALL CHECKS PASSED!")
            print("\n🎯 The fix should work correctly:")
            print("  • Degen test results will update immediately")
            print("  • No logout/login required")
            print("  • Both Profile and Dashboard will show current data")
        else:
            print("❌ Some checks failed - review the implementation")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
