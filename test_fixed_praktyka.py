#!/usr/bin/env python3
"""
Test ostatecznej naprawy sekcji Praktyka
"""

import json
import os
import sys

def test_fixed_practical_section():
    """Testuje czy naprawiona sekcja practical_exercises działa"""
    
    print("🧪 TEST NAPRAWIONEJ SEKCJI PRAKTYKA")
    print("=" * 50)
    
    # Załaduj lekcję B1C1L1
    lesson_path = "data/lessons/B1C1L1.json"
    
    with open(lesson_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    
    practical_data = lesson['sections']['practical_exercises']
    
    # Symuluj logikę z naprawionego views/lesson.py
    available_tabs = []
    tab_keys = []
    sub_tabs_data = {}
    
    print("📋 Symulacja nowej logiki renderowania...")
    
    # Nowa struktura z 'exercises' i 'closing_quiz'
    if 'exercises' in practical_data:
        available_tabs.append("🎯 Ćwiczenia")
        tab_keys.append('exercises')
        sub_tabs_data['exercises'] = practical_data['exercises']
        print("✅ Dodano zakładkę: 🎯 Ćwiczenia")
    
    if 'closing_quiz' in practical_data:
        available_tabs.append("🎓 Quiz końcowy")
        tab_keys.append('closing_quiz')
        sub_tabs_data['closing_quiz'] = practical_data['closing_quiz']
        print("✅ Dodano zakładkę: 🎓 Quiz końcowy")
    
    # Sprawdź warunek renderowania
    has_tabs_key = 'tabs' in practical_data
    should_render = len(available_tabs) > 0 and not has_tabs_key
    
    print(f"\n📊 Analiza warunków renderowania:")
    print(f"   - Liczba dostępnych zakładek: {len(available_tabs)}")
    print(f"   - Czy ma klucz 'tabs': {has_tabs_key}")
    print(f"   - Czy powinien renderować: {should_render}")
    
    if should_render:
        print("\n✅ SUKCES - Logika renderowania ZOSTANIE URUCHOMIONA")
        print("   Sekcja Praktyka będzie wyświetlać zakładki:")
        for i, tab_title in enumerate(available_tabs):
            print(f"   {i+1}. {tab_title}")
        
        # Sprawdź zawartość każdej zakładki
        print("\n🔍 Sprawdzanie zawartości zakładek:")
        for tab_key, tab_title in zip(tab_keys, available_tabs):
            print(f"\n📂 {tab_title} (klucz: {tab_key}):")
            tab_data = sub_tabs_data[tab_key]
            
            if tab_key == 'closing_quiz':
                if 'questions' in tab_data:
                    print(f"   ✅ Quiz z {len(tab_data['questions'])} pytaniami")
                else:
                    print(f"   ❌ Brak pytań w quizie")
            else:
                if 'sections' in tab_data:
                    print(f"   ✅ {len(tab_data['sections'])} sekcji do wyświetlenia")
                    for i, section in enumerate(tab_data['sections']):
                        title = section.get('title', 'Brak tytułu')
                        print(f"      {i+1}. {title}")
                else:
                    print(f"   ❌ Brak sekcji do wyświetlenia")
        
        return True
    else:
        print("\n❌ PROBLEM - Logika renderowania NIE ZOSTANIE URUCHOMIONA")
        if len(available_tabs) == 0:
            print("   Przyczyna: Brak dostępnych zakładek")
        if has_tabs_key:
            print("   Przyczyna: Wykryto starą strukturę 'tabs'")
        return False

def main():
    success = test_fixed_practical_section()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 TEST ZAKOŃCZONY POMYŚLNIE")
        print("✅ Sekcja Praktyka powinna teraz działać poprawnie")
        print("💡 W aplikacji powinieneś zobaczyć zakładki: 'Ćwiczenia' i 'Quiz końcowy'")
    else:
        print("❌ TEST NIEUDANY")
        print("🔧 Potrzebne są dodatkowe poprawki")
    
    return success

if __name__ == "__main__":
    main()
