#!/usr/bin/env python3
"""
Prosty test menu nawigacji
"""

import os
import sys

# Dodaj ścieżkę
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.append(APP_DIR)

# Test importu
try:
    from utils.components import navigation_menu
    print("✅ Import navigation_menu - OK")
except Exception as e:
    print(f"❌ Błąd importu: {e}")
    exit(1)

# Test kodu źródłowego
import inspect
source = inspect.getsource(navigation_menu)

print("\n📋 ANALIZA MENU:")
print("=" * 40)

# Sprawdź menu_options
lines = source.split('\n')
in_menu = False
menu_items = []

for line in lines:
    if 'menu_options = [' in line:
        in_menu = True
        continue
    if in_menu:
        if ']' in line and '{' not in line:
            break
        if '"id":' in line:
            # Wyodrębnij id i name
            if '"id": "' in line:
                id_part = line.split('"id": "')[1].split('"')[0]
                menu_items.append(id_part)

print(f"Znalezione zakładki: {len(menu_items)}")
for i, item in enumerate(menu_items, 1):
    print(f"  {i}. {item}")

if 'degen_explorer' in menu_items:
    print(f"\n❌ BŁĄD: 'degen_explorer' nadal w menu!")
else:
    print(f"\n✅ 'degen_explorer' został usunięty z menu")

print(f"\n🎯 Menu powinno mieć 5 zakładek:")
expected = ["dashboard", "lesson", "skills", "shop", "profile"]
print(f"Oczekiwane: {expected}")
print(f"Aktualne:   {menu_items}")

if menu_items == expected:
    print("✅ Menu jest poprawne!")
else:
    print("❌ Menu nie jest zgodne z oczekiwaniami")
    
print("\n" + "=" * 40)
