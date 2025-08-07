#!/usr/bin/env python3
"""
Test renderowania sekcji Praktyka w lekcji B1C1L1
"""

import json
import os
import sys

# Dodaj główny katalog do ścieżki
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_practical_exercises_structure():
    """Testuje czy sekcja practical_exercises ma poprawną strukturę"""
    
    # Załaduj lekcję B1C1L1
    lesson_path = "data/lessons/B1C1L1.json"
    
    if not os.path.exists(lesson_path):
        print(f"❌ BŁĄD: Nie znaleziono pliku lekcji: {lesson_path}")
        return False
    
    try:
        with open(lesson_path, 'r', encoding='utf-8') as f:
            lesson = json.load(f)
    except Exception as e:
        print(f"❌ BŁĄD podczas wczytywania JSON: {e}")
        return False
    
    print("📚 Testowanie struktury sekcji Praktyka...")
    
    # Sprawdź czy istnieje sections
    if 'sections' not in lesson:
        print("❌ BŁĄD: Brak klucza 'sections' w lekcji")
        return False
    
    # Sprawdź czy istnieje practical_exercises
    if 'practical_exercises' not in lesson['sections']:
        print("❌ BŁĄD: Brak klucza 'practical_exercises' w sections")
        return False
    
    practical_data = lesson['sections']['practical_exercises']
    print(f"✅ Znaleziono sekcję practical_exercises")
    
    # Sprawdź dostępne klucze w practical_exercises
    available_keys = list(practical_data.keys())
    print(f"📋 Dostępne klucze w practical_exercises: {available_keys}")
    
    # Sprawdź czy są exercises
    if 'exercises' in practical_data:
        exercises = practical_data['exercises']
        print(f"✅ Znaleziono 'exercises'")
        print(f"   - Tytuł: {exercises.get('title', 'Brak tytułu')}")
        print(f"   - Opis: {exercises.get('description', 'Brak opisu')}")
        
        if 'sections' in exercises:
            print(f"   - Liczba sekcji w exercises: {len(exercises['sections'])}")
            for i, section in enumerate(exercises['sections']):
                print(f"     {i+1}. {section.get('title', 'Brak tytułu')}")
        else:
            print("   ⚠️ Brak sekcji w exercises")
    else:
        print("❌ Brak klucza 'exercises' w practical_exercises")
    
    # Sprawdź czy jest closing_quiz
    if 'closing_quiz' in practical_data:
        closing_quiz = practical_data['closing_quiz']
        print(f"✅ Znaleziono 'closing_quiz'")
        print(f"   - Tytuł: {closing_quiz.get('title', 'Brak tytułu')}")
        print(f"   - Opis: {closing_quiz.get('description', 'Brak opisu')}")
        
        if 'questions' in closing_quiz:
            print(f"   - Liczba pytań: {len(closing_quiz['questions'])}")
            for i, question in enumerate(closing_quiz['questions']):
                print(f"     {i+1}. {question.get('question', 'Brak pytania')[:50]}...")
        else:
            print("   ⚠️ Brak pytań w closing_quiz")
    else:
        print("❌ Brak klucza 'closing_quiz' w practical_exercises")
    
    return True

def test_tabs_simulation():
    """Symuluje logikę tworzenia zakładek z views/lesson.py"""
    
    lesson_path = "data/lessons/B1C1L1.json"
    
    with open(lesson_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    
    practical_data = lesson['sections']['practical_exercises']
    
    print("\n🔧 Symulacja logiki tworzenia zakładek...")
    
    # Przygotuj zakładki dla różnych typów ćwiczeń (kod z views/lesson.py)
    available_tabs = []
    tab_keys = []
    sub_tabs_data = {}
    
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
    
    # Backward compatibility - stara struktura bezpośrednia
    if 'reflection' in practical_data:
        available_tabs.append("📝 Refleksja")
        tab_keys.append('reflection')
        sub_tabs_data['reflection'] = practical_data['reflection']
        print("✅ Dodano zakładkę: 📝 Refleksja")
    
    if 'application' in practical_data:
        available_tabs.append("🚀 Zadania Praktyczne")
        tab_keys.append('application')
        sub_tabs_data['application'] = practical_data['application']
        print("✅ Dodano zakładkę: 🚀 Zadania Praktyczne")
    
    print(f"\n📋 Finalne zakładki:")
    print(f"   - Liczba zakładek: {len(available_tabs)}")
    print(f"   - Nazwy: {available_tabs}")
    print(f"   - Klucze: {tab_keys}")
    
    if len(available_tabs) == 0:
        print("❌ PROBLEM: Brak dostępnych zakładek!")
        return False
    
    # Sprawdź zawartość każdej zakładki
    print(f"\n🔍 Analiza zawartości zakładek:")
    for tab_key, tab_title in zip(tab_keys, available_tabs):
        print(f"\n📂 Zakładka: {tab_title} (klucz: {tab_key})")
        tab_data = sub_tabs_data[tab_key]
        
        if tab_key == 'closing_quiz':
            print(f"   🎓 Quiz końcowy - specjalna obsługa")
            if 'questions' in tab_data:
                print(f"   - Liczba pytań: {len(tab_data['questions'])}")
            else:
                print(f"   ❌ Brak pytań w quizie!")
        else:
            # Standardowa obsługa dla innych zakładek
            if 'description' in tab_data:
                print(f"   - Opis: {tab_data['description']}")
            
            if 'sections' in tab_data:
                print(f"   - Liczba sekcji: {len(tab_data['sections'])}")
                for i, section in enumerate(tab_data['sections']):
                    title = section.get('title', 'Brak tytułu')
                    print(f"     {i+1}. {title}")
            else:
                print(f"   ❌ Brak sekcji w zakładce!")
    
    return True

def main():
    """Główna funkcja testowa"""
    print("🧪 TEST SEKCJI PRAKTYKA - B1C1L1")
    print("=" * 50)
    
    success = True
    
    # Test 1: Struktura practical_exercises
    if not test_practical_exercises_structure():
        success = False
    
    # Test 2: Symulacja logiki zakładek
    if not test_tabs_simulation():
        success = False
    
    print("\n" + "=" * 50)
    if success:
        print("✅ WSZYSTKIE TESTY PRZESZŁY POMYŚLNIE")
        print("🔍 Sekcja Praktyka powinna być poprawnie renderowana")
    else:
        print("❌ WYKRYTO PROBLEMY")
        print("🔧 Konieczne są poprawki w strukturze danych lub kodzie")
    
    return success

if __name__ == "__main__":
    main()
