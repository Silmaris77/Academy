#!/usr/bin/env python3
"""
Quick test for main_new.py functionality
"""

import sys
import os

# Add the app directory to path
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_dir)

def test_main_imports():
    """Test if main_new.py can be imported without errors"""
    print("🔍 Testing main_new.py imports...")
    
    try:
        import main_new
        print("✅ main_new.py imported successfully")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_navigation_integration():
    """Test if navigation integration works"""
    print("\n🔍 Testing navigation integration...")
    
    try:
        from utils.new_navigation import NewNavigationSystem, initialize_new_navigation
        nav_system = initialize_new_navigation()
        
        if hasattr(nav_system, 'render_sidebar_navigation'):
            print("✅ Navigation system has render_sidebar_navigation method")
        
        if hasattr(nav_system, '_render_learn_section'):
            print("✅ Navigation system has _render_learn_section method")
        
        if 'learn' in nav_system.sections:
            print("✅ 'learn' section found in navigation")
            return True
        else:
            print("❌ 'learn' section not found")
            return False
            
    except Exception as e:
        print(f"❌ Navigation test failed: {e}")
        return False

def test_learn_view():
    """Test if learn view with skills integration works"""
    print("\n🔍 Testing learn view integration...")
    
    try:
        from views.learn import show_learn, show_skills_in_lessons_tab
        print("✅ Learn view with skills integration imported successfully")
        return True
    except Exception as e:
        print(f"❌ Learn view test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Testing main_new.py and NAUKA section integration...\n")
    
    tests = [
        ("Main Import", test_main_imports),
        ("Navigation Integration", test_navigation_integration),
        ("Learn View Integration", test_learn_view)
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
        print("🎉 All tests passed! Application should work correctly.")
        print("\n📋 Next steps:")
        print("1. Run: streamlit run main_new.py")
        print("2. Login to the application")
        print("3. Check if 'NAUKA' section appears in the sidebar")
        print("4. Test the integrated skills functionality")
        print("\n🎯 Expected behavior:")
        print("- Sidebar should show: START, NAUKA, PRAKTYKA, PROFIL")
        print("- NAUKA section should contain integrated skills in tabs")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
