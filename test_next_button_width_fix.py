#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sprawdzający czy przyciski "Dalej" mają zwiększoną szerokość 280px.
"""

import re

def test_next_button_width_fix():
    """Sprawdź czy CSS dla przycisków 'Dalej' ma szerokość 280px."""
    
    # Wczytaj plik lesson.py
    with open('views/lesson.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Sprawdzanie szerokości przycisków 'Dalej'...")
    
    # 1. Sprawdź czy szerokość przycisku to 280px
    button_width_pattern = r'\.next-button\s+\.stButton\s*>\s*button[^}]*width:\s*280px'
    has_280px_width = bool(re.search(button_width_pattern, content))
    
    print(f"✅ Szerokość przycisku (280px): {'TAK' if has_280px_width else '❌ NIE'}")
    
    # 2. Sprawdź czy min-width przycisku to 280px  
    min_width_pattern = r'\.next-button\s+\.stButton\s*>\s*button[^}]*min-width:\s*280px'
    has_280px_min_width = bool(re.search(min_width_pattern, content))
    
    print(f"✅ Min-width przycisku (280px): {'TAK' if has_280px_min_width else '❌ NIE'}")
    
    # 3. Sprawdź czy kontener .stButton ma szerokość 280px
    container_width_pattern = r'\.next-button\s+\.stButton[^}]*width:\s*280px'
    has_280px_container = bool(re.search(container_width_pattern, content))
    
    print(f"✅ Szerokość kontenera .stButton (280px): {'TAK' if has_280px_container else '❌ NIE'}")
    
    # 4. Sprawdź czy div > element ma szerokość 280px
    div_width_pattern = r'\.next-button\s*>\s*div[^}]*width:\s*280px'
    has_280px_div = bool(re.search(div_width_pattern, content))
    
    print(f"✅ Szerokość div zawierającego (280px): {'TAK' if has_280px_div else '❌ NIE'}")
    
    # 5. Sprawdź czy max-width dla wszystkich elementów to 280px
    max_width_pattern = r'\.next-button\s*\*[^}]*max-width:\s*280px'
    has_280px_max_width = bool(re.search(max_width_pattern, content))
    
    print(f"✅ Max-width wszystkich elementów (280px): {'TAK' if has_280px_max_width else '❌ NIE'}")
    
    # 6. Sprawdź czy nie ma już starych wartości 180px
    old_180px_pattern = r'width:\s*180px'
    has_old_180px = bool(re.search(old_180px_pattern, content))
    
    print(f"✅ Brak starych wartości 180px: {'TAK' if not has_old_180px else '❌ NIE, WCIĄŻ SĄ'}")
    
    # 7. Porównaj z szerokością przycisków nawigacji (powinny mieć width: 100%)
    nav_width_pattern = r'\.lesson-nav-container\s+\.stButton\s*>\s*button[^}]*width:\s*100%'
    nav_has_100_percent = bool(re.search(nav_width_pattern, content))
    
    print(f"✅ Przyciski nawigacji mają width: 100%: {'TAK' if nav_has_100_percent else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [
        has_280px_width,
        has_280px_min_width,
        has_280px_container,
        has_280px_div,
        has_280px_max_width,
        not has_old_180px,
        nav_has_100_percent
    ]
    
    passed = sum(all_checks)
    total = len(all_checks)
    
    print(f"\n📊 Wynik: {passed}/{total} sprawdzeń przeszło pomyślnie")
    
    if passed == total:
        print("🎉 Wszystkie sprawdzenia przeszły! Przyciski 'Dalej' mają teraz szerokość 280px.")
        return True
    else:
        print("⚠️ Niektóre sprawdzenia nie przeszły. Sprawdź powyższe szczegóły.")
        return False

if __name__ == "__main__":
    test_next_button_width_fix()
