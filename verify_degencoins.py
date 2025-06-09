#!/usr/bin/env python3
"""
Verify DegenCoins implementation in the shop and user data
"""

import json
import sys
import os

def verify_user_data():
    """Verify that users have degencoins field"""
    print("=== User Data Verification ===")
    
    try:
        with open('users_data.json', 'r', encoding='utf-8') as f:
            users_data = json.load(f)
        
        sample_users = list(users_data.keys())[:5]
        print(f"Checking {len(sample_users)} sample users for DegenCoins field:")
        
        for username in sample_users:
            user = users_data[username]
            xp = user.get('xp', 0)
            degencoins = user.get('degencoins', 'NOT FOUND')
            print(f"  User '{username}': XP={xp}, DegenCoins={degencoins}")
        
        # Check for any users missing degencoins
        missing_degencoins = []
        for username, user_data in users_data.items():
            if 'degencoins' not in user_data:
                missing_degencoins.append(username)
        
        if missing_degencoins:
            print(f"\n⚠️  Users missing degencoins field: {len(missing_degencoins)}")
            for username in missing_degencoins[:5]:  # Show first 5
                print(f"    - {username}")
        else:
            print("\n✅ All users have degencoins field!")
            
    except Exception as e:
        print(f"❌ Error reading user data: {e}")

def verify_shop_implementation():
    """Verify shop uses correct field name"""
    print("\n=== Shop Implementation Verification ===")
    
    try:
        with open('views/shop_new.py', 'r', encoding='utf-8') as f:
            shop_content = f.read()
        
        # Check for old field name (should be 0)
        old_field_count = shop_content.count('degen_coins')
        print(f"Occurrences of old field 'degen_coins': {old_field_count}")
        
        # Check for new field name (should be multiple)
        new_field_count = shop_content.count('degencoins')
        print(f"Occurrences of correct field 'degencoins': {new_field_count}")
        
        if old_field_count == 0 and new_field_count > 0:
            print("✅ Shop implementation uses correct field name!")
        else:
            print("❌ Shop implementation may have field name issues")
            
        # Check for DegenCoins display
        if "Twoje DegenCoins" in shop_content:
            print("✅ Shop displays DegenCoins balance!")
        else:
            print("❌ Shop may not display DegenCoins balance")
            
    except Exception as e:
        print(f"❌ Error reading shop file: {e}")

def verify_dashboard_display():
    """Verify dashboard displays DegenCoins"""
    print("\n=== Dashboard DegenCoins Display Verification ===")
    
    try:
        with open('views/dashboard.py', 'r', encoding='utf-8') as f:
            dashboard_content = f.read()
        
        # Check for DegenCoins in statistics
        if 'degencoins' in dashboard_content.lower():
            print("✅ Dashboard references DegenCoins!")
            
            # Look for the coin emoji
            if '🪙' in dashboard_content:
                print("✅ Dashboard uses coin emoji for DegenCoins!")
            else:
                print("⚠️  Dashboard might not use coin emoji")
        else:
            print("❌ Dashboard may not display DegenCoins")
            
    except Exception as e:
        print(f"❌ Error reading dashboard file: {e}")

if __name__ == "__main__":
    print("DegenCoins Implementation Verification")
    print("=" * 50)
    
    verify_user_data()
    verify_shop_implementation()
    verify_dashboard_display()
    
    print("\n" + "=" * 50)
    print("Verification complete!")
