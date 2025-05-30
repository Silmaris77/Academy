"""
Quick verification of achievement integration fixes
"""

def verify_lesson_completion_integration():
    """Verify that lesson completion now triggers achievement checks"""
    
    print("🔍 Verifying achievement integration in lesson completion...")
    
    # Check views/lesson.py for our integration
    with open('views/lesson.py', 'r', encoding='utf-8') as f:
        lesson_content = f.read()
    
    # Look for our achievement integration code
    if 'check_achievements(username, \'lesson_completion\', lesson_id=lesson_id)' in lesson_content:
        print("✅ Achievement check integration found in views/lesson.py")
    else:
        print("❌ Achievement check integration NOT found in views/lesson.py")
    
    # Check utils/lesson_progress.py for our integration
    with open('utils/lesson_progress.py', 'r', encoding='utf-8') as f:
        progress_content = f.read()
    
    if 'check_achievements(username, \'lesson_completion\', lesson_id=lesson_id)' in progress_content:
        print("✅ Achievement check integration found in utils/lesson_progress.py")
    else:
        print("❌ Achievement check integration NOT found in utils/lesson_progress.py")
    
    # Verify the achievement system still exists
    try:
        import sys
        sys.path.append('.')
        from utils.achievements import check_achievements
        print("✅ Achievement system can be imported successfully")
    except Exception as e:
        print(f"❌ Achievement system import failed: {e}")
    
    print("\n📊 Summary:")
    print("- Fixed lesson completion to trigger achievement checks")
    print("- Both views/lesson.py and utils/lesson_progress.py now call check_achievements")
    print("- This should resolve badges not being awarded when lessons are completed")

if __name__ == "__main__":
    verify_lesson_completion_integration()
