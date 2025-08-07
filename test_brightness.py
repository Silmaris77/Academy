#!/usr/bin/env python3
"""
Test sprawdzający czy tło zostało rozjaśnione dla lepszej czytelności tekstu
"""

import re

def test_brightness_improvements():
    """Sprawdza czy tło zostało rozjaśnione i kontrast poprawiony"""
    print("💡 Sprawdzam rozjaśnienie tła dla lepszej czytelności...")
    
    with open('static/css/style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    checks = []
    
    print("\n🎨 Sprawdzanie głównych kolorów:")
    
    # Sprawdź czy background-light został rozjaśniony
    bg_light_brightened = "#4A5568" in css_content and "background-light:" in css_content
    
    # Sprawdź czy background-card zostało rozjaśnione
    bg_card_brightened = "#4A5568" in css_content and "background-card:" in css_content
    
    # Sprawdź czy text-primary został rozjaśniony
    text_primary_brightened = "--text-primary: #F7FAFC" in css_content
    
    # Sprawdź czy text-secondary został rozjaśniony
    text_secondary_brightened = "--text-secondary: #E2E8F0" in css_content
    
    checks.extend([
        ("✅ Główne tło rozjaśnione" if bg_light_brightened else "❌ Główne tło nie zostało rozjaśnione", bg_light_brightened),
        ("✅ Tło kart rozjaśnione" if bg_card_brightened else "❌ Tło kart nie zostało rozjaśnione", bg_card_brightened),
        ("✅ Tekst główny rozjaśniony" if text_primary_brightened else "❌ Tekst główny nie został rozjaśniony", text_primary_brightened),
        ("✅ Tekst drugorzędny rozjaśniony" if text_secondary_brightened else "❌ Tekst drugorzędny nie został rozjaśniony", text_secondary_brightened)
    ])
    
    print("\n🔳 Sprawdzanie kontrastów i ramek:")
    
    # Sprawdź czy ramki zostały wzmocnione do 0.15
    border_contrast_improved = css_content.count("rgba(255,255,255,0.15)") >= 5
    
    # Sprawdź czy przyciski sidebar zostały rozjaśnione
    sidebar_buttons_brightened = "#5A6A7C" in css_content and "stSidebar" in css_content
    
    # Sprawdź czy hover states zostały zaktualizowane
    hover_brightened = "#6A7A8C" in css_content
    
    checks.extend([
        ("✅ Ramki mają lepszy kontrast" if border_contrast_improved else "❌ Ramki bez poprawy kontrastu", border_contrast_improved),
        ("✅ Przyciski sidebar rozjaśnione" if sidebar_buttons_brightened else "❌ Przyciski sidebar nie zostały rozjaśnione", sidebar_buttons_brightened),
        ("✅ Hover states rozjaśnione" if hover_brightened else "❌ Hover states nie zostały rozjaśnione", hover_brightened)
    ])
    
    print("\n📱 Sprawdzanie elementów interfejsu:")
    
    # Sprawdź czy wszystkie główne klasy mają poprawione tło
    degen_card_ok = "background: var(--background-card)" in css_content and ".degen-card {" in css_content
    mission_card_ok = "background: var(--background-card)" in css_content and ".mission-card {" in css_content
    stat_card_ok = "background: var(--background-card)" in css_content and ".stat-card {" in css_content
    dashboard_section_ok = "background: var(--background-card)" in css_content and ".dashboard-section {" in css_content
    
    checks.extend([
        ("✅ Degen cards używają nowego tła" if degen_card_ok else "❌ Degen cards bez nowego tła", degen_card_ok),
        ("✅ Mission cards używają nowego tła" if mission_card_ok else "❌ Mission cards bez nowego tła", mission_card_ok),
        ("✅ Stat cards używają nowego tła" if stat_card_ok else "❌ Stat cards bez nowego tła", stat_card_ok),
        ("✅ Dashboard sections używają nowego tła" if dashboard_section_ok else "❌ Dashboard sections bez nowego tła", dashboard_section_ok)
    ])
    
    # Wyświetl wyniki
    print(f"\n{'='*65}")
    print("📊 PODSUMOWANIE TESTÓW ROZJAŚNIENIA TŁA:")
    print(f"{'='*65}")
    
    passed = 0
    total = len(checks)
    
    for message, result in checks:
        print(message)
        if result:
            passed += 1
    
    print(f"\n🎯 Wynik: {passed}/{total} testów przeszło pomyślnie")
    
    if passed == total:
        print("🎉 SUKCES! Tło zostało rozjaśnione dla lepszej czytelności!")
        print("💡 Wszystkie elementy mają lepszy kontrast i jaśniejsze kolory")
        print("📚 Tekst powinien być teraz znacznie lepiej widoczny")
    else:
        print("⚠️ Niektóre elementy wymagają jeszcze poprawek")
        print("🔧 Sprawdź powyższe wyniki i popraw brakujące style")
    
    # Pokazuj konkretne wartości kolorów
    print(f"\n🎨 NOWE KOLORY:")
    print(f"- Główne tło: #4A5568 → #4F5B6B → #3A4A5C")
    print(f"- Tło kart: #4A5568 → #3F4A5A")
    print(f"- Tekst główny: #F7FAFC (bardzo jasny)")
    print(f"- Tekst drugorzędny: #E2E8F0 (jasny)")
    print(f"- Ramki: rgba(255,255,255,0.15) (15% przezroczystości)")
    
    return passed == total

if __name__ == "__main__":
    test_brightness_improvements()
