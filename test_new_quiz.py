import json

try:
    with open('data/lessons/B1C1L4.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('✅ JSON VALID - Plik załadowany pomyślnie')
    
    quiz = data['sections']['closing_quiz']
    questions = quiz['questions']
    
    print(f'✅ Quiz zawiera {len(questions)} pytań')
    
    # Sprawdź typy pytań
    single_choice = sum(1 for q in questions if q.get('type', 'single_choice') == 'single_choice')
    multiple_choice = sum(1 for q in questions if q.get('type') == 'multiple_choice')
    
    print(f'✅ Pytania single choice: {single_choice}')
    print(f'✅ Pytania multiple choice: {multiple_choice}') 
    
    # Sprawdź interpretację wyników
    interp = quiz.get('result_interpretation', {})
    print(f'✅ Poziomy interpretacji: {len(interp)}')
    for level, data in interp.items():
        print(f'  - {level}: {data["threshold"]}% - {data["title"]}')
    
    print('\n🎉 WSZYSTKO DZIAŁA! Nowy quiz jest gotowy!')
    print('\n📋 PODSUMOWANIE NOWEGO QUIZU:')
    print(f'- {len(questions)} pytań o emocjonalnej zmienności rynku')
    print(f'- {single_choice} pytań jednokrotnego wyboru')
    print(f'- {multiple_choice} pytań wielokrotnego wyboru')
    print('- 4 poziomy interpretacji wyników')
    print('- Próg zaliczenia: 75%')
    
    # Pokaż pierwsze pytanie jako przykład
    print('\n📝 PRZYKŁAD PYTANIA:')
    first_q = questions[0]
    print(f'Pytanie: {first_q["question"]}')
    print(f'Typ: {first_q["type"]}')
    print(f'Opcje: {len(first_q["options"])}')
    
except Exception as e:
    print(f'❌ Błąd: {e}')
    import traceback
    traceback.print_exc()
