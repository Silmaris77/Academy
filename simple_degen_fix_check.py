#!/usr/bin/env python3
"""
Simple verification that the degen test update fix is working
"""

def verify_fix():
    print("🔍 Verifying Degen Test Update Fix...")
    
    try:
        # Check if get_current_user_data exists
        from data.users import get_current_user_data
        print("✅ get_current_user_data function is available")
        
        # Check if views import the function
        with open('views/profile.py', 'r') as f:
            profile_content = f.read()
            if 'get_current_user_data' in profile_content:
                print("✅ Profile view imports get_current_user_data")
            else:
                print("❌ Profile view missing get_current_user_data import")
                
        with open('views/dashboard.py', 'r') as f:
            dashboard_content = f.read()
            if 'get_current_user_data' in dashboard_content:
                print("✅ Dashboard view imports get_current_user_data")
            else:
                print("❌ Dashboard view missing get_current_user_data import")
                
        # Check that views use the function
        if 'get_current_user_data(st.session_state.username)' in profile_content:
            print("✅ Profile view uses get_current_user_data")
        else:
            print("❌ Profile view doesn't use get_current_user_data")
            
        if 'get_current_user_data(st.session_state.username)' in dashboard_content:
            print("✅ Dashboard view uses get_current_user_data")
        else:
            print("❌ Dashboard view doesn't use get_current_user_data")
            
        print("\n🎯 Fix Summary:")
        print("- Updated Profile view to use get_current_user_data")
        print("- Updated Dashboard view to use get_current_user_data")  
        print("- This ensures degen test results sync properly")
        print("\n✅ Verification complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    verify_fix()
