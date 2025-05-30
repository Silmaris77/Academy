#!/usr/bin/env python3
"""
Simple test for achievement integration
"""

import sys
import os
sys.path.append(os.getcwd())

def test_basic_imports():
    """Test basic imports work"""
    try:
        print("Testing imports...")
        from utils.achievements import check_achievements
        print("✅ Achievement system imported successfully")
        
        from data.users import load_user_data
        print("✅ User data system imported successfully")
        
        from utils.lesson_progress import mark_lesson_as_completed
        print("✅ Lesson progress system imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_user_data():
    """Test loading user data"""
    try:
        from data.users import load_user_data
        users_data = load_user_data()
        print(f"✅ User data loaded: {len(users_data)} users found")
        
        # Find any user with data
        for username, user_data in users_data.items():
            completed_lessons = user_data.get('completed_lessons', [])
            badges = user_data.get('badges', [])
            print(f"User '{username}': {len(completed_lessons)} lessons, {len(badges)} badges")
            if len(completed_lessons) > 0:
                print(f"  Sample completed lessons: {completed_lessons[:3]}")
            if len(badges) > 0:
                print(f"  Sample badges: {badges[:3]}")
            break
        
        return True
    except Exception as e:
        print(f"❌ User data error: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Starting simple achievement integration test...")
    
    if test_basic_imports():
        test_user_data()
    
    print("✅ Test completed!")
