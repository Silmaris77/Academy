#!/usr/bin/env python3
"""
Quick test to verify the shop buy_item function fix
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.getcwd())

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
