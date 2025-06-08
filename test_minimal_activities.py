#!/usr/bin/env python3
"""
Minimal test to simulate how dashboard shows recent activities
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

def test_activities_display():
    """Test how activities should be displayed in dashboard"""
    
    # Import required modules
    from data.users import get_current_user_data
    from utils.time_utils import calculate_relative_time
    from utils.lesson_utils import get_lesson_title
    
    print("=== Testing Recent Activities Display ===")
    
    # Get user data
    user_data = get_current_user_data("a")
    
    if not user_data:
        print("❌ No user data found for user 'a'")
        return
    
    recent_activities = user_data.get('recent_activities', [])
    print(f"Found {len(recent_activities)} recent activities")
    
    if not recent_activities:
        print("🔴 'Brak ostatnich aktywności.' would be displayed")
        return
    
    print("🟢 Activities found! Here's what would be displayed:")
    print()
    
    # Simulate what dashboard.py does
    for i, activity_data in enumerate(recent_activities[:5]):
        activity_type = activity_data.get("type")
        details = activity_data.get("details", {})
        timestamp_str = activity_data.get("timestamp")
        
        time_text = calculate_relative_time(timestamp_str) if timestamp_str else "Nieznana data"
        title = "Nieznana aktywność"
        icon = "🔔"
        color = "#7f8c8d"
        
        if activity_type == "lesson_completed":
            lesson_id = details.get("lesson_id", "Nieznana lekcja")
            lesson_title = get_lesson_title(lesson_id)
            title = f"Ukończono lekcję: {lesson_title}"
            icon = "✅"
            color = "#27ae60"
        elif activity_type == "degen_type_discovered":
            degen_type_name = details.get("degen_type", "Nieznany typ")
            title = f"Odkryto typ inwestora: {degen_type_name}"
            icon = "🧬"
            color = "#3498db"
        elif activity_type == "daily_streak_started":
            title = "Rozpoczęto nową passę dzienną"
            icon = "🔥"
            color = "#e67e22"
        elif activity_type == "badge_earned":
            badge_names = details.get("badge_names", [])
            if badge_names:
                title = f"Zdobyto odznakę: {', '.join(badge_names)}"
            else:
                title = "Zdobyto nową odznakę"
            icon = "🏆"
            color = "#f1c40f"
        
        print(f"Activity {i+1}:")
        print(f"  {icon} {title}")
        print(f"  {time_text}")
        print()
    
    print("✅ Recent activities should display correctly in the dashboard!")

if __name__ == "__main__":
    try:
        test_activities_display()
    except Exception as e:
        print(f"❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
