#!/usr/bin/env python3
"""
Simple test to verify badge system functionality
"""
import sys
import os

print("🧪 TESTING BADGE SYSTEM")
print("=" * 40)

try:
    # Import modules
    from utils.achievements import check_achievements, check_badge_condition
    from data.users import load_user_data
    from config.settings import BADGES
    print("✅ All modules imported successfully")
    
    # Check badge configuration
    badge_id = "first_degen_test"
    badge_info = BADGES.get(badge_id)
    if badge_info:
        print(f"✅ Badge found: {badge_info['name']}")
    else:
        print(f"❌ Badge {badge_id} not found")
        sys.exit(1)
    
    # Load user data
    users_data = load_user_data()
    print(f"✅ Loaded {len(users_data)} users")
    
    # Check users who completed degen test
    users_with_test = 0
    users_with_badge = 0
    
    for username, user_data in users_data.items():
        test_taken = user_data.get('test_taken', False)
        degen_type = user_data.get('degen_type')
        has_badge = badge_id in user_data.get('badges', [])
        
        if test_taken and degen_type:
            users_with_test += 1
            print(f"🔍 User {username}: test completed, type: {degen_type}, has badge: {has_badge}")
            
            if has_badge:
                users_with_badge += 1
            else:
                # Test if they should get the badge
                should_have = check_badge_condition(badge_id, user_data)
                print(f"   Should have badge: {should_have}")
    
    print(f"\n📊 SUMMARY:")
    print(f"   Users with completed test: {users_with_test}")
    print(f"   Users with badge: {users_with_badge}")
    print(f"   Missing badges: {users_with_test - users_with_badge}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("TEST COMPLETED")
