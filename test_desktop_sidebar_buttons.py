#!/usr/bin/env python3
"""
Test sprawdzający czy przyciski sidebar w wersji desktop są przywrócone do normalnych rozmiarów
"""

import os
import re

def test_desktop_sidebar_buttons():
    """Sprawdza czy przyciski sidebar w wersji desktop mają normalne rozmiary"""
    
    print("🖥️  Test normalnych rozmiarów przycisków sidebar na desktop")
    print("=" * 60)
    
    # Sprawdź CSS
    css_path = "static/css/style.css"
    if not os.path.exists(css_path):
        print("❌ Błąd: Nie znaleziono pliku CSS")
        return False
    
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # 1. Sprawdź czy jest reguła dla desktop (@media min-width: 769px)
    desktop_media_pattern = r'@media\s*\(\s*min-width:\s*769px\s*\).*\.stSidebar.*button'
    has_desktop_media = bool(re.search(desktop_media_pattern, css_content, re.DOTALL))
    print(f"✅ Media query dla desktop (≥769px): {'TAK' if has_desktop_media else '❌ NIE'}")
    
    # 2. Sprawdź czy font-size jest inherit na desktop
    inherit_font_pattern = r'@media.*min-width:\s*769px.*font-size:\s*inherit\s*!important'
    has_inherit_font = bool(re.search(inherit_font_pattern, css_content, re.DOTALL))
    print(f"✅ Font-size inherit na desktop: {'TAK' if has_inherit_font else '❌ NIE'}")
    
    # 3. Sprawdź czy padding jest większy na desktop
    desktop_padding_pattern = r'@media.*min-width:\s*769px.*padding:\s*12px\s*16px\s*!important'
    has_desktop_padding = bool(re.search(desktop_padding_pattern, css_content, re.DOTALL))
    print(f"✅ Większy padding na desktop (12px 16px): {'TAK' if has_desktop_padding else '❌ NIE'}")
    
    # 4. Sprawdź czy min-height jest normalny na desktop
    desktop_height_pattern = r'@media.*min-width:\s*769px.*min-height:\s*44px\s*!important'
    has_desktop_height = bool(re.search(desktop_height_pattern, css_content, re.DOTALL))
    print(f"✅ Normalny min-height na desktop (44px): {'TAK' if has_desktop_height else '❌ NIE'}")
    
    # 5. Sprawdź czy white-space jest normal na desktop
    normal_whitespace_pattern = r'@media.*min-width:\s*769px.*white-space:\s*normal\s*!important'
    has_normal_whitespace = bool(re.search(normal_whitespace_pattern, css_content, re.DOTALL))
    print(f"✅ White-space normal na desktop: {'TAK' if has_normal_whitespace else '❌ NIE'}")
    
    # 6. Sprawdź czy są reguły dla dużych ekranów (≥1025px) z przywracaniem
    large_screen_pattern = r'@media.*min-width:\s*1025px.*\.stSidebar.*button.*font-size:\s*inherit'
    has_large_screen = bool(re.search(large_screen_pattern, css_content, re.DOTALL))
    print(f"✅ Przywracanie na dużych ekranach (≥1025px): {'TAK' if has_large_screen else '❌ NIE'}")
    
    # 7. Sprawdź czy mobile reguły są ograniczone do max-width: 768px
    mobile_limit_pattern = r'@media.*max-width:\s*768px.*font-size:\s*0\.85rem'
    has_mobile_limit = bool(re.search(mobile_limit_pattern, css_content, re.DOTALL))
    print(f"✅ Mobile reguły ograniczone do ≤768px: {'TAK' if has_mobile_limit else '❌ NIE'}")
    
    # 8. Sprawdź czy tablet ma przywracanie (769px-1024px)
    tablet_restore_pattern = r'@media.*min-width:\s*769px.*max-width:\s*1024px.*font-size:\s*inherit'
    has_tablet_restore = bool(re.search(tablet_restore_pattern, css_content, re.DOTALL))
    print(f"✅ Przywracanie na tabletach (769-1024px): {'TAK' if has_tablet_restore else '❌ NIE'}")
    
    # Podsumowanie
    all_checks = [
        has_desktop_media,
        has_inherit_font,
        has_desktop_padding,
        has_desktop_height,
        has_normal_whitespace,
        has_large_screen,
        has_mobile_limit,
        has_tablet_restore
    ]
    success_count = sum(all_checks)
    
    print("\n" + "=" * 60)
    print(f"📊 Wynik testu: {success_count}/8 sprawdzeń zaliczonych")
    
    if success_count >= 6:
        print("🎉 SUKCES: Przyciski sidebar na desktop powinny mieć normalne rozmiary!")
        print("📱 Mobile: Małe przyciski (≤768px)")
        print("🖥️  Desktop: Normalne przyciski (≥769px)")
        return True
    else:
        print("⚠️  UWAGA: Niektóre sprawdzenia nie przeszły. Sprawdź implementację.")
        return False

if __name__ == "__main__":
    # Zmień katalog na główny katalog aplikacji
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    test_desktop_sidebar_buttons()
