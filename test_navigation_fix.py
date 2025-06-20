#!/usr/bin/env python3
"""
Test script to verify navigation fixes
"""

import sys
import os

# Add the app directory to path
app_dir = os.path.dirname(os.path.abspath(__file__))
if app_dir not in sys.path:
    sys.path.append(app_dir)

def test_imports():
    """Test if all critical imports work"""
    print("🔍 Testing imports...")
    
    # Test main navigation import
    try:
        from utils.new_navigation import NewNavigationSystem
        print("✅ NewNavigationSystem import successful")
    except Exception as e:
        print(f"❌ NewNavigationSystem import failed: {e}")
        return False
    
    # Test learn view import
    try:
        from views.learn import show_learn
        print("✅ show_learn import successful")
    except Exception as e:
        print(f"❌ show_learn import failed: {e}")
        return False
    
    # Test skills integration
    try:
        from views.learn import show_skills_in_lessons_tab
        print("✅ show_skills_in_lessons_tab import successful")
    except Exception as e:
        print(f"❌ show_skills_in_lessons_tab import failed: {e}")
        return False
    
    return True

def test_navigation_system():
    """Test if navigation system can be initialized"""
    print("\n🔍 Testing navigation system...")
    
    try:
        from utils.new_navigation import NewNavigationSystem
        nav_system = NewNavigationSystem()
        
        # Check if sections are properly defined
        if 'learn' in nav_system.sections:
            learn_section = nav_system.sections['learn']
            print(f"✅ Learn section found: {learn_section['label']}")
            print(f"   Icon: {learn_section['icon']}")
            print(f"   Description: {learn_section['description']}")
            return True
        else:
            print("❌ Learn section not found in navigation")
            return False
            
    except Exception as e:
        print(f"❌ Navigation system test failed: {e}")
        return False

def test_learn_view():
    """Test if learn view can be called"""
    print("\n🔍 Testing learn view...")
    
    try:
        from views.learn import show_learn
        # We can't actually call show_learn without streamlit context,
        # but we can check if the function exists
        print("✅ show_learn function is callable")
        return True
    except Exception as e:
        print(f"❌ Learn view test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting navigation fix verification...\n")
    
    tests = [
        ("Import Tests", test_imports),
        ("Navigation System", test_navigation_system),
        ("Learn View", test_learn_view)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"{'='*50}")
        print(f"Running: {test_name}")
        print(f"{'='*50}")
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} FAILED with exception: {e}")
        
        print()
    
    print(f"{'='*50}")
    print(f"RESULTS: {passed}/{total} tests passed")
    print(f"{'='*50}")
    
    if passed == total:
        print("🎉 All tests passed! Navigation should work correctly.")
        print("\n📋 Next steps:")
        print("1. Run: streamlit run main_new.py")
        print("2. Login to the application")
        print("3. Check if 'NAUKA' section appears in the sidebar")
        print("4. Click on 'NAUKA' to test the integrated skills functionality")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
