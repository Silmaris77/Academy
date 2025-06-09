#!/usr/bin/env python3
"""
Script to initialize DegenCoins for existing users.
This ensures all users have the degencoins field in their data.
"""

import json
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from data.users import load_user_data, save_user_data
    print("Successfully imported user data functions")
except ImportError as e:
    print(f"Import error: {e}")
    # Fallback to direct file operations
    def load_user_data():
        file_path = 'users_data.json'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_user_data(users_data):
        file_path = 'users_data.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(users_data, f, indent=2, ensure_ascii=False)

def initialize_degencoins_for_existing_users():
    """Initialize DegenCoins field for users who don't have it"""
    users_data = load_user_data()
    updated_users = 0
    
    for username, user_data in users_data.items():
        if 'degencoins' not in user_data:
            # Initialize DegenCoins equal to current XP
            current_xp = user_data.get('xp', 0)
            user_data['degencoins'] = current_xp
            updated_users += 1
            print(f"Initialized DegenCoins for user '{username}': {current_xp} DegenCoins")
    
    if updated_users > 0:
        save_user_data(users_data)
        print(f"\nSuccessfully updated {updated_users} users with DegenCoins.")
    else:
        print("All users already have DegenCoins initialized.")
    
    return updated_users

if __name__ == "__main__":
    print("Initializing DegenCoins for existing users...")
    initialize_degencoins_for_existing_users()
    print("Done!")
