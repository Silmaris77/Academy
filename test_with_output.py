#!/usr/bin/env python3
"""
Badge system test with file output
"""
import sys
import os

def run_test():
    try:
        # Import modules
        from utils.achievements import check_achievements, check_badge_condition
        from data.users import load_user_data
        from config.settings import BADGES
        
        results = []
        results.append("🧪 BADGE SYSTEM TEST RESULTS")
        results.append("=" * 50)
        
        # Check badge configuration
        badge_id = "first_degen_test"
        badge_info = BADGES.get(badge_id)
        if badge_info:
            results.append(f"✅ Badge found: {badge_info['name']}")
            results.append(f"📝 Description: {badge_info['description']}")
            results.append(f"💎 XP reward: {badge_info['xp_reward']}")
        else:
            results.append(f"❌ Badge {badge_id} not found")
            return results
        
        # Load user data
        users_data = load_user_data()
        results.append(f"✅ Loaded {len(users_data)} users")
        results.append("")
        
        # Check users who completed degen test
        users_with_test = 0
        users_with_badge = 0
        missing_badge_users = []
        
        for username, user_data in users_data.items():
            test_taken = user_data.get('test_taken', False)
            degen_type = user_data.get('degen_type')
            has_badge = badge_id in user_data.get('badges', [])
            
            if test_taken and degen_type:
                users_with_test += 1
                results.append(f"🔍 User: {username}")
                results.append(f"   Test completed: ✅")
                results.append(f"   Degen type: {degen_type}")
                results.append(f"   Has badge: {'✅' if has_badge else '❌'}")
                
                if has_badge:
                    users_with_badge += 1
                else:
                    # Test if they should get the badge
                    should_have = check_badge_condition(badge_id, user_data)
                    results.append(f"   Should have badge: {'✅' if should_have else '❌'}")
                    if should_have:
                        missing_badge_users.append(username)
                results.append("")
        
        results.append("📊 SUMMARY:")
        results.append(f"   Users with completed test: {users_with_test}")
        results.append(f"   Users with badge: {users_with_badge}")
        results.append(f"   Missing badges: {users_with_test - users_with_badge}")
        
        if missing_badge_users:
            results.append("")
            results.append("🚨 USERS MISSING BADGES:")
            for user in missing_badge_users:
                results.append(f"   - {user}")
        
        results.append("")
        results.append("✅ TEST COMPLETED SUCCESSFULLY")
        
    except Exception as e:
        results.append(f"❌ Error: {e}")
        import traceback
        results.append(traceback.format_exc())
    
    return results

if __name__ == "__main__":
    results = run_test()
    
    # Write to file
    with open("test_results.txt", "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")
    
    # Also try to print
    for line in results:
        print(line)
