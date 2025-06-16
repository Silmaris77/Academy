# test_new_app.py - Test nowej aplikacji
"""
Test script dla nowej wersji aplikacji opartej na prototypie HTML
"""

import sys 
import os

# Add app directory to path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.append(APP_DIR)

def test_imports():
    """Test wszystkich importów"""
    print("🧪 Testowanie importów...")
    
    try:
        from utils.new_navigation import NewNavigationSystem, initialize_new_navigation
        print("✅ utils.new_navigation - OK")
    except Exception as e:
        print(f"❌ utils.new_navigation - ERROR: {e}")
    
    try:
        from utils.daily_missions import get_daily_missions_status, render_missions_widget
        print("✅ utils.daily_missions - OK")
    except Exception as e:
        print(f"❌ utils.daily_missions - ERROR: {e}")
    
    try:
        from utils.lesson_structure_new import LessonStructureNew, get_lesson_structure
        print("✅ utils.lesson_structure_new - OK")
    except Exception as e:
        print(f"❌ utils.lesson_structure_new - ERROR: {e}")
    
    try:
        from data.users import load_user_data, save_user_data, award_badge
        print("✅ data.users - OK")
    except Exception as e:
        print(f"❌ data.users - ERROR: {e}")

def test_navigation_system():
    """Test systemu nawigacji"""
    print("\n🧪 Testowanie systemu nawigacji...")
    
    try:
        from utils.new_navigation import NewNavigationSystem
        nav = NewNavigationSystem()
        
        # Test sekcji
        sections = nav.sections
        print(f"✅ Załadowano {len(sections)} sekcji: {list(sections.keys())}")
        
        # Test tytułów
        for section_key in sections:
            title = nav.get_section_title(section_key)
            print(f"  - {section_key}: {title}")
        
        print("✅ System nawigacji - OK")
        
    except Exception as e:
        print(f"❌ System nawigacji - ERROR: {e}")

def test_daily_missions():
    """Test systemu misji"""
    print("\n🧪 Testowanie systemu misji...")
    
    try:
        from utils.daily_missions import ENHANCED_MISSIONS_POOL, DEGEN_MISSION_PREFERENCES
        
        # Count missions
        total_missions = sum(len(missions) for missions in ENHANCED_MISSIONS_POOL.values())
        print(f"✅ Załadowano {total_missions} misji w {len(ENHANCED_MISSIONS_POOL)} kategoriach")
        
        for category, missions in ENHANCED_MISSIONS_POOL.items():
            print(f"  - {category}: {len(missions)} misji")
        
        # Test degen preferences
        print(f"✅ Preferencje dla {len(DEGEN_MISSION_PREFERENCES)} typów degenów")
        
        print("✅ System misji - OK")
        
    except Exception as e:
        print(f"❌ System misji - ERROR: {e}")

def test_lesson_structure():
    """Test struktury lekcji"""
    print("\n🧪 Testowanie struktury lekcji...")
    
    try:
        from utils.lesson_structure_new import LessonStructureNew
        lesson_structure = LessonStructureNew()
        
        stages = lesson_structure.stages
        print(f"✅ Załadowano {len(stages)} etapów lekcji:")
        
        for i, stage in enumerate(stages):
            print(f"  {i+1}. {stage['name']} ({stage['type']})")
        
        print("✅ Struktura lekcji - OK")
        
    except Exception as e:
        print(f"❌ Struktura lekcji - ERROR: {e}")

def test_data_files():
    """Test plików z danymi"""
    print("\n🧪 Testowanie plików z danymi...")
    
    try:
        from data.users import load_user_data
        users_data = load_user_data()
        print(f"✅ Załadowano dane {len(users_data)} użytkowników")
        
    except Exception as e:
        print(f"❌ Dane użytkowników - ERROR: {e}")
    
    # Test other data files
    files_to_check = [
        'users_data.json',
        'config/settings.py',
        'static/css/style.css'
    ]
    
    for file_path in files_to_check:
        full_path = os.path.join(APP_DIR, file_path)
        if os.path.exists(full_path):
            print(f"✅ {file_path} - EXISTS")
        else:
            print(f"⚠️ {file_path} - NOT FOUND")

def main():
    """Główna funkcja testowa"""
    print("🚀 Test Nowej Aplikacji ZenDegenAcademy")
    print("=" * 50)
    
    test_imports() 
    test_navigation_system()
    test_daily_missions()
    test_lesson_structure()
    test_data_files()
    
    print("\n" + "=" * 50)
    print("🎯 Test zakończony!")
    print("\n💡 Aby uruchomić nową aplikację:")
    print("   streamlit run main_new.py")
    print("\n📱 Aby uruchomić starą aplikację:")
    print("   streamlit run main.py")

if __name__ == "__main__":
    main()
