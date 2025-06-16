#!/usr/bin/env python3
"""
Validation script for the new ZenDegenAcademy application
Tests all major components and imports
"""

def test_imports():
    """Test all critical imports"""
    print("🔍 Testing imports...")
    
    try:
        # Test main application
        import main_new
        print("✅ main_new.py imported successfully")
        
        # Test new navigation system
        from utils.new_navigation import NewNavigationSystem
        print("✅ NewNavigationSystem imported successfully")
        
        # Test enhanced lesson structure
        from utils.lesson_structure_new import LessonStructureNew
        print("✅ LessonStructureNew imported successfully")
        
        # Test fixed mission components
        from utils.mission_components_fixed import render_missions_page, mission_manager
        print("✅ Fixed mission components imported successfully")
        
        # Test daily missions
        from utils.daily_missions import DailyMissionManager
        print("✅ DailyMissionManager imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_components():
    """Test component initialization"""
    print("\n🔧 Testing component initialization...")
    
    try:
        # Test navigation system
        from utils.new_navigation import NewNavigationSystem
        nav = NewNavigationSystem()
        print("✅ Navigation system initialized")
        
        # Test lesson structure
        from utils.lesson_structure_new import LessonStructureNew
        lesson = LessonStructureNew()
        print("✅ Lesson structure initialized")
        
        # Test daily missions
        from utils.daily_missions import DailyMissionManager
        mission_mgr = DailyMissionManager()
        print("✅ Daily mission manager initialized")
        
        return True
        
    except Exception as e:
        print(f"❌ Component initialization error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_navigation_sections():
    """Test navigation sections"""
    print("\n📋 Testing navigation sections...")
    
    try:
        from utils.new_navigation import NewNavigationSystem
        nav = NewNavigationSystem()
        
        sections = nav.get_navigation_sections()
        expected_sections = ['START', 'NAUKA', 'PRAKTYKA', 'PROFIL']
        
        for section in expected_sections:
            if section in sections:
                print(f"✅ Section '{section}' found")
            else:
                print(f"❌ Section '{section}' missing")
                return False
                
        print(f"✅ All {len(expected_sections)} navigation sections available")
        return True
        
    except Exception as e:
        print(f"❌ Navigation test error: {e}")
        return False

def test_lesson_stages():
    """Test lesson structure stages"""
    print("\n📚 Testing lesson stages...")
    
    try:
        from utils.lesson_structure_new import LessonStructureNew
        lesson = LessonStructureNew()
        
        stages = lesson.get_lesson_stages()
        expected_stages = ['introduction', 'opening_case', 'quiz', 'content', 'closing_case', 'summary']
        
        for stage in expected_stages:
            if stage in stages:
                print(f"✅ Stage '{stage}' found")
            else:
                print(f"❌ Stage '{stage}' missing")
                return False
                
        print(f"✅ All {len(expected_stages)} lesson stages available")
        return True
        
    except Exception as e:
        print(f"❌ Lesson stages test error: {e}")
        return False

def main():
    """Run all validation tests"""
    print("🚀 ZenDegenAcademy New Application Validation")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_components,
        test_navigation_sections,
        test_lesson_stages
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The new application is ready to use.")
        print("\n🚀 To start the application, run:")
        print("   streamlit run main_new.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    main()
