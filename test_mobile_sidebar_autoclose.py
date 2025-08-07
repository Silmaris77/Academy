#!/usr/bin/env python3
"""
Test sprawdzający czy automatyczne zamykanie sidebar w wersji mobilnej działa
"""

import os
import re

def test_mobile_sidebar_autoclose():
    """Sprawdza czy implementacja automatycznego zamykania sidebar w wersji mobilnej jest prawidłowa"""
    
    print("📱 Test automatycznego zamykania sidebar w wersji mobilnej")
    print("=" * 60)
    
    # Sprawdź components.py - funkcja navigation_menu
    components_path = "utils/components.py"
    if not os.path.exists(components_path):
        print("❌ Błąd: Nie znaleziono pliku components.py")
        return False
    
    with open(components_path, 'r', encoding='utf-8') as f:
        components_content = f.read()
    
    # 1. Sprawdź czy jest JavaScript do zamykania sidebar
    js_pattern = r'closeSidebarOnMobile.*window\.innerWidth.*768'
    has_js_script = bool(re.search(js_pattern, components_content, re.DOTALL))
    print(f"✅ JavaScript do zamykania sidebar: {'TAK' if has_js_script else '❌ NIE'}")
    
    # 2. Sprawdź czy jest obsługa event listeners dla przycisków
    event_pattern = r'addEventListener.*click.*setTimeout.*closeSidebarOnMobile'
    has_event_listeners = bool(re.search(event_pattern, components_content, re.DOTALL))
    print(f"✅ Event listeners dla przycisków nawigacji: {'TAK' if has_event_listeners else '❌ NIE'}")
    
    # 3. Sprawdź czy skrypt jest renderowany tylko raz
    session_pattern = r'mobile_sidebar_script_loaded.*st\.session_state'
    has_session_control = bool(re.search(session_pattern, components_content))
    print(f"✅ Kontrola jednorazowego ładowania skryptu: {'TAK' if has_session_control else '❌ NIE'}")
    
    # 4. Sprawdź czy jest selektor collapsedControl
    selector_pattern = r'collapsedControl'
    has_correct_selector = bool(re.search(selector_pattern, components_content))
    print(f"✅ Poprawny selektor przycisku zamykania: {'TAK' if has_correct_selector else '❌ NIE'}")
    
    # Sprawdź main.py - przycisk wylogowania
    main_path = "main.py"
    if not os.path.exists(main_path):
        print("❌ Błąd: Nie znaleziono pliku main.py")
        return False
    
    with open(main_path, 'r', encoding='utf-8') as f:
        main_content = f.read()
    
    # 5. Sprawdź czy przycisk wylogowania ma obsługę zamykania sidebar
    logout_js_pattern = r'zen_button.*Wyloguj się.*window\.innerWidth.*768.*collapsedControl'
    has_logout_js = bool(re.search(logout_js_pattern, main_content, re.DOTALL))
    print(f"✅ Obsługa zamykania sidebar dla wylogowania: {'TAK' if has_logout_js else '❌ NIE'}")
    
    # Sprawdź CSS
    css_path = "static/css/style.css"
    if not os.path.exists(css_path):
        print("❌ Błąd: Nie znaleziono pliku CSS")
        return False
    
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # 6. Sprawdź czy są usprawnienia dla mobile touch
    touch_pattern = r'touch-action:\s*manipulation'
    has_touch_improvements = bool(re.search(touch_pattern, css_content))
    print(f"✅ Usprawnienia dla mobile touch: {'TAK' if has_touch_improvements else '❌ NIE'}")
    
    # 7. Sprawdź czy są szybsze animacje dla mobilnych
    animation_pattern = r'transition:.*0\.2s.*ease'
    has_mobile_animations = bool(re.search(animation_pattern, css_content))
    print(f"✅ Szybsze animacje dla mobilnych: {'TAK' if has_mobile_animations else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [
        has_js_script, 
        has_event_listeners, 
        has_session_control, 
        has_correct_selector,
        has_logout_js,
        has_touch_improvements,
        has_mobile_animations
    ]
    success_count = sum(all_checks)
    
    print("\n" + "=" * 60)
    print(f"📊 Wynik testu: {success_count}/7 sprawdzeń zaliczonych")
    
    if success_count >= 5:
        print("🎉 SUKCES: Automatyczne zamykanie sidebar w wersji mobilnej powinno działać!")
        return True
    else:
        print("⚠️  UWAGA: Niektóre sprawdzenia nie przeszły. Sprawdź implementację.")
        return False

if __name__ == "__main__":
    # Zmień katalog na główny katalog aplikacji
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    test_mobile_sidebar_autoclose()
