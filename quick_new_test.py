# quick_new_test.py - Test nowej aplikacji
print("🚀 Test Nowej Aplikacji ZenDegenAcademy")
print("=" * 50)

# Test basic imports
try:
    import streamlit as st
    print("✅ Streamlit - OK")
except Exception as e:
    print(f"❌ Streamlit - ERROR: {e}")

import os
APP_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"✅ App directory: {APP_DIR}")

# Test navigation
try:
    from utils.new_navigation import NewNavigationSystem
    nav = NewNavigationSystem()
    print(f"✅ Navigation system - {len(nav.sections)} sekcji")
    for key, section in nav.sections.items():
        print(f"   - {key}: {section['label']} ({len(section['subsections'])} podsekcji)")
except Exception as e:
    print(f"❌ Navigation system - ERROR: {e}")

# Test missions  
try:
    from utils.daily_missions import ENHANCED_MISSIONS_POOL
    total = sum(len(missions) for missions in ENHANCED_MISSIONS_POOL.values())
    print(f"✅ Daily missions - {total} misji w {len(ENHANCED_MISSIONS_POOL)} kategoriach")
    for category, missions in ENHANCED_MISSIONS_POOL.items():
        print(f"   - {category}: {len(missions)} misji")
except Exception as e:
    print(f"❌ Daily missions - ERROR: {e}")

# Test lesson structure
try:
    from utils.lesson_structure_new import LessonStructureNew
    lesson = LessonStructureNew()
    print(f"✅ Lesson structure - {len(lesson.stages)} etapów")
    for i, stage in enumerate(lesson.stages, 1):
        print(f"   {i}. {stage['name']} ({stage['type']})")
except Exception as e:
    print(f"❌ Lesson structure - ERROR: {e}")

print("=" * 50)
print("🎯 Test zakończony! Gotowe do uruchomienia:")
print("   streamlit run main_new.py")
