#!/usr/bin/env python3
"""
Test sprawdzający czy wszystkie przyciski w sidebarze mają jednakową szerokość
"""

import os
import re

def test_sidebar_button_width():
    """Sprawdza czy implementacja przycisków zapewnia jednakową szerokość"""
    
    print("🔍 Test szerokości przycisków w sidebarze")
    print("=" * 50)
    
    # Sprawdź CSS dla przycisków sidebara
    css_path = "static/css/style.css"
    if not os.path.exists(css_path):
        print("❌ Błąd: Nie znaleziono pliku CSS")
        return False
    
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # 1. Sprawdź czy jest reguła width: 100% dla przycisków sidebar
    width_pattern = r'\.stSidebar.*?button.*?width:\s*100%\s*!important'
    has_width_rule = bool(re.search(width_pattern, css_content, re.DOTALL))
    print(f"✅ Reguła width: 100% dla przycisków sidebar: {'TAK' if has_width_rule else '❌ NIE'}")
    
    # 2. Sprawdź czy jest reguła display: block
    display_pattern = r'\.stSidebar.*?button.*?display:\s*block\s*!important'
    has_display_rule = bool(re.search(display_pattern, css_content, re.DOTALL))
    print(f"✅ Reguła display: block dla przycisków sidebar: {'TAK' if has_display_rule else '❌ NIE'}")
    
    # Sprawdź komponenty navigation_menu
    components_path = "utils/components.py"
    if not os.path.exists(components_path):
        print("❌ Błąd: Nie znaleziono pliku components.py")
        return False
    
    with open(components_path, 'r', encoding='utf-8') as f:
        components_content = f.read()
    
    # 3. Sprawdź czy zen_button ma use_container_width=True w navigation_menu
    nav_button_pattern = r'zen_button\([^)]*use_container_width=True[^)]*\)'
    has_container_width = bool(re.search(nav_button_pattern, components_content))
    print(f"✅ zen_button z use_container_width=True: {'TAK' if has_container_width else '❌ NIE'}")
    
    # Sprawdź main.py dla przycisku wylogowania
    main_path = "main.py"
    if not os.path.exists(main_path):
        print("❌ Błąd: Nie znaleziono pliku main.py")
        return False
    
    with open(main_path, 'r', encoding='utf-8') as f:
        main_content = f.read()
    
    # 4. Sprawdź czy przycisk wylogowania używa zen_button z use_container_width=True
    logout_pattern = r'zen_button\("🚪 Wyloguj się".*?use_container_width=True[^)]*\)'
    has_logout_width = bool(re.search(logout_pattern, main_content))
    print(f"✅ Przycisk wylogowania z use_container_width=True: {'TAK' if has_logout_width else '❌ NIE'}")
    
    # 5. Sprawdź czy zen_button jest importowany w main.py
    import_pattern = r'from utils\.components import.*zen_button'
    has_import = bool(re.search(import_pattern, main_content))
    print(f"✅ Import zen_button w main.py: {'TAK' if has_import else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [has_width_rule, has_display_rule, has_container_width, has_logout_width, has_import]
    success_count = sum(all_checks)
    
    print("\n" + "=" * 50)
    print(f"📊 Wynik testu: {success_count}/5 sprawdzeń zaliczonych")
    
    if success_count == 5:
        print("🎉 SUKCES: Wszystkie przyciski w sidebarze powinny mieć jednakową szerokość!")
        return True
    else:
        print("⚠️  UWAGA: Niektóre sprawdzenia nie przeszły. Sprawdź implementację.")
        return False

if __name__ == "__main__":
    # Zmień katalog na główny katalog aplikacji
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    test_sidebar_button_width()
