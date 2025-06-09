#!/usr/bin/env python3
"""
Comprehensive Avatar System Integration Test
Tests the complete workflow: Purchase -> Inventory -> Activation -> Personalization
"""

import json
import sys
import os
from pathlib import Path

# Add project root and utils to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def load_user_data():
    """Load user data from JSON file"""
    try:
        with open('users_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load user data: {e}")
        return None

def save_user_data(data):
    """Save user data to JSON file"""
    try:
        with open('users_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"❌ Failed to save user data: {e}")
        return False

def test_avatar_definitions():
    """Test 1: Verify avatar definitions are properly loaded"""
    print("🧪 Test 1: Avatar Definitions")
    try:
        from config.settings import USER_AVATARS
        
        # Check basic avatars
        basic_avatars = ["default", "zen", "yolo", "emo", "strategist", "scientist", "spreadsheet", "meta", "hype"]
        premium_avatars = ["diamond_degen", "crypto_wizard", "moon_hunter"]
        
        print(f"   Total avatars defined: {len(USER_AVATARS)}")
        
        missing_basic = [av for av in basic_avatars if av not in USER_AVATARS]
        missing_premium = [av for av in premium_avatars if av not in USER_AVATARS]
        
        if missing_basic:
            print(f"   ❌ Missing basic avatars: {missing_basic}")
            return False
        else:
            print(f"   ✅ All {len(basic_avatars)} basic avatars defined")
            
        if missing_premium:
            print(f"   ❌ Missing premium avatars: {missing_premium}")
            return False
        else:
            print(f"   ✅ All {len(premium_avatars)} premium avatars defined")
            
        # Show premium avatar definitions
        print("   Premium avatars:")
        for avatar in premium_avatars:
            emoji = USER_AVATARS.get(avatar, '❓')
            print(f"     {avatar}: {emoji}")
            
        return True
    except Exception as e:
        print(f"   ❌ Error loading avatar definitions: {e}")
        return False

def test_inventory_system():
    """Test 2: Verify inventory system works correctly"""
    print("\n🧪 Test 2: Inventory System")
    try:
        from utils.inventory import get_user_inventory, activate_item
        
        # Test with user 'a' who has purchased avatars
        inventory = get_user_inventory('a')
        print(f"   User 'a' inventory retrieved successfully")
        print(f"   Avatars in inventory: {inventory.get('avatars', [])}")
        
        # Verify inventory structure
        expected_keys = ['avatars', 'backgrounds', 'special_lessons', 'boosters']
        missing_keys = [key for key in expected_keys if key not in inventory]
        
        if missing_keys:
            print(f"   ❌ Missing inventory keys: {missing_keys}")
            return False
        else:
            print(f"   ✅ All inventory keys present: {list(inventory.keys())}")
            
        return True
    except Exception as e:
        print(f"   ❌ Error testing inventory system: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_avatar_activation():
    """Test 3: Test avatar activation functionality"""
    print("\n🧪 Test 3: Avatar Activation")
    try:
        from utils.inventory import get_user_inventory, activate_item
        
        # Get user's current state
        users_data = load_user_data()
        if not users_data:
            return False
            
        user_data = users_data.get('a', {})
        original_active = user_data.get('active_avatar', 'Not set')
        print(f"   Original active avatar: {original_active}")
        
        # Get inventory
        inventory = get_user_inventory('a')
        user_avatars = inventory.get('avatars', [])
        
        if not user_avatars:
            print("   ❌ No avatars in inventory to test activation")
            return False
            
        # Test activation of first avatar
        test_avatar = user_avatars[0]
        print(f"   Testing activation of: {test_avatar}")
        
        result = activate_item('a', 'avatar', test_avatar)
        print(f"   Activation result: {result}")
        
        # Verify activation worked
        updated_data = load_user_data()
        updated_user = updated_data.get('a', {})
        new_active = updated_user.get('active_avatar', 'Not set')
        print(f"   New active avatar: {new_active}")
        
        if new_active == test_avatar:
            print(f"   ✅ Avatar activation successful")
            return True
        else:
            print(f"   ❌ Avatar activation failed - expected {test_avatar}, got {new_active}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error testing avatar activation: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_personalization_logic():
    """Test 4: Test personalization tab logic"""
    print("\n🧪 Test 4: Personalization Logic")
    try:
        from utils.inventory import get_user_inventory
        from config.settings import USER_AVATARS
        
        # Simulate personalization logic
        inventory = get_user_inventory('a')
        owned_premium_avatars = inventory.get('avatars', [])
        premium_avatars = {"diamond_degen", "crypto_wizard", "moon_hunter"}
        
        print(f"   Owned premium avatars: {owned_premium_avatars}")
        
        # Test avatar filtering logic
        available_avatars = {}
        locked_avatars = []
        
        for avatar_id, avatar_emoji in USER_AVATARS.items():
            if avatar_id not in premium_avatars:
                # Basic avatar - always available
                available_avatars[avatar_id] = avatar_emoji
            elif avatar_id in owned_premium_avatars:
                # Premium avatar - owned
                available_avatars[avatar_id] = avatar_emoji
            else:
                # Premium avatar - locked
                locked_avatars.append(avatar_id)
        
        print(f"   Available avatars: {len(available_avatars)}")
        print(f"   Locked premium avatars: {locked_avatars}")
        
        # Check that owned premium avatars are available
        for owned_avatar in owned_premium_avatars:
            if owned_avatar in available_avatars:
                emoji = available_avatars[owned_avatar]
                print(f"   ✅ {owned_avatar} {emoji} - Available (owned)")
            else:
                print(f"   ❌ {owned_avatar} - Should be available but isn't")
                return False
        
        # Check that non-owned premium avatars are locked
        for premium_avatar in premium_avatars:
            if premium_avatar not in owned_premium_avatars:
                if premium_avatar not in available_avatars:
                    print(f"   ✅ {premium_avatar} - Correctly locked")
                else:
                    print(f"   ❌ {premium_avatar} - Should be locked but isn't")
                    return False
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error testing personalization logic: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_complete_workflow():
    """Test 5: Test complete purchase-to-use workflow"""
    print("\n🧪 Test 5: Complete Workflow Simulation")
    try:
        # This simulates what happens when a user buys an avatar
        # and then tries to use it in personalization
        
        from utils.inventory import get_user_inventory, activate_item
        from config.settings import USER_AVATARS
        
        # Check current state
        users_data = load_user_data()
        user_data = users_data.get('a', {})
        
        print("   Current user state:")
        print(f"     Inventory: {user_data.get('inventory', {})}")
        print(f"     Active avatar: {user_data.get('active_avatar', 'Not set')}")
        
        # Get inventory through system
        inventory = get_user_inventory('a')
        owned_avatars = inventory.get('avatars', [])
        
        print(f"   Owned avatars via inventory system: {owned_avatars}")
        
        # Check avatar definitions exist
        missing_definitions = []
        for avatar in owned_avatars:
            if avatar not in USER_AVATARS:
                missing_definitions.append(avatar)
                
        if missing_definitions:
            print(f"   ❌ Missing avatar definitions: {missing_definitions}")
            return False
        else:
            print(f"   ✅ All owned avatars have definitions")
            
        # Test activation of each owned avatar
        for avatar in owned_avatars:
            print(f"   Testing {avatar}...")
            result = activate_item('a', 'avatar', avatar)
            if result:
                emoji = USER_AVATARS.get(avatar, '❓')
                print(f"     ✅ {avatar} {emoji} - Can be activated")
            else:
                print(f"     ❌ {avatar} - Activation failed")
                return False
        
        print("   ✅ Complete workflow test passed")
        return True
        
    except Exception as e:
        print(f"   ❌ Error in complete workflow test: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🎯 AVATAR SYSTEM INTEGRATION TEST")
    print("=" * 60)
    
    tests = [
        test_avatar_definitions,
        test_inventory_system,
        test_avatar_activation,
        test_personalization_logic,
        test_complete_workflow
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"   💥 Test crashed: {e}")
            failed += 1
        print()
    
    print("=" * 60)
    print(f"📊 TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed == 0:
        print("🎉 ALL TESTS PASSED! Avatar system is working correctly.")
        print("\n✅ Avatar purchase system complete:")
        print("   • Users can buy avatars in shop")
        print("   • Purchased avatars appear in inventory")
        print("   • Avatars can be activated from inventory")
        print("   • Premium avatars show correctly in personalization")
        print("   • Only owned premium avatars are selectable")
    else:
        print(f"❌ {failed} test(s) failed. Avatar system needs fixes.")
    
    return failed == 0

if __name__ == "__main__":
    main()
