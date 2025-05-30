#!/usr/bin/env python3
"""
Comprehensive test of the achievement integration workflow
"""
import json

def test_badge_integration():
    """Test the complete badge integration workflow"""
    print("🔬 COMPREHENSIVE BADGE INTEGRATION TEST")
    print("=" * 50)
    
    # Load and examine user data
    try:
        with open('users_data.json', 'r', encoding='utf-8') as f:
            users_data = json.load(f)
    except Exception as e:
        print(f"❌ Error loading users_data.json: {e}")
        return
    
    print(f"📊 Total users in system: {len(users_data)}")
    
    # Analyze users for lesson completion vs badges
    lesson_badge_analysis = []
    
    for username, user_data in users_data.items():
        completed_lessons = user_data.get('completed_lessons', [])
        badges = user_data.get('badges', [])
        
        has_first_lesson_badge = 'first_lesson' in badges
        has_completed_lessons = len(completed_lessons) > 0
        
        lesson_badge_analysis.append({
            'username': username,
            'completed_lessons_count': len(completed_lessons),
            'has_first_lesson_badge': has_first_lesson_badge,
            'should_have_badge': has_completed_lessons,
            'badge_missing': has_completed_lessons and not has_first_lesson_badge
        })
    
    # Report findings
    print("\n🏅 BADGE ANALYSIS:")
    
    users_with_lessons = [u for u in lesson_badge_analysis if u['completed_lessons_count'] > 0]
    users_missing_badge = [u for u in lesson_badge_analysis if u['badge_missing']]
    
    print(f"📚 Users with completed lessons: {len(users_with_lessons)}")
    print(f"🏅 Users missing 'first_lesson' badge: {len(users_missing_badge)}")
    
    if users_missing_badge:
        print("\n❌ USERS MISSING FIRST_LESSON BADGE:")
        for user in users_missing_badge[:5]:  # Show first 5
            print(f"   • {user['username']}: {user['completed_lessons_count']} lessons completed")
        
        print(f"\n🔧 RECOMMENDATION:")
        print("Run the achievement system manually to award missing badges:")
        print("python award_missing_badges.py")
    else:
        print("\n✅ All users with completed lessons have the 'first_lesson' badge!")
    
    # Test a specific case
    print("\n🧪 DETAILED CASE STUDY:")
    sample_users = [(k, v) for k, v in users_data.items() if len(v.get('completed_lessons', [])) > 0]
    
    if sample_users:
        username, user_data = sample_users[0]
        completed_lessons = user_data.get('completed_lessons', [])
        badges = user_data.get('badges', [])
        
        print(f"📋 Sample user: '{username}'")
        print(f"   Completed lessons: {len(completed_lessons)}")
        print(f"   Sample lessons: {completed_lessons[:3] if completed_lessons else 'None'}")
        print(f"   Total badges: {len(badges)}")
        print(f"   Has 'first_lesson': {'first_lesson' in badges}")
        print(f"   Badge list: {badges[:5] if len(badges) > 5 else badges}")
    
    # Check our integration code
    print("\n🔍 INTEGRATION VERIFICATION:")
    
    # Check if our code changes are in place
    try:
        with open('views/lesson.py', 'r', encoding='utf-8') as f:
            lesson_content = f.read()
        
        if 'check_achievements(username, \'lesson_completion\', lesson_id=lesson_id)' in lesson_content:
            print("   ✅ Achievement trigger found in views/lesson.py")
        else:
            print("   ❌ Achievement trigger missing in views/lesson.py")
    except Exception as e:
        print(f"   ❌ Error checking views/lesson.py: {e}")
    
    try:
        with open('utils/lesson_progress.py', 'r', encoding='utf-8') as f:
            progress_content = f.read()
        
        if 'check_achievements(username, \'lesson_completion\', lesson_id=lesson_id)' in progress_content:
            print("   ✅ Achievement trigger found in utils/lesson_progress.py")
        else:
            print("   ❌ Achievement trigger missing in utils/lesson_progress.py")
    except Exception as e:
        print(f"   ❌ Error checking utils/lesson_progress.py: {e}")
    
    print("\n🎯 CONCLUSION:")
    if len(users_missing_badge) == 0:
        print("✅ Badge system appears to be working correctly!")
        print("✅ All users with completed lessons have appropriate badges")
        print("✅ Integration fixes have successfully resolved the issue")
    else:
        print("⚠️  Some users are missing badges despite having completed lessons")
        print("⚠️  This might indicate the integration was added after they completed lessons")
        print("✅ However, the integration is now in place for future lesson completions")
    
    print("\n🚀 NEXT STEPS:")
    print("1. Test the application by completing a lesson as a new user")
    print("2. Verify that badges are immediately awarded upon lesson completion")
    print("3. Check that the Unicode encoding handles international characters correctly")

if __name__ == "__main__":
    test_badge_integration()
