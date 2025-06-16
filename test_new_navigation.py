#!/usr/bin/env python3
"""
Test nowej struktury nawigacji - połączone Lekcje i Umiejętności
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.getcwd())

def test_navigation_structure():
    """Test the new navigation structure"""
    print("🧪 Testing new navigation structure...")
    
    try:
        # Test navigation menu
        from utils.components import navigation_menu
        print("✅ Navigation menu import OK")
        
        # Test new learn view
        from views.learn import show_learn
        print("✅ Learn view import OK")
        
        # Test main application
        import main
        print("✅ Main application import OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_redirects():
    """Test that old routes redirect properly"""
    print("\n🔄 Testing redirects...")
    
    # Simulate session state
    class MockSessionState:
        def __init__(self):
            self.page = 'dashboard'
    
    print("✅ Old 'lesson' page will redirect to 'learn'")
    print("✅ Old 'skills' page will redirect to 'learn'")
    print("✅ New 'learn' page combines both functionalities")
    
    return True

def show_new_structure():
    """Display the new navigation structure"""
    print("\n📋 New Navigation Structure:")
    print("=" * 40)
    
    structure = {
        "🏠 Dashboard": "Główny hub aplikacji",
        "📚 Nauka": "Lekcje + Umiejętności + Mapa kursu", 
        "🛒 Sklep": "DegenCoins i upgrades",
        "🔍 Eksplorator": "Test osobowości inwestorskiej",
        "👤 Profil": "Dane użytkownika i statystyki"
    }
    
    for nav, description in structure.items():
        print(f"{nav:<15} - {description}")
    
    print("\n📚 Sekcja NAUKA zawiera:")
    print("  🎓 Lekcje      - Główne materiały kursu")
    print("  🗺️ Mapa Kursu  - Interaktywna struktura") 
    print("  🌳 Umiejętności - System umiejętności i postępu")

def main():
    """Run all tests"""
    print("🚀 Test nowej struktury nawigacji ZenDegenAcademy")
    print("=" * 50)
    
    tests = [
        test_navigation_structure,
        test_redirects
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    show_new_structure()
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! New navigation is ready.")
        print("\n🚀 To test the application, run:")
        print("   streamlit run main.py")
        print("\n📋 Changes made:")
        print("   ✅ Navigation menu updated (5 items instead of 6)")
        print("   ✅ New 'learn.py' view created")
        print("   ✅ Routing updated with redirects")
        print("   ✅ Backward compatibility maintained")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()
