#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sprawdzający pełną spójność stylów przycisków nawigacji i "Dalej".
"""

import re

def test_button_consistency():
    """Sprawdź czy wszystkie przyciski (nawigacja + Dalej) mają spójny styl."""
    
    # Wczytaj plik lesson.py
    with open('views/lesson.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Sprawdzanie spójności wszystkich przycisków...")
    
    # 1. Sprawdź szerokość przycisków nawigacji (280px)
    nav_width_pattern = r'\.lesson-nav-container\s+\.stButton\s*>\s*button[^}]*width:\s*280px'
    nav_has_280px = bool(re.search(nav_width_pattern, content))
    
    print(f"✅ Przyciski nawigacji 280px: {'TAK' if nav_has_280px else '❌ NIE'}")
    
    # 2. Sprawdź szerokość przycisków "Dalej" (280px)
    next_width_pattern = r'\.next-button\s+\.stButton\s*>\s*button[^}]*width:\s*280px'
    next_has_280px = bool(re.search(next_width_pattern, content))
    
    print(f"✅ Przyciski 'Dalej' 280px: {'TAK' if next_has_280px else '❌ NIE'}")
    
    # 3. Sprawdź wysokość przycisków nawigacji (48px)
    nav_height_pattern = r'\.lesson-nav-container\s+\.stButton\s*>\s*button[^}]*height:\s*48px'
    nav_has_48px = bool(re.search(nav_height_pattern, content))
    
    print(f"✅ Wysokość przycisków nawigacji 48px: {'TAK' if nav_has_48px else '❌ NIE'}")
    
    # 4. Sprawdź wysokość przycisków "Dalej" (48px) 
    next_height_pattern = r'\.next-button\s+\.stButton\s*>\s*button[^}]*height:\s*48px'
    next_has_48px = bool(re.search(next_height_pattern, content))
    
    print(f"✅ Wysokość przycisków 'Dalej' 48px: {'TAK' if next_has_48px else '❌ NIE'}")
    
    # 5. Sprawdź font-size dla obu typów przycisków (0.9rem)
    nav_font_pattern = r'\.lesson-nav-container\s+\.stButton\s*>\s*button[^}]*font-size:\s*0\.9rem'
    nav_has_font = bool(re.search(nav_font_pattern, content))
    
    print(f"✅ Font-size przycisków nawigacji 0.9rem: {'TAK' if nav_has_font else '❌ NIE'}")
    
    next_font_pattern = r'\.next-button\s+\.stButton\s*>\s*button[^}]*font-size:\s*0\.9rem'
    next_has_font = bool(re.search(next_font_pattern, content))
    
    print(f"✅ Font-size przycisków 'Dalej' 0.9rem: {'TAK' if next_has_font else '❌ NIE'}")
    
    # 6. Sprawdź czy używany jest zen_button dla zablokowanych przycisków
    zen_button_pattern = r'zen_button\(\s*f"🔒 Dalej:'
    has_zen_button = bool(re.search(zen_button_pattern, content))
    
    print(f"✅ Użycie zen_button dla zablokowanych: {'TAK' if has_zen_button else '❌ NIE'}")
    
    # 7. Sprawdź czy nie ma już starych st.button dla zablokowanych
    old_button_pattern = r'st\.button\(\s*f"🔒 Dalej:'
    has_old_button = bool(re.search(old_button_pattern, content))
    
    print(f"✅ Brak starych st.button zablokowanych: {'TAK' if not has_old_button else '❌ NIE'}")
    
    # 8. Sprawdź czy przyciski "Dalej" mają centrowanie
    center_pattern = r'\.next-button[^}]*text-align:\s*center'
    has_center = bool(re.search(center_pattern, content))
    
    print(f"✅ Centrowanie przycisków 'Dalej': {'TAK' if has_center else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [
        nav_has_280px,
        next_has_280px,
        nav_has_48px,
        next_has_48px,
        nav_has_font,
        next_has_font,
        has_zen_button,
        not has_old_button,
        has_center
    ]
    
    passed = sum(all_checks)
    total = len(all_checks)
    
    print(f"\n📊 Wynik: {passed}/{total} sprawdzeń przeszło pomyślnie")
    
    if passed == total:
        print("🎉 DOSKONALE! Wszystkie przyciski mają teraz spójny styl:")
        print("   • Szerokość: 280px")
        print("   • Wysokość: 48px") 
        print("   • Font-size: 0.9rem")
        print("   • Właściwe funkcje przycisków")
        print("   • Centrowanie")
        return True
    else:
        print("⚠️ Niektóre sprawdzenia nie przeszły. Sprawdź szczegóły powyżej.")
        return False

if __name__ == "__main__":
    test_button_consistency()
