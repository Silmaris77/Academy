#!/usr/bin/env python3
"""
Test to verify dashboard activities display
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from data.users import get_current_user_data
from utils.time_utils import calculate_relative_time
from utils.lesson_utils import get_lesson_title

def test_dashboard_activities():
    """Test the dashboard activities display logic"""
    
    print("Testing dashboard activities display...")
    
    # Get user data
    user_data = get_current_user_data("a")
    
    if not user_data:
        print("❌ User data not found")
        return
    
    print(f"✓ Found user data for user 'a'")
    
    recent_activities = user_data.get('recent_activities', [])
    print(f"✓ Found {len(recent_activities)} recent activities")
    
    if not recent_activities:
        print("❌ No recent activities found")
        return
    
    # Process activities like the dashboard does
    for i, activity_data in enumerate(recent_activities[:5]):
        print(f"\n--- Activity {i+1} ---")
        
        activity_type = activity_data.get("type")
        details = activity_data.get("details", {})
        timestamp_str = activity_data.get("timestamp")
        
        print(f"Type: {activity_type}")
        print(f"Details: {details}")
        print(f"Timestamp: {timestamp_str}")
        
        # Calculate relative time
        time_text = calculate_relative_time(timestamp_str) if timestamp_str else "Nieznana data"
        print(f"Relative time: {time_text}")
        
        # Determine title and icon
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
        
        print(f"Display title: {title}")
        print(f"Icon: {icon}")
        print(f"Color: {color}")

if __name__ == "__main__":
    test_dashboard_activities()
