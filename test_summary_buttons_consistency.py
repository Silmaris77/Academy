#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sprawdzający czy przyciski "Zakończ lekcję" i "Wróć do wszystkich lekcji" mają spójny layout z innymi przyciskami.
"""

import re

def test_summary_buttons_consistency():
    """Sprawdź czy wszystkie przyciski w sekcji summary mają spójny styl i layout."""
    
    # Wczytaj plik lesson.py
    with open('views/lesson.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Sprawdzanie przycisków w sekcji summary...")
    
    # 1. Sprawdź czy przycisk "Zakończ lekcję" używa kolumn st.columns([1, 1, 1])
    finish_button_columns_pattern = r'zen_button\("🎉 Zakończ lekcję"[^}]*\)\s*:\s*.*?col1,\s*col2,\s*col3\s*=\s*st\.columns\(\[1,\s*1,\s*1\]\)'
    finish_has_columns = bool(re.search(finish_button_columns_pattern, content, re.DOTALL))
    
    # Alternatywna metoda - sprawdź czy kolumny są przed przyciskiem
    finish_context = re.search(r'col1,\s*col2,\s*col3\s*=\s*st\.columns\(\[1,\s*1,\s*1\]\).*?zen_button\("🎉 Zakończ lekcję"', content, re.DOTALL)
    finish_has_columns = bool(finish_context)
    
    print(f"✅ Przycisk 'Zakończ lekcję' używa kolumn: {'TAK' if finish_has_columns else '❌ NIE'}")
    
    # 2. Sprawdź czy przycisk "Zakończ lekcję" używa use_container_width=True
    finish_container_width_pattern = r'zen_button\("🎉 Zakończ lekcję",\s*use_container_width=True\)'
    finish_has_container_width = bool(re.search(finish_container_width_pattern, content))
    
    print(f"✅ Przycisk 'Zakończ lekcję' use_container_width=True: {'TAK' if finish_has_container_width else '❌ NIE'}")
    
    # 3. Sprawdź czy przycisk "Wróć do wszystkich lekcji" używa kolumn
    back_context = re.search(r'col1,\s*col2,\s*col3\s*=\s*st\.columns\(\[1,\s*1,\s*1\]\).*?zen_button\("📚 Wróć do wszystkich lekcji"', content, re.DOTALL)
    back_has_columns = bool(back_context)
    
    print(f"✅ Przycisk 'Wróć do wszystkich lekcji' używa kolumn: {'TAK' if back_has_columns else '❌ NIE'}")
    
    # 4. Sprawdź czy przycisk "Wróć do wszystkich lekcji" używa use_container_width=True
    back_container_width_pattern = r'zen_button\("📚 Wróć do wszystkich lekcji",\s*use_container_width=True\)'
    back_has_container_width = bool(re.search(back_container_width_pattern, content))
    
    print(f"✅ Przycisk 'Wróć do wszystkich lekcji' use_container_width=True: {'TAK' if back_has_container_width else '❌ NIE'}")
    
    # 5. Sprawdź czy oba przyciski używają klasy CSS next-button
    finish_next_button_pattern = r'st\.markdown\("<div class=\'next-button\'>"[^}]*zen_button\("🎉 Zakończ lekcję"'
    finish_has_next_button_class = bool(re.search(finish_next_button_pattern, content, re.DOTALL))
    
    print(f"✅ Przycisk 'Zakończ lekcję' ma klasę next-button: {'TAK' if finish_has_next_button_class else '❌ NIE'}")
    
    back_next_button_pattern = r'st\.markdown\("<div class=\'next-button\'>"[^}]*zen_button\("📚 Wróć do wszystkich lekcji"'
    back_has_next_button_class = bool(re.search(back_next_button_pattern, content, re.DOTALL))
    
    print(f"✅ Przycisk 'Wróć do wszystkich lekcji' ma klasę next-button: {'TAK' if back_has_next_button_class else '❌ NIE'}")
    
    # 6. Sprawdź czy są używane w bloku with col2:
    finish_with_col2_pattern = r'with\s+col2:\s*if\s+zen_button\("🎉 Zakończ lekcję"'
    finish_has_with_col2 = bool(re.search(finish_with_col2_pattern, content))
    
    print(f"✅ Przycisk 'Zakończ lekcję' w bloku 'with col2:': {'TAK' if finish_has_with_col2 else '❌ NIE'}")
    
    back_with_col2_pattern = r'with\s+col2:\s*if\s+zen_button\("📚 Wróć do wszystkich lekcji"'
    back_has_with_col2 = bool(re.search(back_with_col2_pattern, content))
    
    print(f"✅ Przycisk 'Wróć do wszystkich lekcji' w bloku 'with col2:': {'TAK' if back_has_with_col2 else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [
        finish_has_columns,
        finish_has_container_width,
        back_has_columns,
        back_has_container_width,
        finish_has_next_button_class,
        back_has_next_button_class,
        finish_has_with_col2,
        back_has_with_col2
    ]
    
    passed = sum(all_checks)
    total = len(all_checks)
    
    print(f"\n📊 Wynik: {passed}/{total} sprawdzeń przeszło pomyślnie")
    
    if passed == total:
        print("🎉 DOSKONALE! Wszystkie przyciski w sekcji summary mają spójny layout:")
        print("   • Używają kolumn st.columns([1, 1, 1])")
        print("   • Są w bloku 'with col2:' (wyśrodkowane)")
        print("   • Używają use_container_width=True")
        print("   • Mają klasę CSS 'next-button'")
        print("   • Będą mieć szerokość 280px jak inne przyciski")
        return True
    else:
        print("⚠️ Niektóre sprawdzenia nie przeszły. Sprawdź szczegóły powyżej.")
        return False

if __name__ == "__main__":
    test_summary_buttons_consistency()
