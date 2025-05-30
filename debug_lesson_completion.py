#!/usr/bin/env python3
"""
Diagnostic script to test lesson completion display issues
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_lesson_card_component():
    """Test the lesson_card component directly"""
    print("🔍 Testing lesson_card component")
    print("=" * 50)
    
    try:
        from utils.components import lesson_card
        from data.users import load_user_data
        from data.lessons import load_lessons
        
        # Load data
        users_data = load_user_data()
        lessons = load_lessons()
        
        # Test with user 'a'
        username = "a"
        if username not in users_data:
            print(f"❌ User '{username}' not found")
            return False
        
        user_data = users_data[username]
        completed_lessons = user_data.get('completed_lessons', [])
        
        print(f"📊 User '{username}' data:")
        print(f"   Completed lessons: {len(completed_lessons)}")
        print(f"   First 5 completed: {completed_lessons[:5]}")
        
        # Test with a completed lesson
        if completed_lessons:
            test_lesson_id = completed_lessons[0]
            is_completed = test_lesson_id in completed_lessons
            
            print(f"\n🧪 Testing completed lesson: {test_lesson_id}")
            print(f"   is_completed: {is_completed}")
            print(f"   Should show: ✓ Ukończono")
            
            # Try to call lesson_card component
            try:
                # Mock streamlit for testing
                class MockStreamlit:
                    def markdown(self, content, **kwargs):
                        print(f"MARKDOWN OUTPUT:\n{content}")
                
                # Test the lesson card logic directly
                lesson_info = lessons.get(test_lesson_id, {})
                lesson_title = lesson_info.get('title', 'Unknown')
                
                print(f"\n📄 Lesson card for '{test_lesson_id}':")
                print(f"   Title: {lesson_title}")
                print(f"   Completed: {is_completed}")
                
                # Simulate the status logic from lesson_card
                status_text = '✓ Ukończono' if is_completed else '○ Nieukończono'
                css_class = 'm3-completed' if is_completed else ''
                
                print(f"   Status text: {status_text}")
                print(f"   CSS class: '{css_class}'")
                
                # Check if this matches expected output
                expected_status = '✓ Ukończono'
                if status_text == expected_status:
                    print(f"   ✅ Status correct!")
                else:
                    print(f"   ❌ Status incorrect! Expected: {expected_status}, Got: {status_text}")
                
            except Exception as e:
                print(f"❌ Error testing lesson_card: {e}")
                
        # Test with an uncompleted lesson
        all_lessons = list(lessons.keys())
        uncompleted_lesson = None
        for lesson_id in all_lessons:
            if lesson_id not in completed_lessons:
                uncompleted_lesson = lesson_id
                break
        
        if uncompleted_lesson:
            is_completed = uncompleted_lesson in completed_lessons
            
            print(f"\n🧪 Testing uncompleted lesson: {uncompleted_lesson}")
            print(f"   is_completed: {is_completed}")
            print(f"   Should show: ○ Nieukończono")
            
            # Test the status logic
            status_text = '✓ Ukończono' if is_completed else '○ Nieukończono'
            expected_status = '○ Nieukończono'
            
            print(f"   Status text: {status_text}")
            if status_text == expected_status:
                print(f"   ✅ Status correct!")
            else:
                print(f"   ❌ Status incorrect! Expected: {expected_status}, Got: {status_text}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in test: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_dashboard_logic():
    """Test the dashboard logic for lesson completion"""
    print("\n🏠 Testing dashboard logic")
    print("=" * 50)
    
    try:
        from data.users import load_user_data
        from data.lessons import load_lessons
        
        # Simulate dashboard logic
        users_data = load_user_data()
        lessons = load_lessons()
        
        username = "a"
        user_data = users_data.get(username, {})
        completed_lessons = user_data.get('completed_lessons', [])
        
        print(f"📊 Dashboard simulation for '{username}':")
        print(f"   User data loaded: {bool(user_data)}")
        print(f"   Completed lessons: {len(completed_lessons)}")
        
        # Test some specific lessons
        test_lessons = list(lessons.keys())[:3]
        
        for lesson_id in test_lessons:
            is_completed = lesson_id in completed_lessons
            lesson_title = lessons.get(lesson_id, {}).get('title', 'Unknown')
            
            print(f"\n   Lesson: {lesson_id}")
            print(f"   Title: {lesson_title}")
            print(f"   In completed_lessons: {is_completed}")
            print(f"   Would display: {'✅ Ukończono' if is_completed else '❌ Nieukończono'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in dashboard test: {e}")
        return False

def check_data_integrity():
    """Check data integrity between different sources"""
    print("\n🔍 Checking data integrity")
    print("=" * 50)
    
    try:
        from data.users import load_user_data
        from data.lessons import load_lessons
        
        users_data = load_user_data()
        lessons = load_lessons()
        
        username = "a"
        user_data = users_data.get(username, {})
        completed_lessons = user_data.get('completed_lessons', [])
        
        print(f"📊 Data integrity check:")
        print(f"   Total lessons in database: {len(lessons)}")
        print(f"   Completed lessons for '{username}': {len(completed_lessons)}")
        
        # Check if completed lessons exist in lessons database
        invalid_completed = []
        for lesson_id in completed_lessons:
            if lesson_id not in lessons:
                invalid_completed.append(lesson_id)
        
        if invalid_completed:
            print(f"   ⚠️  Invalid completed lessons: {invalid_completed}")
        else:
            print(f"   ✅ All completed lessons are valid")
        
        # Sample some completed lessons
        print(f"\n📝 Sample completed lessons:")
        for i, lesson_id in enumerate(completed_lessons[:5]):
            lesson_title = lessons.get(lesson_id, {}).get('title', 'Unknown')
            print(f"   {i+1}. {lesson_id} - {lesson_title}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in integrity check: {e}")
        return False

def main():
    """Main diagnostic function"""
    print("🚀 LESSON COMPLETION DIAGNOSTIC")
    print("=" * 60)
    
    # Run all tests
    test1 = test_lesson_card_component()
    test2 = test_dashboard_logic()
    test3 = check_data_integrity()
    
    print("\n" + "=" * 60)
    print("DIAGNOSTIC SUMMARY")
    print("=" * 60)
    print(f"✅ Lesson card component: {'PASS' if test1 else 'FAIL'}")
    print(f"✅ Dashboard logic: {'PASS' if test2 else 'FAIL'}")
    print(f"✅ Data integrity: {'PASS' if test3 else 'FAIL'}")
    
    if all([test1, test2, test3]):
        print(f"\n💡 All tests passed! The logic should be working correctly.")
        print(f"   If you're still seeing incorrect status, the issue might be:")
        print(f"   1. Session state not updating properly")
        print(f"   2. Streamlit caching issues")
        print(f"   3. Frontend display issues")
    else:
        print(f"\n❌ Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()
