#!/usr/bin/env python3
"""
Simple test runner for the new ZenDegenAcademy application
"""

import sys
import os
import traceback

# Add current directory to Python path
sys.path.insert(0, os.getcwd())

def test_imports():
    """Test all critical imports step by step"""
    print("🔍 Testing imports step by step...")
    
    # Test 1: Basic imports
    try:
        import streamlit as st
        print("✅ Streamlit import OK")
    except Exception as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    # Test 2: Config
    try:
        from config.settings import PAGE_CONFIG
        print("✅ Config import OK")
    except Exception as e:
        print(f"❌ Config import failed: {e}")
        return False
    
    # Test 3: Utils
    try:
        from utils.session import init_session_state, clear_session
        print("✅ Session utils import OK")
    except Exception as e:
        print(f"❌ Session utils import failed: {e}")
        return False
    
    # Test 4: New navigation
    try:
        from utils.new_navigation import initialize_new_navigation
        print("✅ New navigation import OK")
    except Exception as e:
        print(f"❌ New navigation import failed: {e}")
        return False
    
    # Test 5: Views
    try:
        from views.login import show_login_page
        print("✅ Login view import OK")
    except Exception as e:
        print(f"❌ Login view import failed: {e}")
        return False
    
    # Test 6: Dashboard
    try:
        from views.dashboard import show_dashboard
        print("✅ Dashboard view import OK")  
    except Exception as e:
        print(f"❌ Dashboard view import failed: {e}")
        return False
    
    # Test 7: Implementation
    try:
        from views.implementation import show_implementation
        print("✅ Implementation view import OK")
    except Exception as e:
        print(f"❌ Implementation view import failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False
    
    # Test 8: Main application
    try:
        import main_new
        print("✅ main_new.py import OK")
    except Exception as e:
        print(f"❌ main_new.py import failed: {e}")
        print(f"Error details: {traceback.format_exc()}")
        return False
    
    return True

def main():
    """Run the test"""
    print("🧪 ZenDegenAcademy New App - Import Test")
    print("=" * 50)
    
    if test_imports():
        print("\n🎉 All imports successful!")
        print("✅ Application is ready to run")
        print("\n🚀 To start the app, run:")
        print("   streamlit run main_new.py")
    else:
        print("\n❌ Some imports failed")
        print("Please check the errors above")

if __name__ == "__main__":
    main()
