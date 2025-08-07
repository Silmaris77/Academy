#!/usr/bin/env python3
"""
Test sprawdzający implementację ciemnego motywu z gradientami grafitowymi
"""

import re

def test_dark_theme_implementation():
    """Sprawdza czy wszystkie elementy mają właściwe ciemne tło z gradientami"""
    print("🎨 Sprawdzam implementację ciemnego motywu...")
    
    with open('static/css/style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    checks = []
    
    # Sprawdź czy główne zmienne CSS zostały zaktualizowane
    print("\n📋 Sprawdzanie głównych zmiennych CSS:")
    
    # Background variables
    background_light_check = "background-light: linear-gradient" in css_content
    background_card_check = "background-card: linear-gradient" in css_content
    text_primary_check = "--text-primary: #ECEFF4" in css_content
    
    checks.extend([
        ("✅ Background light z gradientem" if background_light_check else "❌ Brak background light z gradientem", background_light_check),
        ("✅ Background card z gradientem" if background_card_check else "❌ Brak background card z gradientem", background_card_check),
        ("✅ Jasny kolor tekstu" if text_primary_check else "❌ Brak jasnego koloru tekstu", text_primary_check)
    ])
    
    # Sprawdź style podstawowe
    print("\n🏗️ Sprawdzanie stylów podstawowych:")
    
    main_bg_check = ".main {\n    background: var(--background-light)" in css_content
    stbx_bg_check = "background: var(--background-card)" in css_content and ".st-bx {" in css_content
    
    checks.extend([
        ("✅ Main z ciemnym tłem" if main_bg_check else "❌ Main bez ciemnego tła", main_bg_check),
        ("✅ st-bx z gradientowym tłem" if stbx_bg_check else "❌ st-bx bez gradientowego tła", stbx_bg_check)
    ])
    
    # Sprawdź karty
    print("\n🎴 Sprawdzanie kart:")
    
    degen_card_bg = "background: var(--background-card)" in css_content and ".degen-card {" in css_content
    mission_card_bg = "background: var(--background-card)" in css_content and ".mission-card {" in css_content
    stat_card_bg = "background: var(--background-card)" in css_content and ".stat-card {" in css_content
    
    checks.extend([
        ("✅ Degen card z ciemnym tłem" if degen_card_bg else "❌ Degen card bez ciemnego tła", degen_card_bg),
        ("✅ Mission card z ciemnym tłem" if mission_card_bg else "❌ Mission card bez ciemnego tła", mission_card_bg),
        ("✅ Stat card z ciemnym tłem" if stat_card_bg else "❌ Stat card bez ciemnego tła", stat_card_bg)
    ])
    
    # Sprawdź sidebar
    print("\n📱 Sprawdzanie sidebara:")
    
    sidebar_bg_check = "background: var(--background-dark)" in css_content
    sidebar_buttons_check = "linear-gradient(145deg, #4A5A6C 0%, #3F4F5F 100%)" in css_content
    
    checks.extend([
        ("✅ Sidebar z ciemnym tłem" if sidebar_bg_check else "❌ Sidebar bez ciemnego tła", sidebar_bg_check),
        ("✅ Przyciski sidebar z gradientem" if sidebar_buttons_check else "❌ Przyciski sidebar bez gradientu", sidebar_buttons_check)
    ])
    
    # Sprawdź hover states
    print("\n🖱️ Sprawdzanie efektów hover:")
    
    hover_bg_check = "background: var(--background-card-hover)" in css_content
    gradient_hover_count = css_content.count("linear-gradient(145deg")
    
    checks.extend([
        ("✅ Hover states z ciemnym tłem" if hover_bg_check else "❌ Brak hover states z ciemnym tłem", hover_bg_check),
        ("✅ Wystarczająco gradientów" if gradient_hover_count >= 5 else f"❌ Za mało gradientów ({gradient_hover_count})", gradient_hover_count >= 5)
    ])
    
    # Wyświetl wyniki
    print(f"\n{'='*50}")
    print("📊 PODSUMOWANIE TESTÓW:")
    print(f"{'='*50}")
    
    passed = 0
    total = len(checks)
    
    for message, result in checks:
        print(message)
        if result:
            passed += 1
    
    print(f"\n🎯 Wynik: {passed}/{total} testów przeszło pomyślnie")
    
    if passed == total:
        print("🎉 SUKCES! Ciemny motyw został poprawnie zaimplementowany!")
        print("🎨 Wszystkie elementy mają ciemne tło z gradientami grafitowymi")
    else:
        print("⚠️ Niektóre elementy wymagają poprawek")
        print("🔧 Sprawdź powyższe wyniki i popraw brakujące style")
    
    return passed == total

if __name__ == "__main__":
    test_dark_theme_implementation()
