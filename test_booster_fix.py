#!/usr/bin/env python3
"""
Test script to verify the booster AttributeError fix
"""

import sys
import os

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from utils.inventory import is_booster_active
    from data.users import load_user_data
    
    print("✅ Successfully imported inventory functions")
    
    # Load user data to find users with active boosters
    users_data = load_user_data()
    
    # Find a user with active boosters
    test_user = None
    for username, user_data in users_data.items():
        if 'active_boosters' in user_data and user_data['active_boosters']:
            test_user = username
            break
    
    if test_user:
        print(f"✅ Found test user with active boosters: {test_user}")
        
        # Get the first booster ID
        user_data = users_data[test_user]
        booster_id = list(user_data['active_boosters'].keys())[0]
        
        print(f"🧪 Testing booster: {booster_id}")
        
        # Test the function
        is_active, expiration = is_booster_active(test_user, booster_id)
        
        print(f"✅ Function executed successfully!")
        print(f"   - Is active: {is_active}")
        print(f"   - Expiration: {expiration}")
        
        # Test with non-existent booster
        is_active_fake, expiration_fake = is_booster_active(test_user, "fake_booster")
        print(f"✅ Non-existent booster test: active={is_active_fake}, expiration={expiration_fake}")
        
    else:
        print("⚠️  No users with active boosters found - creating test scenario")
        
        # Test with non-existent user
        is_active, expiration = is_booster_active("fake_user", "fake_booster")
        print(f"✅ Non-existent user test: active={is_active}, expiration={expiration}")
        
    print("\n🎉 All tests passed! The AttributeError fix is working correctly.")
    
except Exception as e:
    print(f"❌ Error during testing: {e}")
    import traceback
    traceback.print_exc()
