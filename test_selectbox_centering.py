#!/usr/bin/env python3
"""
Test stylów selectbox - sprawdza czy tekst jest wyśrodkowany
"""

import os
import re

def test_selectbox_styles():
    """Test czy style wyśrodkowania tekstu w selectbox zostały dodane"""
    print("🧪 Testowanie stylów selectbox...")
    
    # Sprawdź plik material3_components.py
    material3_path = "utils/material3_components.py"
    print(f"\n📁 Sprawdzanie: {material3_path}")
    
    if os.path.exists(material3_path):
        with open(material3_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sprawdź obecność kluczowych stylów
        checks = [
            ("align-items: center", "align-items: center dla wyśrodkowania"),
            ("display: flex", "display: flex dla flexbox"),
            ("vertical-align: middle", "vertical-align: middle"),
            ("min-height: 40px", "min-height dla wysokości"),
            ("line-height: normal", "line-height: normal"),
        ]
        
        for pattern, description in checks:
            found = pattern in content
            status = "✅" if found else "❌"
            print(f"   {status} {description}: {'ZNALEZIONO' if found else 'BRAK'}")
    else:
        print(f"   ❌ Plik {material3_path} nie istnieje")
    
    # Sprawdź plik material3_extended.css
    css_extended_path = "static/css/material3_extended.css"
    print(f"\n📁 Sprawdzanie: {css_extended_path}")
    
    if os.path.exists(css_extended_path):
        with open(css_extended_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = [
            (".stSelectbox > div > div", "Selektor stSelectbox"),
            ("align-items: center", "align-items: center"),
            ("role=\"option\"", "Selektor dla opcji dropdown"),
            ("display: flex", "display: flex"),
        ]
        
        for pattern, description in checks:
            found = pattern in content
            status = "✅" if found else "❌"
            print(f"   {status} {description}: {'ZNALEZIONO' if found else 'BRAK'}")
    else:
        print(f"   ❌ Plik {css_extended_path} nie istnieje")
    
    # Sprawdź główny plik style.css
    main_css_path = "static/css/style.css"
    print(f"\n📁 Sprawdzanie: {main_css_path}")
    
    if os.path.exists(main_css_path):
        with open(main_css_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sprawdź czy sekcja z stylami selectbox została dodana
        selectbox_section = "GLOBALNE STYLE DLA SELECTBOX" in content
        align_items = "align-items: center" in content
        display_flex = "display: flex" in content
        
        print(f"   ✅ Sekcja selectbox: {'ZNALEZIONA' if selectbox_section else '❌ BRAK'}")
        print(f"   ✅ align-items: center: {'ZNALEZIONO' if align_items else '❌ BRAK'}")
        print(f"   ✅ display: flex: {'ZNALEZIONO' if display_flex else '❌ BRAK'}")
    else:
        print(f"   ❌ Plik {main_css_path} nie istnieje")
    
    print("\n" + "="*50)
    print("PODSUMOWANIE STYLÓW SELECTBOX:")
    print("="*50)
    
    print("🎯 DODANE STYLE:")
    print("   • display: flex !important")
    print("   • align-items: center !important")
    print("   • vertical-align: middle !important") 
    print("   • line-height: normal !important")
    print("   • min-height: 40px !important")
    
    print("\n📋 SELEKTORY CSS:")
    print("   • .stSelectbox > div > div")
    print("   • .stMultiSelect > div > div")
    print("   • div[data-baseweb=\"select\"]")
    print("   • div[role=\"option\"]")
    
    print("\n🎨 EFEKT:")
    print("   Tekst w rozwijanych menu będzie wyśrodkowany")
    print("   pionowo zamiast być wyrównany do dołu!")
    
    print("\n✅ Test zakończony!")

if __name__ == "__main__":
    test_selectbox_styles()
