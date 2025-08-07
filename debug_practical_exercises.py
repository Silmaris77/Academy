#!/usr/bin/env python3
"""
Debug sekcji practical_exercises - sprawdź dlaczego zakładki się nie wyświetlają
"""

import json
import os
import sys

def debug_practical_exercises():
    """Debug logiki practical_exercises"""
    
    # Załaduj lekcję
    lesson_path = "data/lessons/B1C1L1.json"
    
    with open(lesson_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    
    practical_data = lesson['sections']['practical_exercises']
    
    print("🔍 DEBUG SEKCJI PRACTICAL_EXERCISES")
    print("=" * 50)
    
    # Symuluj logikę z views/lesson.py
    available_tabs = []
    tab_keys = []
    sub_tabs_data = {}
    
    print("📋 Sprawdzam dostępne klucze w practical_data:")
    for key in practical_data.keys():
        print(f"  - {key}")
    
    print("\n🔧 Testuję logikę tworzenia zakładek...")
    
    # Test 1: Nowa struktura z 'exercises' i 'closing_quiz'
    print("\n1️⃣ Sprawdzam 'exercises':")
    if 'exercises' in practical_data:
        available_tabs.append("🎯 Ćwiczenia")
        tab_keys.append('exercises')
        sub_tabs_data['exercises'] = practical_data['exercises']
        print("   ✅ Dodano zakładkę: 🎯 Ćwiczenia")
    else:
        print("   ❌ Brak klucza 'exercises'")
    
    print("\n2️⃣ Sprawdzam 'closing_quiz':")
    if 'closing_quiz' in practical_data:
        available_tabs.append("🎓 Quiz końcowy")
        tab_keys.append('closing_quiz')
        sub_tabs_data['closing_quiz'] = practical_data['closing_quiz']
        print("   ✅ Dodano zakładkę: 🎓 Quiz końcowy")
    else:
        print("   ❌ Brak klucza 'closing_quiz'")
    
    # Test 2: Backward compatibility
    print("\n3️⃣ Sprawdzam backward compatibility:")
    if 'reflection' in practical_data:
        available_tabs.append("📝 Refleksja")
        tab_keys.append('reflection')
        sub_tabs_data['reflection'] = practical_data['reflection']
        print("   ✅ Dodano zakładkę: 📝 Refleksja")
    else:
        print("   ℹ️ Brak klucza 'reflection' (OK - nowa struktura)")
    
    if 'application' in practical_data:
        available_tabs.append("🚀 Zadania Praktyczne")
        tab_keys.append('application')
        sub_tabs_data['application'] = practical_data['application']
        print("   ✅ Dodano zakładkę: 🚀 Zadania Praktyczne")
    else:
        print("   ℹ️ Brak klucza 'application' (OK - nowa struktura)")
    
    # Test 3: Stara struktura z 'tabs'
    print("\n4️⃣ Sprawdzam starą strukturę z 'tabs':")
    if 'tabs' in practical_data:
        print("   ❌ Znaleziono starą strukturę 'tabs' - może to powodować konflikty")
        old_tabs = practical_data['tabs']
        print(f"   Klucze w 'tabs': {list(old_tabs.keys())}")
    else:
        print("   ✅ Brak starej struktury 'tabs' (OK)")
    
    # Wyniki finalne
    print("\n📊 WYNIKI FINALNE:")
    print(f"   Liczba dostępnych zakładek: {len(available_tabs)}")
    print(f"   Nazwy zakładek: {available_tabs}")
    print(f"   Klucze zakładek: {tab_keys}")
    
    if len(available_tabs) == 0:
        print("\n❌ PROBLEM: Brak dostępnych zakładek!")
        print("   To wyjaśnia dlaczego sekcja Praktyka jest pusta")
        return False
    elif len(available_tabs) > 0:
        print(f"\n✅ ZAKŁADKI SĄ DOSTĘPNE ({len(available_tabs)} zakładek)")
        print("   Problem może być w renderowaniu lub emoji")
        
        # Sprawdź zawartość każdej zakładki
        print("\n🔍 Sprawdzam zawartość zakładek:")
        for tab_key, tab_title in zip(tab_keys, available_tabs):
            print(f"\n📂 {tab_title} (klucz: {tab_key}):")
            tab_data = sub_tabs_data[tab_key]
            
            if 'sections' in tab_data:
                print(f"   - Liczba sekcji: {len(tab_data['sections'])}")
            elif 'questions' in tab_data:
                print(f"   - Liczba pytań: {len(tab_data['questions'])}")
            else:
                print(f"   - Inne klucze: {list(tab_data.keys())}")
        
        return True
    
    return False

def main():
    debug_practical_exercises()

if __name__ == "__main__":
    main()
