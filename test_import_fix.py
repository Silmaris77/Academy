#!/usr/bin/env python3
"""
Test script to validate the mission components fix
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.getcwd())

def test_mission_components():
    """Test mission components imports"""
    print("🔧 Testing mission components...")
    
    try:
        from utils.mission_components_clean import render_missions_page, mission_manager
        print("✅ Clean mission components imported successfully")
        
        # Test mission manager
        missions = mission_manager.get_available_missions("test_user", "B1C1L1")
        print(f"✅ Mission manager working - found {len(missions)} missions")
        
        return True
    except Exception as e:
        print(f"❌ Mission components error: {e}")
        return False

def test_implementation_view():
    """Test implementation view imports"""
    print("\n📄 Testing implementation view...")
    
    try:
        from views.implementation import show_implementation
        print("✅ Implementation view imported successfully")
        return True
    except Exception as e:
        print(f"❌ Implementation view error: {e}")
        return False

def test_main_app():
    """Test main application"""
    print("\n🚀 Testing main application...")
    
    try:
        import main_new
        print("✅ main_new.py imported successfully")
        return True
    except Exception as e:
        print(f"❌ Main application error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("🧪 ZenDegenAcademy Import Fix Validation")
    print("=" * 50)
    
    tests = [
        test_mission_components,
        test_implementation_view,
        test_main_app
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! Import issue fixed!")
        print("\n🚀 Ready to run: streamlit run main_new.py")
    else:
        print("⚠️ Some tests failed. Check errors above.")
    
    return passed == len(tests)

if __name__ == "__main__":
    main()
