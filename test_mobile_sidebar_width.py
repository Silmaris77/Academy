#!/usr/bin/env python3
"""
Test sprawdzający czy sidebar w wersji mobilnej jest o połowę węższy
"""

import os
import re

def test_mobile_sidebar_width():
    """Sprawdza czy implementacja węższego sidebara w wersji mobilnej jest prawidłowa"""
    
    print("📱 Test węższego sidebara w wersji mobilnej")
    print("=" * 50)
    
    # Sprawdź CSS
    css_path = "static/css/style.css"
    if not os.path.exists(css_path):
        print("❌ Błąd: Nie znaleziono pliku CSS")
        return False
    
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # 1. Sprawdź czy jest reguła dla szerokości sidebara 150px
    width_pattern = r'@media.*max-width:\s*768px.*\[data-testid="stSidebar"\].*width:\s*150px\s*!important'
    has_sidebar_width = bool(re.search(width_pattern, css_content, re.DOTALL))
    print(f"✅ Reguła szerokości sidebara 150px: {'TAK' if has_sidebar_width else '❌ NIE'}")
    
    # 2. Sprawdź czy jest min-width dla sidebara
    min_width_pattern = r'min-width:\s*150px\s*!important'
    has_min_width = bool(re.search(min_width_pattern, css_content))
    print(f"✅ Reguła min-width sidebara: {'TAK' if has_min_width else '❌ NIE'}")
    
    # 3. Sprawdź czy jest max-width dla sidebara
    max_width_pattern = r'max-width:\s*150px\s*!important'
    has_max_width = bool(re.search(max_width_pattern, css_content))
    print(f"✅ Reguła max-width sidebara: {'TAK' if has_max_width else '❌ NIE'}")
    
    # 4. Sprawdź czy są reguły dla mniejszego tekstu w nagłówku
    header_text_pattern = r'\.stSidebar.*\.stMarkdown.*h3.*font-size:\s*0\.9rem'
    has_header_text = bool(re.search(header_text_pattern, css_content, re.DOTALL))
    print(f"✅ Mniejszy tekst nagłówka sidebara: {'TAK' if has_header_text else '❌ NIE'}")
    
    # 5. Sprawdź czy są reguły dla mniejszych przycisków
    button_text_pattern = r'\.stSidebar.*button.*font-size:\s*0\.8rem'
    has_button_text = bool(re.search(button_text_pattern, css_content, re.DOTALL))
    print(f"✅ Mniejszy tekst przycisków: {'TAK' if has_button_text else '❌ NIE'}")
    
    # 6. Sprawdź czy są reguły ellipsis dla długiego tekstu
    ellipsis_pattern = r'text-overflow:\s*ellipsis'
    has_ellipsis = bool(re.search(ellipsis_pattern, css_content))
    print(f"✅ Text overflow ellipsis: {'TAK' if has_ellipsis else '❌ NIE'}")
    
    # 7. Sprawdź czy jest white-space: nowrap
    nowrap_pattern = r'white-space:\s*nowrap'
    has_nowrap = bool(re.search(nowrap_pattern, css_content))
    print(f"✅ White-space nowrap: {'TAK' if has_nowrap else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [
        has_sidebar_width,
        has_min_width,
        has_max_width,
        has_header_text,
        has_button_text,
        has_ellipsis,
        has_nowrap
    ]
    success_count = sum(all_checks)
    
    print("\n" + "=" * 50)
    print(f"📊 Wynik testu: {success_count}/7 sprawdzeń zaliczonych")
    
    if success_count >= 6:
        print("🎉 SUKCES: Sidebar w wersji mobilnej powinien być o połowę węższy!")
        return True
    else:
        print("⚠️  UWAGA: Niektóre sprawdzenia nie przeszły. Sprawdź implementację.")
        return False

if __name__ == "__main__":
    # Zmień katalog na główny katalog aplikacji
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    test_mobile_sidebar_width()
