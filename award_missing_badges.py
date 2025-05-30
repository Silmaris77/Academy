#!/usr/bin/env python3
"""
Script to award missing badges to all users who completed the degen test
"""
import sys
import os

def award_missing_badges():
    """Award missing badges to all eligible users"""
    try:
        from utils.achievements import check_achievements
        from data.users import load_user_data
        
        print("🏆 AWARDING MISSING BADGES")
        print("=" * 40)
        
        users_data = load_user_data()
        total_users = len(users_data)
        users_with_completed_test = 0
        users_awarded_badges = 0
        
        for username, user_data in users_data.items():
            test_taken = user_data.get('test_taken', False)
            degen_type = user_data.get('degen_type')
            current_badges = user_data.get('badges', [])
            
            if test_taken and degen_type:
                users_with_completed_test += 1
                print(f"\n🔍 Processing user: {username}")
                print(f"   Degen type: {degen_type}")
                print(f"   Current badges: {len(current_badges)}")
                
                # Check and award achievements
                new_badges = check_achievements(username)
                
                if new_badges:
                    users_awarded_badges += 1
                    print(f"   ✅ Awarded {len(new_badges)} badges:")
                    for badge in new_badges:
                        print(f"      - {badge}")
                else:
                    print(f"   ℹ️  No new badges to award")
        
        print(f"\n📊 SUMMARY:")
        print(f"   Total users: {total_users}")
        print(f"   Users with completed test: {users_with_completed_test}")
        print(f"   Users awarded new badges: {users_awarded_badges}")
        print(f"\n✅ BADGE AWARDING COMPLETED!")
        
        # Verify the fix worked
        print(f"\n🔍 VERIFICATION:")
        users_data_updated = load_user_data()
        for username, user_data in users_data_updated.items():
            test_taken = user_data.get('test_taken', False)
            degen_type = user_data.get('degen_type')
            badges = user_data.get('badges', [])
            
            if test_taken and degen_type:
                has_degen_badge = 'first_degen_test' in badges
                print(f"   {username}: {'✅' if has_degen_badge else '❌'} has degen badge")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    award_missing_badges()
