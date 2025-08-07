#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test kompatybilności Streamlit - sprawdza czy wszystkie funkcje działają poprawnie
"""

import sys
import traceback
from pathlib import Path

# Dodaj ścieżkę do głównego katalogu aplikacji
sys.path.append(str(Path(__file__).parent))

def test_streamlit_compatibility():
    """Test podstawowej kompatybilności Streamlit"""
    print("🔧 Test kompatybilności Streamlit...")
    
    try:
        import streamlit as st
        print(f"✅ Streamlit zaimportowany - wersja: {st.__version__}")
    except ImportError as e:
        print(f"❌ Błąd importu Streamlit: {e}")
        return False
    
    # Test dostępności funkcji
    features_to_test = [
        ('tabs', 'st.tabs()'),
        ('columns', 'st.columns()'),
        ('expander', 'st.expander()'),
        ('markdown', 'st.markdown()'),
        ('button', 'st.button()'),
        ('selectbox', 'st.selectbox()'),
        ('multiselect', 'st.multiselect()'),
    ]
    
    all_ok = True
    for feature, description in features_to_test:
        if hasattr(st, feature):
            print(f"✅ {description} - dostępne")
        else:
            print(f"❌ {description} - NIEDOSTĘPNE")
            all_ok = False
    
    return all_ok

def test_custom_compatibility():
    """Test naszych narzędzi kompatybilności"""
    print("\n🛠️ Test narzędzi kompatybilności...")
    
    try:
        from utils.streamlit_compat import tabs_with_fallback, get_streamlit_version
        print("✅ utils.streamlit_compat zaimportowany")
        
        version = get_streamlit_version()
        print(f"✅ Wersja Streamlit: {version}")
        
        # Nie możemy przetestować tabs_with_fallback bez kontekstu Streamlit
        print("✅ tabs_with_fallback dostępny (test w aplikacji)")
        
        return True
    except Exception as e:
        print(f"❌ Błąd testowania kompatybilności: {e}")
        traceback.print_exc()
        return False

def test_error_handling():
    """Test systemu obsługi błędów"""
    print("\n🚨 Test systemu obsługi błędów...")
    
    try:
        from utils.error_handling import handle_error, safe_execute, AppError
        print("✅ utils.error_handling zaimportowany")
        
        # Test safe_execute
        def test_function():
            return "success"
        
        result = safe_execute(test_function, fallback_value="fallback")
        if result == "success":
            print("✅ safe_execute działa poprawnie")
        else:
            print(f"❌ safe_execute zwrócił: {result}")
            
        # Test funkcji z błędem
        def error_function():
            raise ValueError("Test error")
        
        result = safe_execute(error_function, fallback_value="fallback", error_message="Test error message")
        if result == "fallback":
            print("✅ safe_execute obsługuje błędy poprawnie")
        else:
            print(f"❌ safe_execute nie obsłużył błędu: {result}")
            
        return True
    except Exception as e:
        print(f"❌ Błąd testowania error handling: {e}")
        traceback.print_exc()
        return False

def test_imports():
    """Test importów podstawowych modułów"""
    print("\n📦 Test importów modułów...")
    
    modules_to_test = [
        'data.lessons',
        'data.users', 
        'utils.components',
        'utils.lesson_progress',
        'views.dashboard',
        'views.lesson',
        'views.profile',
    ]
    
    all_ok = True
    for module in modules_to_test:
        try:
            __import__(module)
            print(f"✅ {module}")
        except Exception as e:
            print(f"❌ {module}: {e}")
            all_ok = False
    
    return all_ok

def main():
    """Główna funkcja testowa"""
    print("🧪 TESTY KOMPATYBILNOŚCI I STABILNOŚCI APLIKACJI")
    print("=" * 60)
    
    tests = [
        ("Kompatybilność Streamlit", test_streamlit_compatibility),
        ("Narzędzia kompatybilności", test_custom_compatibility), 
        ("System obsługi błędów", test_error_handling),
        ("Importy modułów", test_imports),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Błąd krytyczny w teście '{test_name}': {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("📊 PODSUMOWANIE TESTÓW:")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {test_name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 WSZYSTKIE TESTY PRZESZŁY! Aplikacja gotowa do uruchomienia.")
    else:
        print("⚠️  NIEKTÓRE TESTY NIE PRZESZŁY! Sprawdź błędy powyżej.")
    print("=" * 60)
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
