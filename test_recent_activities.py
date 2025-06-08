#!/usr/bin/env python3
"""
Test script to verify recent activities functionality
"""

import json
import os
from data.users import add_recent_activity, get_current_user_data
from utils.time_utils import calculate_relative_time
from datetime import datetime, timezone

def test_recent_activities():
    """Test the recent activities functionality"""
      # Test username - replace with actual username from your system
    test_username = "a"  # Using existing user
    
    print(f"Testing recent activities for user: {test_username}")
    
    # Add a test activity
    print("\n1. Adding test activity...")
    add_recent_activity(
        test_username,
        "degen_type_discovered",
        {"degen_type": "Bitcoin Maximalist"}
    )
    
    # Get user data and check activities
    print("\n2. Retrieving user data...")
    user_data = get_current_user_data(test_username)
    
    if user_data:
        recent_activities = user_data.get('recent_activities', [])
        print(f"Found {len(recent_activities)} recent activities")
        
        for i, activity in enumerate(recent_activities):
            print(f"\nActivity {i+1}:")
            print(f"  Type: {activity.get('type')}")
            print(f"  Details: {activity.get('details')}")
            print(f"  Timestamp: {activity.get('timestamp')}")
            
            # Test relative time calculation
            timestamp = activity.get('timestamp')
            if timestamp:
                relative_time = calculate_relative_time(timestamp)
                print(f"  Relative time: {relative_time}")
    else:
        print("User data not found!")
    
    # Check raw JSON file
    print("\n3. Checking raw JSON file...")
    users_file = os.path.join(os.path.dirname(__file__), 'users_data.json')
    if os.path.exists(users_file):
        with open(users_file, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
            
        if test_username in users_data:
            user_raw_data = users_data[test_username]
            activities = user_raw_data.get('recent_activities', [])
            print(f"Raw JSON shows {len(activities)} activities for {test_username}")
            
            for activity in activities:
                print(f"  Raw activity: {activity}")
        else:
            print(f"User {test_username} not found in JSON file")
            print(f"Available users: {list(users_data.keys())}")
    else:
        print("users_data.json file not found!")

if __name__ == "__main__":
    test_recent_activities()
