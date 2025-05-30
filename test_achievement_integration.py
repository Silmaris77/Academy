#!/usr/bin/env python3
"""
Test achievement integration with lesson completion
"""

import sys
import os
sys.path.append(os.getcwd())

def test_achievement_integration():
    """Test if achievement checking works with lesson completion"""
    
    try:
        from utils.achievements import check_achievements, check_badge_condition
        from data.users import load_user_data
        
        print('🔍 Testing achievement integration...')
        
        # Load user data to see current state
        users_data = load_user_data()
        print(f'✅ User data loaded: {len(users_data)} users found')
        
        # Find a user with lesson progress
        test_username = None
        for username, user_data in users_data.items():
            completed_lessons = user_data.get('completed_lessons', [])
            if len(completed_lessons) > 0:
                test_username = username
                print(f'📚 Found user "{username}" with {len(completed_lessons)} completed lessons')
                break
        
        if test_username:
            user_data = users_data[test_username]
            
            # Test first_lesson badge condition
            first_lesson_condition = check_badge_condition('first_lesson', user_data)
            print(f'🏅 First lesson badge condition: {first_lesson_condition}')
            
            # Test lesson_rookie badge condition (need 3 lessons)
            rookie_condition = check_badge_condition('lesson_rookie', user_data)
            print(f'🏅 Lesson rookie badge condition: {rookie_condition}')
            
            # Test calling check_achievements with lesson completion context
            print('🔍 Testing check_achievements function...')
            new_badges = check_achievements(test_username, 'lesson_completion', lesson_id='B1C1L1')
            print(f'🎉 New badges earned: {new_badges}')
            
        else:
            print('⚠️ No users found with completed lessons to test')
        
        print('✅ Achievement system integration test completed!')
        
    except Exception as e:
        print(f'❌ Test failed: {e}')
        import traceback
        traceback.print_exc()
        
if __name__ == "__main__":
    test_achievement_integration()
