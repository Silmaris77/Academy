#!/usr/bin/env python3
"""Simple test for avatar system"""

import json
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.getcwd())

def test_basic_functionality():
    print('=== Avatar System Integration Test ===')
    
    # Test 1: Check user data
    print('\n1. Checking user data structure...')
    try:
        with open('users_data.json', 'r', encoding='utf-8') as f:
            users_data = json.load(f)
        user_data = users_data.get('a', {})
        print(f'✅ User "a" data loaded')
        print(f'   Inventory: {user_data.get("inventory", {})}')
        print(f'   Active avatar: {user_data.get("active_avatar", "Not set")}')
    except Exception as e:
        print(f'❌ Error loading user data: {e}')
        return
    
    # Test 2: Check avatar definitions
    print('\n2. Checking avatar definitions...')
    try:
        from config.settings import USER_AVATARS
        print(f'✅ USER_AVATARS loaded with {len(USER_AVATARS)} avatars')
        premium_avatars = ['diamond_degen', 'crypto_wizard', 'moon_hunter']
        for premium in premium_avatars:
            if premium in USER_AVATARS:
                print(f'   {premium}: {USER_AVATARS[premium]} ✅')
            else:
                print(f'   {premium}: Missing ❌')
    except Exception as e:
        print(f'❌ Error loading avatar definitions: {e}')
        return
    
    # Test 3: Check inventory functions
    print('\n3. Testing inventory functions...')
    try:
        from utils.inventory import get_user_inventory, activate_item
        inventory = get_user_inventory('a')
        print(f'✅ get_user_inventory works')
        print(f'   User avatars: {inventory.get("avatars", [])}')
        
        # Test activation if user has avatars
        if inventory.get('avatars'):
            test_avatar = inventory['avatars'][0]
            print(f'\n   Testing activation of: {test_avatar}')
            result = activate_item('a', 'avatar', test_avatar)
            print(f'   Activation result: {result}')
            
            # Verify activation
            with open('users_data.json', 'r', encoding='utf-8') as f:
                updated_data = json.load(f)
            updated_user = updated_data.get('a', {})
            print(f'   New active_avatar: {updated_user.get("active_avatar", "Not set")}')
        else:
            print('   No avatars in inventory to test')
            
    except Exception as e:
        print(f'❌ Error testing inventory functions: {e}')
        import traceback
        traceback.print_exc()
        return
    
    print('\n✅ All tests completed successfully!')

if __name__ == "__main__":
    test_basic_functionality()
