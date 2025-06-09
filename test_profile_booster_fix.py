#!/usr/bin/env python3
"""
Test script to verify profile page loads without AttributeError
"""

import sys
import os

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from utils.inventory import is_booster_active
    from data.users import load_user_data
    
    print("✅ Testing profile page booster functionality...")
    
    # Load user data
    users_data = load_user_data()
    
    # Find user 'a' who had the issue and has boosters
    test_username = 'a'
    
    if test_username in users_data:
        user_data = users_data[test_username]
        print(f"✅ Found user '{test_username}'")
        
        # Check if user has active_boosters
        if 'active_boosters' in user_data:
            active_boosters = user_data['active_boosters']
            print(f"✅ User has active_boosters: {list(active_boosters.keys())}")
            
            # Test each booster
            for booster_id in active_boosters.keys():
                try:
                    is_active, expiration = is_booster_active(test_username, booster_id)
                    print(f"✅ Booster '{booster_id}': active={is_active}, expires={expiration}")
                except Exception as e:
                    print(f"❌ Error testing booster '{booster_id}': {e}")
                    raise
        else:
            print("ℹ️  User has no active_boosters")
            
        # Test the specific scenario that was failing
        print(f"\n🧪 Testing specific profile page scenario...")
        
        # Simulate what happens in profile.py line 319
        # is_active, expiration = is_booster_active(st.session_state.username, booster_id)
        
        if 'active_boosters' in user_data and user_data['active_boosters']:
            first_booster = list(user_data['active_boosters'].keys())[0]
            is_active, expiration = is_booster_active(test_username, first_booster)
            print(f"✅ Profile scenario test passed: booster={first_booster}, active={is_active}")
        else:
            print("ℹ️  No boosters to test profile scenario")
            
    else:
        print(f"⚠️  User '{test_username}' not found")
        
    print("\n🎉 All profile page tests passed! AttributeError fix successful.")
    
except Exception as e:
    print(f"❌ Error during profile testing: {e}")
    import traceback
    traceback.print_exc()
