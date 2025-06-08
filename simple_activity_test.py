#!/usr/bin/env python3
"""
Simple test to check if imports work
"""

try:
    import json
    print("✓ json imported")
    
    import os
    print("✓ os imported")
    
    from data.users import add_recent_activity, get_current_user_data
    print("✓ data.users imported")
    
    from utils.time_utils import calculate_relative_time
    print("✓ utils.time_utils imported")
    
    from datetime import datetime, timezone
    print("✓ datetime imported")
    
    # Test adding activity
    print("\nTesting add_recent_activity...")
    add_recent_activity("a", "degen_type_discovered", {"degen_type": "Bitcoin Maximalist"})
    print("✓ Activity added successfully")
    
    # Test getting user data
    print("\nTesting get_current_user_data...")
    user_data = get_current_user_data("a")
    print(f"✓ User data retrieved: {type(user_data)}")
    
    if user_data and 'recent_activities' in user_data:
        activities = user_data['recent_activities']
        print(f"✓ Found {len(activities)} activities")
        if activities:
            print(f"Latest activity: {activities[0]}")
    else:
        print("⚠ No recent_activities found")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\nTest completed.")
