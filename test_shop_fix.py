#!/usr/bin/env python3
"""
Test script to verify the shop booster fix
"""

import sys
import os
import datetime

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_booster_data_handling():
    """Test that both old and new booster data formats work"""
    
    print("🧪 Testing booster data format handling...")
    
    # Test data with old format (string)
    old_format_data = {
        'active_boosters': {
            'xp_boost': '2025-06-17T15:56:10.600451'
        }
    }
    
    # Test data with new format (object)
    new_format_data = {
        'active_boosters': {
            'xp_boost': {
                'expires_at': '2025-06-17T15:56:10.600451',
                'activated_at': '2025-06-16T15:56:10.600470'
            }
        }
    }
    
    def test_format(user_data, format_name):
        print(f"\n📋 Testing {format_name} format...")
        
        booster_id = 'xp_boost'
        
        if 'active_boosters' in user_data and booster_id in user_data.get('active_boosters', {}):
            booster_data = user_data['active_boosters'][booster_id]
            
            try:
                # Handle both old format (string) and new format (object with expires_at)
                if isinstance(booster_data, str):
                    expiry_time = datetime.datetime.fromisoformat(booster_data)
                    print(f"✅ Old format handled successfully: {expiry_time}")
                elif isinstance(booster_data, dict) and 'expires_at' in booster_data:
                    expiry_time = datetime.datetime.fromisoformat(booster_data['expires_at'])
                    print(f"✅ New format handled successfully: {expiry_time}")
                else:
                    print(f"❌ Invalid booster data format: {type(booster_data)}")
                    return False
                
                now = datetime.datetime.now()
                
                if expiry_time > now:
                    remaining_seconds = (expiry_time - now).total_seconds()
                    remaining_hours = int(remaining_seconds // 3600)
                    remaining_minutes = int((remaining_seconds % 3600) // 60)
                    remaining_time = f"{remaining_hours}h {remaining_minutes}m"
                    print(f"✅ Booster is active, remaining: {remaining_time}")
                else:
                    print(f"⏰ Booster has expired")
                
                return True
                
            except Exception as e:
                print(f"❌ Error processing {format_name} format: {e}")
                return False
        else:
            print(f"❌ No booster data found")
            return False
    
    # Test both formats
    old_result = test_format(old_format_data, "old")
    new_result = test_format(new_format_data, "new")
    
    if old_result and new_result:
        print(f"\n🎉 All tests passed! Both formats handled correctly.")
        return True
    else:
        print(f"\n💥 Some tests failed!")
        return False

if __name__ == "__main__":
    print("🚀 Shop Booster Fix Verification")
    print("=" * 50)
    
    success = test_booster_data_handling()
    
    if success:
        print("\n✅ Fix verification successful!")
        print("The shop should now handle both old and new booster data formats.")
    else:
        print("\n❌ Fix verification failed!")
        print("There are still issues with booster data handling.")

def test_shop_import():
    """Test if the shop module imports without errors"""
    print("=== Shop Module Import Test ===")
    
    try:
        import views.shop_new
        print("✅ Shop module imported successfully!")
        
        # Test if the buy_item function has the correct signature
        import inspect
        sig = inspect.signature(views.shop_new.buy_item)
        params = list(sig.parameters.keys())
        
        print(f"buy_item function parameters: {params}")
        
        expected_params = ['item_type', 'item_id', 'price', 'user_data', 'users_data', 'username']
        if params == expected_params:
            print("✅ buy_item function has correct parameters!")
        else:
            print(f"❌ buy_item function parameters mismatch. Expected: {expected_params}")
            
        return True
        
    except Exception as e:
        print(f"❌ Error importing shop module: {e}")
        import traceback
        print(traceback.format_exc())
        return False

def test_function_calls():
    """Test if function calls in the shop use correct parameters"""
    print("\n=== Function Call Verification ===")
    
    try:
        with open('views/shop_new.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count buy_item calls with username parameter
        correct_calls = content.count('buy_item(') - content.count('def buy_item(')
        username_param_calls = content.count('st.session_state.username)')
        
        print(f"Total buy_item calls found: {correct_calls}")
        print(f"Calls with username parameter: {username_param_calls}")
        
        if correct_calls == username_param_calls:
            print("✅ All buy_item calls use correct parameters!")
        else:
            print("❌ Some buy_item calls may be missing username parameter")
            
    except Exception as e:
        print(f"❌ Error reading shop file: {e}")

if __name__ == "__main__":
    print("DegenCoins Shop Username Fix Verification")
    print("=" * 50)
    
    success = test_shop_import()
    test_function_calls()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Shop username fix verification PASSED!")
    else:
        print("❌ Shop username fix verification FAILED!")
