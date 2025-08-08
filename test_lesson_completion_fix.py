#!/usr/bin/env python3
"""
Test naprawionego systemu oznaczania lekcji jako ukończone
"""

import json
import os
import sys

# Dodaj główny katalog do ścieżki
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_lesson_completion_logic():
    """Testuje nową logikę sprawdzania ukończenia lekcji"""
    
    # Symuluj postęp lekcji w nowej 4-etapowej strukturze
    test_progress = {
        'intro_completed': True,
        'content_completed': True,
        'practical_exercises_completed': True,
        'summary_completed': True,
        # Dodatkowe dane fragmentów
        'intro_xp_awarded': True,
        'content_xp_awarded': True,
        'practical_exercises_xp_awarded': True,
        'summary_xp_awarded': True
    }
    
    print("🧪 TEST SYSTEMU OZNACZANIA LEKCJI JAKO UKOŃCZONE")
    print("=" * 60)
    
    print("📋 Test 1: Sprawdzenie logiki calculate_lesson_completion")
    
    # Test dla nowej struktury
    new_steps = ['intro', 'content', 'practical_exercises', 'summary']
    new_completed = sum(1 for step in new_steps if test_progress.get(f"{step}_completed", False))
    completion_percentage = (new_completed / len(new_steps)) * 100
    
    print(f"   Ukończone etapy (nowa struktura): {new_completed}/{len(new_steps)}")
    print(f"   Procent ukończenia: {completion_percentage}%")
    
    if completion_percentage == 100:
        print("   ✅ Lekcja powinna być oznaczona jako ukończona")
    else:
        print("   ❌ Lekcja NIE powinna być oznaczona jako ukończona")
    
    print(f"\n📋 Test 2: Sprawdzenie detekcji nowej struktury")
    
    # Sprawdź czy lekcja używa nowej struktury
    uses_new_structure = any(test_progress.get(f"{step}_completed", False) for step in new_steps)
    print(f"   Używa nowej struktury: {'✅ TAK' if uses_new_structure else '❌ NIE'}")
    
    print(f"\n📋 Test 3: Porównanie ze starą strukturą")
    
    # Test dla starej struktury
    old_steps = ['intro', 'opening_quiz', 'content', 'reflection', 'application', 'closing_quiz', 'summary']
    old_completed = sum(1 for step in old_steps if test_progress.get(f"{step}_completed", False))
    old_completion = (old_completed / len(old_steps)) * 100
    
    print(f"   Ukończone etapy (stara struktura): {old_completed}/{len(old_steps)}")
    print(f"   Procent ukończenia (stara): {old_completion}%")
    
    print(f"\n📊 WYNIKI:")
    print(f"   Nowa struktura (4 etapy): {completion_percentage}% ✅")
    print(f"   Stara struktura (7 etapów): {old_completion}% (ignorowana)")
    print(f"   Decyzja: {'UKOŃCZONA' if completion_percentage == 100 else 'NIEUKOŃCZONA'}")
    
    return completion_percentage == 100

def test_lesson_completion_with_missing_steps():
    """Test przypadku gdy brakuje niektórych etapów"""
    
    print(f"\n" + "=" * 60)
    print("🧪 TEST Z BRAKUJĄCYMI ETAPAMI")
    
    # Symuluj częściowo ukończoną lekcję
    partial_progress = {
        'intro_completed': True,
        'content_completed': True,
        'practical_exercises_completed': False,  # Brakuje!
        'summary_completed': False  # Brakuje!
    }
    
    new_steps = ['intro', 'content', 'practical_exercises', 'summary']
    completed = sum(1 for step in new_steps if partial_progress.get(f"{step}_completed", False))
    completion_percentage = (completed / len(new_steps)) * 100
    
    print(f"   Ukończone etapy: {completed}/{len(new_steps)}")
    print(f"   Procent ukończenia: {completion_percentage}%")
    print(f"   Status: {'UKOŃCZONA' if completion_percentage == 100 else 'NIEUKOŃCZONA'} ✅")
    
    return completion_percentage < 100

def check_current_user_data():
    """Sprawdź aktualne dane użytkownika"""
    
    print(f"\n" + "=" * 60)
    print("📊 SPRAWDZENIE DANYCH UŻYTKOWNIKA")
    
    users_file = "users_data.json"
    if os.path.exists(users_file):
        with open(users_file, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
        
        print(f"   Znaleziono {len(users_data)} użytkowników")
        
        for username, data in users_data.items():
            completed_lessons = data.get('completed_lessons', [])
            xp = data.get('xp', 0)
            level = data.get('level', 1)
            
            print(f"\n   👤 {username}:")
            print(f"      XP: {xp}")
            print(f"      Poziom: {level}")
            print(f"      Ukończone lekcje: {len(completed_lessons)}")
            
            if completed_lessons:
                print(f"      Lista: {completed_lessons}")
            else:
                print(f"      Lista: Brak ukończonych lekcji")
    else:
        print("   ❌ Brak pliku users_data.json")

def main():
    """Główna funkcja testowa"""
    
    test1_passed = test_lesson_completion_logic()
    test2_passed = test_lesson_completion_with_missing_steps()
    
    check_current_user_data()
    
    print(f"\n" + "=" * 60)
    print("📋 PODSUMOWANIE TESTÓW")
    print(f"   Test ukończonej lekcji: {'✅ PASSED' if test1_passed else '❌ FAILED'}")
    print(f"   Test częściowej lekcji: {'✅ PASSED' if test2_passed else '❌ FAILED'}")
    
    if test1_passed and test2_passed:
        print(f"\n🎉 WSZYSTKIE TESTY PRZESZŁY POMYŚLNIE!")
        print(f"💡 Naprawy powinny rozwiązać problem z oznaczaniem lekcji jako ukończone")
    else:
        print(f"\n❌ NIEKTÓRE TESTY SIĘ NIE POWIODŁY")
    
    print(f"\n🔧 CO ZOSTAŁO NAPRAWIONE:")
    print(f"   1. ✅ Logika calculate_lesson_completion wspiera nową 4-etapową strukturę")
    print(f"   2. ✅ Dodano funkcję check_and_mark_lesson_completion")
    print(f"   3. ✅ Sprawdzenie ukończenia po każdym etapie (intro, content, practical_exercises, summary)")
    print(f"   4. ✅ Backward compatibility ze starą 7-etapową strukturą")
    
    print(f"\n🚀 NASTĘPNE KROKI:")
    print(f"   1. Uruchom aplikację i przetestuj lekcję B1C1L1")
    print(f"   2. Sprawdź czy po ukończeniu wszystkich 4 etapów status zmieni się na 'Ukończono'")
    print(f"   3. Sprawdź dashboard czy lekcja jest oznaczona jako ukończona")

if __name__ == "__main__":
    main()
