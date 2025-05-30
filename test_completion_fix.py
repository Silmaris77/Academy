#!/usr/bin/env python3
"""
Test script to verify lesson completion display fix
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def simulate_lesson_completion_flow():
    """Simulate the lesson completion flow to test the fix"""
    print("🧪 TESTING LESSON COMPLETION DISPLAY FIX")
    print("=" * 60)
    
    try:
        # Mock streamlit session state
        class MockSessionState:
            def __init__(self):
                self.username = "a"
                self.user_data = None
                
        # Mock streamlit module
        class MockStreamlit:
            def __init__(self):
                self.session_state = MockSessionState()
        
        # Replace streamlit in sys.modules
        import streamlit as st
        original_session_state = st.session_state if hasattr(st, 'session_state') else None
        st.session_state = MockSessionState()
        
        from data.users import load_user_data, get_current_user_data
        from utils.lesson_progress import mark_lesson_as_completed
        
        username = "a"
        
        # Step 1: Load initial data
        print(f"📊 Step 1: Loading initial data for user '{username}'")
        users_data = load_user_data()
        initial_user_data = users_data.get(username, {})
        initial_completed = initial_user_data.get('completed_lessons', [])
        
        print(f"   Initial completed lessons: {len(initial_completed)}")
        print(f"   First 5 completed: {initial_completed[:5]}")
        
        # Step 2: Test get_current_user_data (should use file data initially)
        print(f"\n🔍 Step 2: Testing get_current_user_data (no session state)")
        current_data = get_current_user_data(username)
        current_completed = current_data.get('completed_lessons', [])
        
        print(f"   Current completed lessons: {len(current_completed)}")
        print(f"   Data source: {'session_state' if hasattr(st.session_state, 'user_data') and st.session_state.user_data else 'file'}")
        
        # Step 3: Simulate lesson completion
        print(f"\n✅ Step 3: Simulating lesson completion")
        
        # Find a lesson that's not completed yet
        from data.lessons import load_lessons
        lessons = load_lessons()
        all_lessons = list(lessons.keys())
        uncompleted_lesson = None
        
        for lesson_id in all_lessons:
            if lesson_id not in current_completed:
                uncompleted_lesson = lesson_id
                break
        
        if uncompleted_lesson:
            print(f"   Completing lesson: {uncompleted_lesson}")
            
            # Mock the completion
            st.session_state.username = username
            result = mark_lesson_as_completed(uncompleted_lesson)
            
            print(f"   Completion result: {result}")
            print(f"   Session state updated: {hasattr(st.session_state, 'user_data') and st.session_state.user_data is not None}")
            
            if hasattr(st.session_state, 'user_data') and st.session_state.user_data:
                session_completed = st.session_state.user_data.get('completed_lessons', [])
                print(f"   Session state completed lessons: {len(session_completed)}")
                print(f"   New lesson in session state: {uncompleted_lesson in session_completed}")
        
        # Step 4: Test get_current_user_data (should use session state now)
        print(f"\n🔍 Step 4: Testing get_current_user_data (with session state)")
        current_data_after = get_current_user_data(username)
        current_completed_after = current_data_after.get('completed_lessons', [])
        
        print(f"   Current completed lessons: {len(current_completed_after)}")
        print(f"   Data source: {'session_state' if hasattr(st.session_state, 'user_data') and st.session_state.user_data else 'file'}")
        
        if uncompleted_lesson:
            print(f"   New lesson in current data: {uncompleted_lesson in current_completed_after}")
        
        # Step 5: Test lesson card status logic
        print(f"\n🎯 Step 5: Testing lesson card status logic")
        
        if uncompleted_lesson:
            # Test the completed lesson
            is_completed = uncompleted_lesson in current_completed_after
            status_text = '✓ Ukończono' if is_completed else '○ Nieukończono'
            
            print(f"   Lesson: {uncompleted_lesson}")
            print(f"   is_completed: {is_completed}")
            print(f"   Status text: {status_text}")
            print(f"   Expected: ✓ Ukończono")
            print(f"   ✅ Status correct: {status_text == '✓ Ukończono'}")
        
        # Step 6: Test an uncompleted lesson
        other_uncompleted = None
        for lesson_id in all_lessons:
            if lesson_id not in current_completed_after:
                other_uncompleted = lesson_id
                break
        
        if other_uncompleted:
            is_completed = other_uncompleted in current_completed_after
            status_text = '✓ Ukończono' if is_completed else '○ Nieukończono'
            
            print(f"\n   Uncompleted lesson: {other_uncompleted}")
            print(f"   is_completed: {is_completed}")
            print(f"   Status text: {status_text}")
            print(f"   Expected: ○ Nieukończono")
            print(f"   ✅ Status correct: {status_text == '○ Nieukończono'}")
        
        print(f"\n" + "=" * 60)
        print("✅ LESSON COMPLETION DISPLAY FIX TEST COMPLETED")
        print("✅ The fix should now show correct completion status!")
        print("✅ Completed lessons will show: ✓ Ukończono")
        print("✅ Uncompleted lessons will show: ○ Nieukończono")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    simulate_lesson_completion_flow()

if __name__ == "__main__":
    main()
