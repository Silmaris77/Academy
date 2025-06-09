#!/usr/bin/env python3
"""
Test script to verify that DegenCoins are awarded alongside XP points.
"""

import json
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_user_data():
    """Load user data from JSON file"""
    file_path = 'users_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def test_degencoins_system():
    """Test that DegenCoins are properly initialized and displayed"""
    users_data = load_user_data()
    
    print("=== DegenCoins System Test ===\n")
    
    # Test 1: Check if DegenCoins field exists for all users
    users_without_degencoins = []
    for username, user_data in users_data.items():
        if 'degencoins' not in user_data:
            users_without_degencoins.append(username)
    
    if users_without_degencoins:
        print(f"❌ FAIL: {len(users_without_degencoins)} users missing DegenCoins field:")
        for username in users_without_degencoins[:5]:  # Show first 5
            print(f"  - {username}")
        if len(users_without_degencoins) > 5:
            print(f"  ... and {len(users_without_degencoins) - 5} more")
    else:
        print("✅ PASS: All users have DegenCoins field initialized")
    
    # Test 2: Check XP and DegenCoins values for sample users
    print("\n=== Sample User Statistics ===")
    sample_users = list(users_data.keys())[:5]  # First 5 users
    
    for username in sample_users:
        user_data = users_data[username]
        xp = user_data.get('xp', 0)
        degencoins = user_data.get('degencoins', 0)
        level = user_data.get('level', 1)
        completed_lessons = len(user_data.get('completed_lessons', []))
        
        print(f"User: {username}")
        print(f"  XP: {xp}")
        print(f"  DegenCoins: {degencoins}")
        print(f"  Level: {level}")
        print(f"  Completed Lessons: {completed_lessons}")
        print(f"  XP == DegenCoins: {'✅' if xp == degencoins else '❌'}")
        print()
    
    # Test 3: Check that XP equals DegenCoins for most users (they should match after initialization)
    xp_degencoins_match = 0
    total_users = len(users_data)
    
    for username, user_data in users_data.items():
        xp = user_data.get('xp', 0)
        degencoins = user_data.get('degencoins', 0)
        if xp == degencoins:
            xp_degencoins_match += 1
    
    match_percentage = (xp_degencoins_match / total_users) * 100
    print(f"=== XP vs DegenCoins Consistency ===")
    print(f"Users with matching XP and DegenCoins: {xp_degencoins_match}/{total_users} ({match_percentage:.1f}%)")
    
    if match_percentage >= 95:
        print("✅ PASS: XP and DegenCoins are consistent for most users")
    else:
        print("⚠️  WARNING: Some users have mismatched XP and DegenCoins")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_degencoins_system()
