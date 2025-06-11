"""
Test script dla weryfikacji rozwiązania problemu podwójnego kliknięcia.
Ten skrypt testuje czy przyciski w quizach działają po pojedynczym kliknięciu.
"""

import streamlit as st
import sys
import os

# Dodaj ścieżkę do głównego katalogu aplikacji
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="Test pojedynczego kliknięcia - Quiz",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Test pojedynczego kliknięcia w quizach")

st.markdown("""
Ten test sprawdza czy problem z podwójnym kliknięciem został rozwiązany:

### Co testujemy:
1. **Pojedyncze kliknięcie na przycisk odpowiedzi** (pytania typu single choice)
2. **Pojedyncze kliknięcie na przycisk "Zatwierdź odpowiedzi"** (pytania typu multiple choice)
3. **Pojedyncze kliknięcie na przycisk w quizach samodiagnozy**

### Jak testować:
- Kliknij przycisk **tylko jeden raz**
- Sprawdź czy odpowiedź została natychmiast zarejestrowana
- Sprawdź czy nie musisz klikać drugi raz

---
""")

# Test data dla różnych typów pytań
test_quiz_data = {
    'title': 'Test Quiz - Pojedyncze kliknięcie',
    'description': 'Ten quiz testuje czy przyciski działają po pojedynczym kliknięciu.',
    'questions': [
        {
            'question': 'Test pytania z pojedynczym wyborem - czy działa po 1 kliknięciu?',
            'options': ['Tak, działa', 'Nie, trzeba kliknąć dwa razy', 'Nie jestem pewien'],
            'type': 'single_choice',
            'correct_answer': 0
        },
        {
            'question': 'Test pytania z wielokrotnym wyborem - czy "Zatwierdź" działa po 1 kliknięciu?',
            'options': ['Opcja A', 'Opcja B', 'Opcja C', 'Opcja D'],
            'type': 'multiple_choice',
            'correct_answers': [0, 2]
        },
        {
            'question': 'Test quizu samodiagnozy - czy działa po 1 kliknięciu?',
            'options': ['1 - Zdecydowanie nie', '2 - Raczej nie', '3 - Neutralnie', '4 - Raczej tak', '5 - Zdecydowanie tak'],
            'type': 'single_choice'
            # Brak correct_answer oznacza quiz samodiagnozy
        }
    ]
}

# Import funkcji display_quiz
try:
    from views.lesson import display_quiz
    
    st.markdown("### ✅ Funkcja display_quiz została zaimportowana pomyślnie")
    
    # Wyświetl test quiz
    st.markdown("### 🧪 Quiz testowy:")
    
    quiz_complete, quiz_passed, earned_points = display_quiz(test_quiz_data, passing_threshold=60)
    
    # Wyświetl status testu
    if quiz_complete:
        st.success(f"✅ Quiz ukończony! Wynik zdany: {quiz_passed}, Punkty: {earned_points}")
        st.balloons()
        
        # Podsumowanie testu
        st.markdown("""
        ### 📊 Wyniki testu:
        
        Jeśli udało Ci się ukończyć quiz klikając każdy przycisk **tylko jeden raz**, 
        to problem z podwójnym kliknięciem został rozwiązany! 🎉
        
        #### Co zostało naprawione:
        - ✅ Usunięto natychmiastowe `st.rerun()` po kliknięciu przycisku
        - ✅ Dodano system flag dla opóźnionego odświeżania 
        - ✅ Zachowano funkcjonalność przycisków
        - ✅ Naprawiono zarówno pytania single choice jak i multiple choice
        
        #### Jak to działa teraz:
        1. Kliknięcie przycisku → natychmiastowe przetworzenie odpowiedzi
        2. Ustawienie flagi `quiz_needs_refresh` 
        3. Odświeżenie strony następuje dopiero na końcu funkcji
        4. Użytkownik widzi efekt po pojedynczym kliknięciu
        """)
    else:
        st.info("Quiz w toku - testuj klikając przyciski tylko jeden raz każdy!")
        
except ImportError as e:
    st.error(f"❌ Błąd importu: {e}")
except Exception as e:
    st.error(f"❌ Błąd: {e}")
    st.exception(e)

# Dodatkowe informacje o teście
with st.expander("🔍 Szczegóły techniczne rozwiązania"):
    st.markdown("""
    ### Przyczyna problemu:
    Streamlit wykonywał `st.rerun()` natychmiast po kliknięciu przycisku, co resetowało stan wszystkich widgetów. 
    Pierwsze kliknięcie uruchamiało rerun, drugie kliknięcie faktycznie przetwarzało logikę.
    
    ### Rozwiązanie:
    ```python
    # PRZED (problemowe):
    if st.button("Odpowiedź"):
        # logika przetwarzania
        st.rerun()  # ← Natychmiastowy rerun
    
    # PO (naprawione):
    if st.button("Odpowiedź"):
        # logika przetwarzania
        st.session_state['quiz_needs_refresh'] = True  # ← Flaga
    
    # Na końcu funkcji:
    if st.session_state.get('quiz_needs_refresh', False):
        st.session_state['quiz_needs_refresh'] = False
        st.rerun()  # ← Opóźniony rerun
    ```
    
    ### Korzyści:
    - ✅ Pojedyncze kliknięcie wystarczy
    - ✅ Lepsze UX (User Experience)
    - ✅ Zachowana funkcjonalność
    - ✅ Brak problemów z session state
    """)
