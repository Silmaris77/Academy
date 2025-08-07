#!/usr/bin/env python3
"""
Test sprawdzający poprawione ustawienia sidebara mobilnego
"""

import os
import re

def test_fixed_mobile_sidebar():
    """Sprawdza czy poprawione ustawienia sidebara mobilnego są prawidłowe"""
    
    print("📱 Test poprawionych ustawień sidebara mobilnego")
    print("=" * 55)
    
    # Sprawdź CSS
    css_path = "static/css/style.css"
    if not os.path.exists(css_path):
        print("❌ Błąd: Nie znaleziono pliku CSS")
        return False
    
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # 1. Sprawdź czy jest reguła dla szerokości sidebara 200px
    width_pattern = r'@media.*max-width:\s*768px.*\[data-testid="stSidebar"\].*width:\s*200px\s*!important'
    has_sidebar_width = bool(re.search(width_pattern, css_content, re.DOTALL))
    print(f"✅ Reguła szerokości sidebara 200px: {'TAK' if has_sidebar_width else '❌ NIE'}")
    
    # 2. Sprawdź czy jest reguła dla stSidebar > div
    div_pattern = r'\[data-testid="stSidebar"\]\s*>\s*div.*width:\s*200px\s*!important'
    has_div_width = bool(re.search(div_pattern, css_content, re.DOTALL))
    print(f"✅ Reguła szerokości dla div wewnętrznego: {'TAK' if has_div_width else '❌ NIE'}")
    
    # 3. Sprawdź czy tekst nie jest obcinany (white-space: normal)
    normal_text_pattern = r'white-space:\s*normal\s*!important'
    has_normal_text = bool(re.search(normal_text_pattern, css_content))
    print(f"✅ White-space normal (bez obcinania): {'TAK' if has_normal_text else '❌ NIE'}")
    
    # 4. Sprawdź czy overflow jest visible
    visible_overflow_pattern = r'overflow:\s*visible\s*!important'
    has_visible_overflow = bool(re.search(visible_overflow_pattern, css_content))
    print(f"✅ Overflow visible: {'TAK' if has_visible_overflow else '❌ NIE'}")
    
    # 5. Sprawdź czy text-overflow jest unset
    unset_text_overflow_pattern = r'text-overflow:\s*unset\s*!important'
    has_unset_text_overflow = bool(re.search(unset_text_overflow_pattern, css_content))
    print(f"✅ Text-overflow unset: {'TAK' if has_unset_text_overflow else '❌ NIE'}")
    
    # 6. Sprawdź czy przyciski mają min-height
    min_height_pattern = r'min-height:\s*40px\s*!important'
    has_min_height = bool(re.search(min_height_pattern, css_content))
    print(f"✅ Min-height dla przycisków: {'TAK' if has_min_height else '❌ NIE'}")
    
    # 7. Sprawdź czy jest dostosowanie main content
    main_content_pattern = r'\.main\s+\.block-container.*padding-left:\s*1rem'
    has_main_content = bool(re.search(main_content_pattern, css_content, re.DOTALL))
    print(f"✅ Dostosowanie main content: {'TAK' if has_main_content else '❌ NIE'}")
    
    # 8. Sprawdź czy są reguły przywracające normalny wygląd na tabletach
    tablet_restore_pattern = r'@media.*min-width:\s*769px.*max-width:\s*1024px.*width:\s*auto\s*!important'
    has_tablet_restore = bool(re.search(tablet_restore_pattern, css_content, re.DOTALL))
    print(f"✅ Przywracanie normalnego wyglądu na tabletach: {'TAK' if has_tablet_restore else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [
        has_sidebar_width,
        has_div_width,
        has_normal_text,
        has_visible_overflow,
        has_unset_text_overflow,
        has_min_height,
        has_main_content,
        has_tablet_restore
    ]
    success_count = sum(all_checks)
    
    print("\n" + "=" * 55)
    print(f"📊 Wynik testu: {success_count}/8 sprawdzeń zaliczonych")
    
    if success_count >= 6:
        print("🎉 SUKCES: Sidebar mobilny powinien być prawidłowo dostosowany!")
        print("📏 Szerokość: 200px (czytelne nazwy)")
        print("📱 Responsywność: Przywracanie normalnego wyglądu na większych ekranach")
        return True
    else:
        print("⚠️  UWAGA: Niektóre sprawdzenia nie przeszły. Sprawdź implementację.")
        return False

if __name__ == "__main__":
    # Zmień katalog na główny katalog aplikacji
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    test_fixed_mobile_sidebar()
