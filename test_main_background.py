#!/usr/bin/env python3
"""
Test sprawdzający czy główne tło aplikacji ma ciemny kolor grafitowy
"""

import re

def test_main_background_fix():
    """Sprawdza czy główne tło zostało zmienione na ciemne"""
    print("🎨 Sprawdzam implementację ciemnego tła głównej strony...")
    
    with open('static/css/style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    checks = []
    
    print("\n🔍 Sprawdzanie elementów głównego tła:")
    
    # Sprawdź czy .stApp ma ciemne tło
    stapp_bg_check = ".stApp {\n    background: var(--background-light)" in css_content
    
    # Sprawdź czy body ma ciemne tło  
    body_bg_check = "body {\n    background: var(--background-light)" in css_content
    
    # Sprawdź czy block-container ma transparentne tło
    block_container_check = "background: transparent" in css_content and ".main .block-container" in css_content
    
    # Sprawdź czy główny kontener ma ciemne tło
    section_main_check = "section.main {\n    background: var(--background-light)" in css_content
    
    # Sprawdź czy stAppViewContainer ma ciemne tło
    app_view_check = "[data-testid=\"stAppViewContainer\"] {\n    background: var(--background-light)" in css_content
    
    checks.extend([
        ("✅ .stApp ma ciemne tło" if stapp_bg_check else "❌ .stApp bez ciemnego tła", stapp_bg_check),
        ("✅ body ma ciemne tło" if body_bg_check else "❌ body bez ciemnego tła", body_bg_check),
        ("✅ block-container ma transparentne tło" if block_container_check else "❌ block-container bez transparentnego tła", block_container_check),
        ("✅ section.main ma ciemne tło" if section_main_check else "❌ section.main bez ciemnego tła", section_main_check),
        ("✅ stAppViewContainer ma ciemne tło" if app_view_check else "❌ stAppViewContainer bez ciemnego tła", app_view_check)
    ])
    
    print("\n🎯 Sprawdzanie przycisków i elementów:")
    
    # Sprawdź czy przyciski mają ciemne tło
    button_bg_check = "background: var(--background-card)" in css_content and "[data-testid=\"stButton\"] button {" in css_content
    
    # Sprawdź czy avatar-option ma ciemne tło
    avatar_bg_check = "background: var(--background-card)" in css_content and ".avatar-option {" in css_content
    
    # Sprawdź czy nie zostały białe tła
    white_bg_count = css_content.count("background: white")
    white_bg_color_count = css_content.count("background-color: white")
    
    checks.extend([
        ("✅ Przyciski mają ciemne tło" if button_bg_check else "❌ Przyciski bez ciemnego tła", button_bg_check),
        ("✅ Avatar options mają ciemne tło" if avatar_bg_check else "❌ Avatar options bez ciemnego tła", avatar_bg_check),
        ("✅ Brak białych tłem (background: white)" if white_bg_count == 0 else f"❌ Znaleziono {white_bg_count} białych tła", white_bg_count == 0),
        ("✅ Brak białych tłem (background-color: white)" if white_bg_color_count == 0 else f"❌ Znaleziono {white_bg_color_count} białych tła", white_bg_color_count == 0)
    ])
    
    # Wyświetl wyniki
    print(f"\n{'='*60}")
    print("📊 PODSUMOWANIE TESTÓW GŁÓWNEGO TŁA:")
    print(f"{'='*60}")
    
    passed = 0
    total = len(checks)
    
    for message, result in checks:
        print(message)
        if result:
            passed += 1
    
    print(f"\n🎯 Wynik: {passed}/{total} testów przeszło pomyślnie")
    
    if passed == total:
        print("🎉 SUKCES! Główne tło zostało poprawnie zmienione na ciemne!")
        print("🎨 Cała aplikacja ma teraz spójny ciemny motyw z gradientami grafitowymi")
    else:
        print("⚠️ Niektóre elementy wymagają jeszcze poprawek")
        print("🔧 Sprawdź powyższe wyniki i popraw brakujące style")
    
    return passed == total

if __name__ == "__main__":
    test_main_background_fix()
