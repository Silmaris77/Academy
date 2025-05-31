#!/usr/bin/env python3
"""
Test script to verify timestamp functionality for degen test completion.
"""

import sys
import os
sys.path.append('.')

def test_timestamp_functionality():
    """Test the new timestamp functionality"""
    print("🧪 TESTING TIMESTAMP FUNCTIONALITY")
    print("=" * 50)
    
    try:
        # Test time utility functions
        from utils.time_utils import calculate_relative_time, get_current_timestamp, get_current_iso_timestamp
        
        print("✅ Successfully imported time utility functions")
        
        # Test current timestamp generation
        current_timestamp = get_current_timestamp()
        current_iso = get_current_iso_timestamp()
        
        print(f"📅 Current timestamp: {current_timestamp}")
        print(f"📅 Current ISO timestamp: {current_iso}")
        
        # Test relative time calculation with various scenarios
        test_cases = [
            ("2024-01-01 12:00:00", "should be very old"),
            ("2024-12-01 12:00:00", "should be recent"),
            (current_timestamp, "should be 'przed chwilą'")
        ]
        
        print("\n🕒 Testing relative time calculations:")
        for timestamp, description in test_cases:
            relative_time = calculate_relative_time(timestamp)
            print(f"  {timestamp} -> {relative_time} ({description})")
        
        # Test with users data to see if test_completion_date field exists
        from data.users import load_user_data
        users_data = load_user_data()
        
        print(f"\n👥 Checking user data for test completion timestamps:")
        users_with_test = 0
        users_with_timestamp = 0
        
        for username, user_data in users_data.items():
            test_taken = user_data.get('test_taken', False)
            has_timestamp = 'test_completion_date' in user_data
            
            if test_taken:
                users_with_test += 1
                if has_timestamp:
                    users_with_timestamp += 1
                    timestamp = user_data['test_completion_date']
                    relative_time = calculate_relative_time(timestamp)
                    print(f"  ✅ {username}: test completed {relative_time}")
                else:
                    print(f"  ⚠️  {username}: test completed but no timestamp")
        
        print(f"\n📊 Summary:")
        print(f"  Users with completed test: {users_with_test}")
        print(f"  Users with timestamp: {users_with_timestamp}")
        print(f"  Missing timestamps: {users_with_test - users_with_timestamp}")
        
        if users_with_test > users_with_timestamp:
            print(f"\n💡 Note: {users_with_test - users_with_timestamp} users need to retake the test to get timestamps")
        
        print("\n✅ Timestamp functionality test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_timestamp_functionality()
