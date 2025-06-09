import json
import sys
import os

print("Starting avatar verification...")

# Test 1: Load user data
print("\n1. Loading user data...")
with open('users_data.json', 'r', encoding='utf-8') as f:
    users_data = json.load(f)

user_a = users_data.get('a', {})
print(f"User 'a' inventory: {user_a.get('inventory', {})}")
print(f"User 'a' active_avatar: {user_a.get('active_avatar', 'Not set')}")

# Test 2: Check avatar definitions
print("\n2. Checking avatar definitions...")
sys.path.append('.')
try:
    from config.settings import USER_AVATARS
    premium_avatars = ['diamond_degen', 'crypto_wizard', 'moon_hunter']
    print("Premium avatar definitions:")
    for avatar in premium_avatars:
        if avatar in USER_AVATARS:
            print(f"  {avatar}: {USER_AVATARS[avatar]} ✅")
        else:
            print(f"  {avatar}: Missing ❌")
except Exception as e:
    print(f"Error loading avatars: {e}")

# Test 3: Test inventory function
print("\n3. Testing inventory function...")
try:
    from utils.inventory import get_user_inventory
    inventory = get_user_inventory('a')
    print(f"Retrieved avatars: {inventory.get('avatars', [])}")
except Exception as e:
    print(f"Error with inventory: {e}")

print("\nVerification complete!")
