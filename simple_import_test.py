#!/usr/bin/env python3
"""
Simple import test for navigation fixes
"""

import sys
import os

# Add the app directory to path
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_dir)

print("🔍 Testing navigation system imports...")

# Test 1: Basic navigation import
try:
    from utils.new_navigation import NewNavigationSystem
    print("✅ NewNavigationSystem imported successfully")
    nav = NewNavigationSystem()
    if 'learn' in nav.sections:
        print("✅ 'learn' section found in navigation")
        learn_section = nav.sections['learn']
        print(f"   - Label: {learn_section['label']}")
        print(f"   - Icon: {learn_section['icon']}")
        print(f"   - Description: {learn_section['description']}")
    else:
        print("❌ 'learn' section NOT found in navigation")
except Exception as e:
    print(f"❌ Navigation import failed: {e}")

# Test 2: Learn view import
try:
    from views.learn import show_learn
    print("✅ show_learn imported successfully")
except Exception as e:
    print(f"❌ show_learn import failed: {e}")

# Test 3: Skills integration import
try:
    from views.learn import show_skills_in_lessons_tab
    print("✅ show_skills_in_lessons_tab imported successfully")
except Exception as e:
    print(f"❌ show_skills_in_lessons_tab import failed: {e}")

# Test 4: Check if main_new.py can import all needed components
try:
    from utils.session import init_session_state, clear_session
    print("✅ Session utilities imported successfully")
except Exception as e:
    print(f"❌ Session utilities import failed: {e}")

try:
    from utils.new_navigation import initialize_new_navigation
    print("✅ initialize_new_navigation imported successfully")
except Exception as e:
    print(f"❌ initialize_new_navigation import failed: {e}")

print("\n🎯 Summary:")
print("If all tests passed, the navigation should work correctly.")
print("Next steps:")
print("1. Run: streamlit run main_new.py")
print("2. Login to the application")
print("3. Look for 'NAUKA' button in the sidebar")
print("4. Click 'NAUKA' to see integrated skills functionality")
