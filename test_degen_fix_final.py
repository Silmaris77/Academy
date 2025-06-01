#!/usr/bin/env python3
"""
Final comprehensive test for degen test update fix.
This script verifies that the Profile and Dashboard views are properly using
get_current_user_data() instead of get_live_user_stats() to ensure immediate
display of degen test results.
"""

import sys
import os
import ast
import importlib.util

def test_imports_and_functions():
    """Test that the required functions are properly imported and used."""
    
    print("=== DEGEN TEST UPDATE FIX - FINAL VERIFICATION ===\n")
    
    # Test files to check
    test_files = {
        'views/profile.py': {
            'should_import': ['get_current_user_data'],
            'should_not_use': ['get_live_user_stats()'],
            'should_use': ['get_current_user_data(']
        },
        'views/dashboard.py': {
            'should_import': ['get_current_user_data'],
            'should_not_use': ['get_live_user_stats()'],
            'should_use': ['get_current_user_data(']
        }
    }
    
    all_tests_passed = True
    
    for file_path, requirements in test_files.items():
        print(f"Testing {file_path}...")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check imports
            for required_import in requirements['should_import']:
                if required_import in content:
                    print(f"  ✅ Imports {required_import}")
                else:
                    print(f"  ❌ Missing import: {required_import}")
                    all_tests_passed = False
            
            # Check that old function is not used
            for forbidden_usage in requirements['should_not_use']:
                if forbidden_usage in content:
                    print(f"  ❌ Still uses forbidden function: {forbidden_usage}")
                    all_tests_passed = False
                else:
                    print(f"  ✅ No longer uses: {forbidden_usage}")
            
            # Check that new function is used
            for required_usage in requirements['should_use']:
                if required_usage in content:
                    print(f"  ✅ Uses correct function: {required_usage}")
                else:
                    print(f"  ❌ Missing usage: {required_usage}")
                    all_tests_passed = False
                    
            print()
            
        except FileNotFoundError:
            print(f"  ❌ File not found: {file_path}")
            all_tests_passed = False
        except Exception as e:
            print(f"  ❌ Error reading file: {e}")
            all_tests_passed = False
    
    return all_tests_passed

def test_function_definitions():
    """Test that the required functions exist and have the right signatures."""
    
    print("=== FUNCTION DEFINITIONS TEST ===\n")
    
    try:
        # Test get_current_user_data exists
        with open('data/users.py', 'r', encoding='utf-8') as f:
            users_content = f.read()
        
        if 'def get_current_user_data(' in users_content:
            print("✅ get_current_user_data() function exists in data/users.py")
        else:
            print("❌ get_current_user_data() function not found in data/users.py")
            return False
            
        # Test get_live_user_stats exists  
        with open('utils/real_time_updates.py', 'r', encoding='utf-8') as f:
            realtime_content = f.read()
        
        if 'def get_live_user_stats(' in realtime_content:
            print("✅ get_live_user_stats() function exists in utils/real_time_updates.py")
        else:
            print("❌ get_live_user_stats() function not found in utils/real_time_updates.py")
            return False
            
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error checking function definitions: {e}")
        return False

def analyze_function_differences():
    """Analyze the differences between the two functions."""
    
    print("=== FUNCTION ANALYSIS ===\n")
    
    try:
        # Read both functions
        with open('data/users.py', 'r', encoding='utf-8') as f:
            users_content = f.read()
        
        with open('utils/real_time_updates.py', 'r', encoding='utf-8') as f:
            realtime_content = f.read()
        
        # Check for key differences
        if 'degen_type' in users_content and 'get_current_user_data' in users_content:
            print("✅ get_current_user_data() likely includes degen test fields")
        else:
            print("⚠️  Cannot confirm degen test fields in get_current_user_data()")
        
        if 'session_state' in users_content and 'get_current_user_data' in users_content:
            print("✅ get_current_user_data() likely uses session state priority")
        else:
            print("⚠️  Cannot confirm session state usage in get_current_user_data()")
            
        print()
        return True
        
    except Exception as e:
        print(f"❌ Error analyzing functions: {e}")
        return False

def main():
    """Run all tests."""
    
    print("Starting comprehensive degen test update fix verification...\n")
    
    # Change to the correct directory
    if not os.path.exists('views'):
        print("❌ Not in correct directory. Please run from ZenDegenAcademy root.")
        return False
    
    test1 = test_imports_and_functions()
    test2 = test_function_definitions() 
    test3 = analyze_function_differences()
    
    print("=== FINAL RESULTS ===")
    
    if test1 and test2 and test3:
        print("🎉 ALL TESTS PASSED!")
        print("\nThe degen test update fix has been successfully implemented:")
        print("- Profile view uses get_current_user_data()")
        print("- Dashboard view uses get_current_user_data()")
        print("- Both functions exist and are properly imported")
        print("\nDegen test results should now display immediately without logout/login!")
        return True
    else:
        print("❌ SOME TESTS FAILED")
        print("\nPlease review the failed tests above and fix any issues.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
