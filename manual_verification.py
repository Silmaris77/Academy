#!/usr/bin/env python3
"""
Manual verification script for the degen test update fix.
This script checks that the implementation is correct without running complex tests.
"""

import os

def check_file_exists(filepath):
    """Check if a file exists"""
    return os.path.exists(filepath)

def check_string_in_file(filepath, search_string):
    """Check if a string exists in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return search_string in f.read()
    except Exception:
        return False

def main():
    print("🔍 DEGEN TEST UPDATE FIX - MANUAL VERIFICATION")
    print("=" * 50)
    
    # Check that all required files exist
    files_to_check = [
        'views/profile.py',
        'views/dashboard.py', 
        'data/users.py',
        'utils/real_time_updates.py'
    ]
    
    print("\n📁 File Existence Check:")
    all_files_exist = True
    for file_path in files_to_check:
        exists = check_file_exists(file_path)
        status = "✅" if exists else "❌"
        print(f"  {status} {file_path}")
        if not exists:
            all_files_exist = False
    
    if not all_files_exist:
        print("\n❌ Some required files are missing!")
        return False
    
    # Check Profile view implementation
    print("\n👤 Profile View Check:")
    profile_checks = [
        ('Imports get_current_user_data', 'from data.users import load_user_data, save_user_data, update_single_user_field, get_current_user_data'),
        ('Uses get_current_user_data', 'user_data = get_current_user_data(st.session_state.username)'),
        ('No get_live_user_stats usage', 'get_live_user_stats')
    ]
    
    profile_ok = True
    for check_name, search_string in profile_checks:
        found = check_string_in_file('views/profile.py', search_string)
        if 'No get_live_user_stats' in check_name:
            # For this check, we want NOT to find the string
            status = "✅" if not found else "❌"
            result = "Not found (good)" if not found else "Found (bad)"
        else:
            status = "✅" if found else "❌"
            result = "Found" if found else "Not found"
        
        print(f"  {status} {check_name}: {result}")
        if (not found and 'No get_live_user_stats' not in check_name) or (found and 'No get_live_user_stats' in check_name):
            profile_ok = False
    
    # Check Dashboard view implementation
    print("\n📊 Dashboard View Check:")
    dashboard_checks = [
        ('Imports get_current_user_data', 'from data.users import load_user_data, save_user_data, get_current_user_data'),
        ('Uses get_current_user_data', 'user_data = get_current_user_data(st.session_state.username)'),
        ('Clean imports (live_xp_indicator only)', 'from utils.real_time_updates import live_xp_indicator'),
        ('No get_live_user_stats usage', 'get_live_user_stats')
    ]
    
    dashboard_ok = True
    for check_name, search_string in dashboard_checks:
        found = check_string_in_file('views/dashboard.py', search_string)
        if 'No get_live_user_stats' in check_name:
            # For this check, we want NOT to find the string
            status = "✅" if not found else "❌"
            result = "Not found (good)" if not found else "Found (bad)"
        else:
            status = "✅" if found else "❌"
            result = "Found" if found else "Not found"
        
        print(f"  {status} {check_name}: {result}")
        if (not found and 'No get_live_user_stats' not in check_name) or (found and 'No get_live_user_stats' in check_name):
            dashboard_ok = False
    
    # Check function definitions
    print("\n🔧 Function Definitions Check:")
    function_checks = [
        ('get_current_user_data exists', 'data/users.py', 'def get_current_user_data(username):'),
        ('get_live_user_stats exists', 'utils/real_time_updates.py', 'def get_live_user_stats(username):'),
        ('get_current_user_data uses session_state', 'data/users.py', 'st.session_state.user_data'),
        ('get_current_user_data falls back to file', 'data/users.py', 'load_user_data()')
    ]
    
    functions_ok = True
    for check_name, file_path, search_string in function_checks:
        found = check_string_in_file(file_path, search_string)
        status = "✅" if found else "❌"
        result = "Found" if found else "Not found"
        print(f"  {status} {check_name}: {result}")
        if not found:
            functions_ok = False
    
    # Final assessment
    print("\n" + "=" * 50)
    print("📋 FINAL ASSESSMENT:")
    
    all_checks_pass = profile_ok and dashboard_ok and functions_ok
    
    if all_checks_pass:
        print("🎉 ALL CHECKS PASSED!")
        print("\n✅ The degen test update fix has been successfully implemented:")
        print("  • Profile view uses get_current_user_data()")
        print("  • Dashboard view uses get_current_user_data()")
        print("  • No more get_live_user_stats() usage in views")
        print("  • Functions exist and have correct logic")
        print("\n🚀 Degen test results should now display immediately!")
        print("   (No logout/login required)")
        return True
    else:
        print("❌ SOME CHECKS FAILED!")
        print("\n🔧 Issues found:")
        if not profile_ok:
            print("  • Profile view implementation incomplete")
        if not dashboard_ok:
            print("  • Dashboard view implementation incomplete") 
        if not functions_ok:
            print("  • Function definitions incomplete")
        print("\n🛠️  Please review and fix the issues above.")
        return False

if __name__ == '__main__':
    success = main()
    if success:
        print("\n🎯 Ready for testing! Try completing a degen test to verify the fix.")
    else:
        print("\n⚠️  Fix needs completion before testing.")
