#!/usr/bin/env python3
"""
Test struktury lekcji po konwersji
"""

import json

def test_converted_lesson():
    """Test skonwertowanej lekcji B1C1L1"""
    
    print("🧪 Test skonwertowanej lekcji B1C1L1")
    print("=" * 50)
    
    try:
        with open('data/lessons/B1C1L1.json', 'r', encoding='utf-8') as f:
            lesson = json.load(f)
        print("✅ Odczyt pliku JSON - SUCCESS")
    except Exception as e:
        print(f"❌ Błąd odczytu JSON: {e}")
        return False
    
    print(f"\n📖 Tytuł lekcji: {lesson.get('title', 'Brak tytułu')}")
    
    # Sprawdź strukturę sekcji
    sections = lesson.get('sections', {})
    print(f"\n📦 Dostępne sekcje:")
    for section_name in sections.keys():
        print(f"   - {section_name}")
    
    # Sprawdź czy ma nową strukturę practical_exercises
    has_practical_exercises = 'practical_exercises' in sections
    has_old_reflection = 'reflection' in sections
    has_old_application = 'application' in sections
    
    print(f"\n🔍 Analiza struktury:")
    print(f"   practical_exercises: {'✅' if has_practical_exercises else '❌'}")
    print(f"   old reflection:      {'❌ (old format)' if has_old_reflection else '✅'}")
    print(f"   old application:     {'❌ (old format)' if has_old_application else '✅'}")
    
    if has_practical_exercises:
        practical = sections['practical_exercises']
        print(f"\n📋 Zawartość practical_exercises:")
        for key in practical.keys():
            print(f"   - {key}")
            
        # Sprawdź czy ma pod-sekcje
        has_reflection = 'reflection' in practical
        has_application = 'application' in practical
        has_closing_quiz = 'closing_quiz' in practical
        
        print(f"\n🎯 Pod-sekcje praktyki:")
        print(f"   reflection:    {'✅' if has_reflection else '❌'}")
        print(f"   application:   {'✅' if has_application else '❌'}")
        print(f"   closing_quiz:  {'✅' if has_closing_quiz else '❌'}")
    
    # Symuluj step_order jak w aplikacji
    available_steps = []
    
    if 'intro' in lesson or 'sections' in lesson:
        available_steps.append('intro')
    
    if 'learning' in sections:
        available_steps.append('content')
    
    if 'practical_exercises' in sections:
        available_steps.append('practical_exercises')
    elif 'reflection' in sections or 'application' in sections:
        if 'reflection' in sections:
            available_steps.append('reflection')
        if 'application' in sections:
            available_steps.append('application')
    
    available_steps.append('summary')
    
    step_names = {
        'intro': 'Wprowadzenie',
        'content': 'Nauka',
        'practical_exercises': 'Praktyka',
        'reflection': 'Refleksja',
        'application': 'Zadania praktyczne',
        'summary': 'Podsumowanie'
    }
    
    print(f"\n🔗 Przewidywana nawigacja ({len(available_steps)} etapów):")
    for i, step in enumerate(available_steps, 1):
        display_name = step_names.get(step, step.capitalize())
        print(f"   {i}. {step} → {display_name}")
    
    if len(available_steps) == 4 and has_practical_exercises:
        print(f"\n🎉 SUKCES! Lekcja ma strukturę 4-etapową z practical_exercises!")
        return True
    else:
        print(f"\n⚠️  Lekcja ma {len(available_steps)} etapów (oczekiwano 4)")
        return False

if __name__ == "__main__":
    test_converted_lesson()
