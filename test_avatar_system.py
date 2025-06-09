#!/usr/bin/env python3
"""Test script for avatar system integration"""

import json
from utils.inventory import get_user_inventory, activate_item
from config.settings import USER_AVATARS

def test_avatar_system():
    print('=== Testing Avatar System Integration ===')
    print()

    # 1. Check user data structure
    with open('users_data.json', 'r', encoding='utf-8') as f:
        users_data = json.load(f)

    user_data = users_data.get('a', {})
    print('User a inventory structure:')
    print(f'  inventory: {user_data.get("inventory", {})}')
    print(f'  active_avatar: {user_data.get("active_avatar", "Not set")}')
    print()

    # 2. Test inventory retrieval
    inventory = get_user_inventory('a')
    print('Retrieved inventory:')
    print(f'  avatars: {inventory.get("avatars", [])}')
    print()

    # 3. Test avatar definitions
    print('Available avatar definitions:')
    for avatar_id, emoji in USER_AVATARS.items():
        print(f'  {avatar_id}: {emoji}')
    print()

    # 4. Test avatar activation
    if inventory.get('avatars'):
        test_avatar = inventory['avatars'][0]  # First owned avatar
        print(f'Testing activation of: {test_avatar}')
        try:
            result = activate_item('a', 'avatar', test_avatar)
            print(f'Activation result: {result}')
            
            # Check if it was set
            with open('users_data.json', 'r', encoding='utf-8') as f:
                updated_data = json.load(f)
            updated_user = updated_data.get('a', {})
            print(f'Updated active_avatar: {updated_user.get("active_avatar", "Not set")}')
        except Exception as e:
            print(f'Activation error: {e}')
    else:
        print('No avatars found in inventory to test activation')

    print()
    print('=== Testing Premium Avatar Access ===')
    
    # 5. Test premium avatar filtering logic (like in personalization)
    owned_premium_avatars = inventory.get('avatars', [])
    premium_avatars = {"diamond_degen", "crypto_wizard", "moon_hunter"}
    
    print('Premium avatar access:')
    for premium_avatar in premium_avatars:
        owned = premium_avatar in owned_premium_avatars
        emoji = USER_AVATARS.get(premium_avatar, '❓')
        status = "✅ OWNED" if owned else "🔒 LOCKED"
        print(f'  {premium_avatar} {emoji}: {status}')

if __name__ == "__main__":
    test_avatar_system()
