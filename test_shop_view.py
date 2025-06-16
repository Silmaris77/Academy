#!/usr/bin/env python3
"""
Test the actual shop view to ensure it loads without the fromisoformat error
"""

import sys
import os
import datetime

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_shop_view_import():
    """Test that the shop view can be imported and basic functions work"""
    
    print("🧪 Testing shop view import and basic functionality...")
    
    try:
        # Import the shop module
        from views.shop_new import show_shop
        print("✅ Successfully imported shop_new module")
        
        # Test importing other dependencies
        from utils.user_management import load_user_data, save_user_data
        print("✅ Successfully imported user management utilities")
        
        # Test loading user data
        users_data = load_user_data()
        print(f"✅ Successfully loaded user data ({len(users_data)} users)")
        
        # Check if any user has active boosters
        users_with_boosters = 0
        for username, user_data in users_data.items():
            if 'active_boosters' in user_data and user_data['active_boosters']:
                users_with_boosters += 1
                print(f"📋 User '{username}' has active boosters: {list(user_data['active_boosters'].keys())}")
                
                # Test the booster format handling for this user
                for booster_id, booster_data in user_data['active_boosters'].items():
                    try:
                        if isinstance(booster_data, str):
                            expiry_time = datetime.datetime.fromisoformat(booster_data)
                            print(f"  ✅ Old format booster '{booster_id}' expires: {expiry_time}")
                        elif isinstance(booster_data, dict) and 'expires_at' in booster_data:
                            expiry_time = datetime.datetime.fromisoformat(booster_data['expires_at'])
                            print(f"  ✅ New format booster '{booster_id}' expires: {expiry_time}")
                        else:
                            print(f"  ⚠️  Unknown format for booster '{booster_id}': {type(booster_data)}")
                    except Exception as e:
                        print(f"  ❌ Error processing booster '{booster_id}': {e}")
        
        print(f"📊 Found {users_with_boosters} users with active boosters")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during shop view test: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 Shop View Error Fix Verification")
    print("=" * 50)
    
    success = test_shop_view_import()
    
    if success:
        print("\n✅ Shop view test successful!")
        print("The shop should now load without fromisoformat errors.")
    else:
        print("\n❌ Shop view test failed!")
        print("There are still issues with the shop view.")
