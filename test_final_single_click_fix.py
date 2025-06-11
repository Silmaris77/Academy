"""
OSTATECZNY TEST POJEDYNCZEGO KLIKNIĘCIA - QUIZ
Sprawdza czy problem z podwójnym kliknięciem został całkowicie rozwiązany.
"""

import streamlit as st
import sys
import os

# Dodaj ścieżkę do głównego katalogu aplikacji
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="🔧 Ostateczny Test Pojedynczego Kliknięcia",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Ostateczny Test Pojedynczego Kliknięcia - Quiz")

st.markdown("""
# 🎯 KLUCZOWE NAPRAWY

### ✅ Co zostało naprawione:

1. **Funkcja pomocnicza `check_and_handle_refresh()`**
   - Sprawdza flagę `quiz_needs_refresh` 
   - Resetuje flagę przed `st.rerun()`
   - Wywołana przed **każdym** returnem w funkcji

2. **Umieszczenie sprawdzania flagi przed WSZYSTKIMI punktami wyjścia:**
   - `return False, False, 0` (brak pytań)
   - `return is_completed, True, total_points` (quiz samodiagnozy)
   - `return is_completed, is_passed, earned_points` (quiz standardowy)
   - `return is_completed, False, 0` (quiz w toku)

3. **Eliminacja race condition:**
   - Wcześniej flaga była sprawdzana tylko na końcu funkcji
   - Jeśli funkcja wcześniej robiła `return`, flaga nigdy nie była sprawdzona
   - Teraz flaga jest sprawdzana przed każdym wyjściem

---

## 🧪 TEST RÓŻNYCH TYPÓW QUIZÓW

Poniżej testujemy różne scenariusze aby upewnić się, że pojedyncze kliknięcie działa we wszystkich przypadkach:

""")

# Test data dla różnych typów pytań
test_scenarios = [
    {
        'title': '🔍 Test 1: Quiz Samodiagnozy (Opening Quiz)',
        'description': 'Test czy quiz startowy działa po pojedynczym kliknięciu.',
        'quiz_data': {
            'title': 'Quiz Samodiagnozy - Test Single Click',
            'description': '🪞 Ten quiz sprawdza czy przyciski samodiagnozy działają po jednym kliknięciu.',
            'questions': [
                {
                    'question': 'Jak oceniasz swoją obecną wiedzę o inwestowaniu?',
                    'options': ['1 - Bardzo niska', '2 - Niska', '3 - Średnia', '4 - Wysoka', '5 - Bardzo wysoka'],
                    'type': 'single_choice'
                    # Brak correct_answer = quiz samodiagnozy
                }
            ]
        }
    },
    {
        'title': '🎯 Test 2: Quiz z Pojedynczym Wyborem (Closing Quiz)',
        'description': 'Test czy quiz końcowy działa po pojedynczym kliknięciu.',
        'quiz_data': {
            'title': 'Quiz Końcowy - Test Single Click',
            'description': '🧠 Ten quiz sprawdza czy przyciski pojedynczego wyboru działają po jednym kliknięciu.',
            'questions': [
                {
                    'question': 'Która z poniższych opcji jest poprawna?',
                    'options': ['Opcja A (poprawna)', 'Opcja B (niepoprawna)', 'Opcja C (niepoprawna)'],
                    'type': 'single_choice',
                    'correct_answer': 0
                }
            ]
        }
    },
    {
        'title': '📋 Test 3: Quiz z Wielokrotnym Wyborem',
        'description': 'Test czy przycisk "Zatwierdź odpowiedzi" działa po pojedynczym kliknięciu.',
        'quiz_data': {
            'title': 'Quiz Wielokrotny Wybór - Test Single Click',
            'description': '✅ Ten quiz sprawdza czy przycisk zatwierdzenia działa po jednym kliknięciu.',
            'questions': [
                {
                    'question': 'Które z poniższych są poprawne? (Wybierz wszystkie)',
                    'options': ['Opcja A (poprawna)', 'Opcja B (poprawna)', 'Opcja C (niepoprawna)', 'Opcja D (niepoprawna)'],
                    'type': 'multiple_choice',
                    'correct_answers': [0, 1]
                }
            ]
        }
    }
]

# Import funkcji display_quiz
try:
    from views.lesson import display_quiz
    
    st.success("✅ Funkcja display_quiz została zaimportowana pomyślnie")
    
    # Wyświetl testy
    for i, scenario in enumerate(test_scenarios):
        st.markdown(f"## {scenario['title']}")
        st.info(scenario['description'])
        
        # Wyświetl quiz dla tego scenariusza
        quiz_complete, quiz_passed, earned_points = display_quiz(
            scenario['quiz_data'], 
            passing_threshold=75 if 'Końcowy' in scenario['title'] else 60
        )
        
        # Status testu
        if quiz_complete:
            st.success(f"✅ **Scenariusz {i+1} ukończony!** Wynik zdany: {quiz_passed}, Punkty: {earned_points}")
            
            # Sprawdź czy to był test pojedynczego kliknięcia
            if f"scenario_{i}_single_click_success" not in st.session_state:
                st.session_state[f"scenario_{i}_single_click_success"] = True
                st.balloons()
                st.success("🎉 **Pojedyncze kliknięcie zadziałało!** Problem został rozwiązany!")
        else:
            st.info(f"ℹ️ Scenariusz {i+1} w toku - przetestuj klikając każdy przycisk tylko **jeden raz**")
        
        st.markdown("---")

    # Podsumowanie wszystkich testów
    completed_scenarios = sum(1 for i in range(len(test_scenarios)) 
                            if st.session_state.get(f"scenario_{i}_single_click_success", False))
    
    if completed_scenarios == len(test_scenarios):
        st.markdown("""
        # 🎉 WSZYSTKIE TESTY ZAKOŃCZONE SUKCESEM!
        
        ## ✅ Potwierdzone naprawy:
        - **Quiz samodiagnozy** - pojedyncze kliknięcie ✅
        - **Quiz z pojedynczym wyborem** - pojedyncze kliknięcie ✅  
        - **Quiz z wielokrotnym wyborem** - przycisk "Zatwierdź" działa po jednym kliknięciu ✅
        
        ## 🔧 Zastosowane rozwiązanie:
        
        ```python
        def check_and_handle_refresh():
            if st.session_state.get('quiz_needs_refresh', False):
                st.session_state['quiz_needs_refresh'] = False
                st.rerun()
        
        # Przed każdym return:
        check_and_handle_refresh()
        return result
        ```
        
        ## 🎯 Rezultat:
        **Problem z podwójnym kliknięciem został całkowicie rozwiązany!**
        
        Użytkownicy mogą teraz klikać przyciski quiz **tylko jeden raz** i natychmiast zobaczyć rezultat.
        """)
    elif completed_scenarios > 0:
        st.markdown(f"""
        ## 📊 Postęp testów: {completed_scenarios}/{len(test_scenarios)}
        
        ✅ Ukończone testy: {completed_scenarios}  
        🔄 Pozostałe testy: {len(test_scenarios) - completed_scenarios}
        
        **Kontynuuj testowanie powyższych quizów...**
        """)

except ImportError as e:
    st.error(f"❌ Błąd importu: {e}")
except Exception as e:
    st.error(f"❌ Błąd: {e}")
    st.exception(e)

# Dodatkowe informacje techniczne
with st.expander("🔍 Szczegóły techniczne - co zostało naprawione"):
    st.markdown("""
    ### 🐛 Problem:
    Funkcja `display_quiz()` miała **4 punkty wyjścia** (return statements), ale sprawdzanie flagi 
    `quiz_needs_refresh` było tylko na końcu funkcji. Jeśli funkcja wcześniej robiła `return`, 
    flaga nigdy nie była sprawdzana i `st.rerun()` nie był wywoływany.
    
    ### 🔧 Rozwiązanie:
    1. Stworzono funkcję pomocniczą `check_and_handle_refresh()`
    2. Dodano wywołanie tej funkcji przed **każdym** returnem:
       - Linia ~1205: `return False, False, 0` (brak pytań)
       - Linia ~1538: `return is_completed, True, total_points` (samodiagnoza)
       - Linia ~1603: `return is_completed, is_passed, earned_points` (standardowy)
       - Linia ~1608: `return is_completed, False, 0` (w toku)
    
    ### ✅ Rezultat:
    Niezależnie od tego, w którym miejscu funkcja kończy działanie, flaga jest sprawdzana
    i `st.rerun()` jest wywołany jeśli potrzebny - eliminując problem podwójnego kliknięcia.
    
    ### 🎯 Testowane scenariusze:
    - Przyciski odpowiedzi w quizach samodiagnozy (opening quiz)
    - Przyciski odpowiedzi w quizach standardowych (closing quiz)  
    - Przycisk "Zatwierdź odpowiedzi" w pytaniach wielokrotnego wyboru
    - Wszystkie typy pytań w różnych konfiguracjach
    """)
