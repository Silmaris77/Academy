import streamlit as st
import pandas as pd
import altair as alt
import json
import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Dodaj ścieżkę główną projektu do systemu, aby móc importować moduły
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.degen_details import degen_details
from data.test_questions import DEGEN_TYPES, TEST_QUESTIONS
from utils.components import zen_header, zen_button, notification
from utils.material3_components import apply_material3_theme
from data.users import load_user_data, save_user_data
from utils.achievements import check_achievements

def show_degen_types():
    """Wyświetla nową zakładkę Typy Degenów, zawierającą test i eksplorator typów degenów"""
    
    apply_material3_theme()
    
    # Utwórz tabs dla podsekcji
    tab1, tab2 = st.tabs(["Test Degena", "Eksplorator Typów"])
    
    with tab1:
        show_degen_test_content()
    
    with tab2:
        show_degen_explorer_content()


def show_degen_test_content():
    """Wyświetla zawartość testu typu degena"""
    
    zen_header("Test Typu Degena 🎭")
    
    st.markdown("""
    ## Odkryj swój typ inwestora
    
    Ten test pozwoli Ci lepiej poznać swój profil psychologiczny jako inwestora. 
    Odpowiedz szczerze na poniższe pytania, aby otrzymać swój profil degena.
    
    ### Instrukcje:
    * Test składa się z 10 pytań
    * Przy każdym pytaniu zaznacz odpowiedź, która najlepiej Cię opisuje
    * Na końcu otrzymasz wynik wraz z opisem Twojego profilu
    * Wyniki testu zostaną zapisane w Twoim profilu
    """)
    
    # Sprawdź, czy użytkownik już wypełnił test
    users_data = load_user_data()
    user_data = users_data.get(st.session_state.username, {})
    test_results = user_data.get("degen_test", None)
    
    if "reset_test" not in st.session_state:
        st.session_state.reset_test = False
    
    if test_results and not st.session_state.reset_test:
        # Użytkownik już wypełnił test - pokaż wyniki
        st.success(f"Już wypełniłeś test! Twój typ degena to: {test_results['degen_type']}")
        
        # Wyświetl szczegóły typu
        show_degen_type_details(test_results['degen_type'])
        
        # Przycisk do resetowania testu
        if st.button("Wypełnij test ponownie"):
            st.session_state.reset_test = True
            st.rerun()
    else:
        # Użytkownik nie wypełnił testu lub chce go zresetować
        run_test()


def run_test():
    """Uruchamia test typu degena"""
    
    # Użyj bezpośrednio TEST_QUESTIONS z importu
    questions = TEST_QUESTIONS
    
    # Inicjalizacja stanu pytań
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.answers = []
        
    if st.session_state.current_question < len(questions):
        # Wyświetl aktualne pytanie
        question = questions[st.session_state.current_question]
        
        st.markdown(f"### Pytanie {st.session_state.current_question + 1} / {len(questions)}")
        st.markdown(f"**{question['question']}**")
          # Pokaż odpowiedzi jako przyciski
        answered = False
        
        for i, option in enumerate(question['options']):
            col1, col2 = st.columns([5, 1])
            with col1:
                if st.button(option['text'], key=f"answer_{i}", use_container_width=True):
                    # Zapisz wyniki dla tej odpowiedzi
                    if 'scores' not in st.session_state:
                        st.session_state.scores = {degen_type: 0 for degen_type in DEGEN_TYPES}
                    
                    # Dodaj punkty z wybranej odpowiedzi
                    for degen_type, score in option['scores'].items():
                        st.session_state.scores[degen_type] = st.session_state.scores.get(degen_type, 0) + score
                    
                    st.session_state.current_question += 1
                    answered = True
        
        if answered:
            st.rerun()
            
    else:
        # Wszystkie pytania zostały odpowiedziane - oblicz wyniki
        calculate_results()


def calculate_results():
    """Oblicza wyniki testu i zapisuje je w profilu użytkownika"""
    
    # Użyj zebranych punktów dla każdego typu degena
    if 'scores' not in st.session_state:
        st.session_state.scores = {degen_type: 0 for degen_type in DEGEN_TYPES}
    
    # Określ dominujący typ na podstawie punktacji
    dominant_type = max(st.session_state.scores.items(), key=lambda x: x[1])[0]
    
    # Zapisz wyniki
    users_data = load_user_data()
    user_data = users_data.get(st.session_state.username, {})
    
    test_results = {
        "degen_type": dominant_type,
        "scores": st.session_state.scores,
        "timestamp": pd.Timestamp.now().isoformat()
    }
      user_data["degen_test"] = test_results
    users_data[st.session_state.username] = user_data
    save_user_data(users_data)
    
    # Check for achievements after test completion
    check_achievements(st.session_state.username)
    
    # Pokaż wyniki
    st.balloons()
    st.success(f"Test zakończony! Twój typ degena to: {dominant_type}")
    
    # Wyświetl szczegóły typu
    show_degen_type_details(dominant_type)
    
    # Resetuj stan testu
    st.session_state.reset_test = False
    del st.session_state.current_question
    del st.session_state.answers
    
    # Dodaj przycisk do powrotu do głównej strony
    if st.button("Wróć do dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()


def show_degen_type_details(degen_type):
    """Wyświetla szczegółowe informacje o typie degena"""
    
    # Pobierz dane o typie degena z dostępnych struktur danych
    degen_type_data = DEGEN_TYPES.get(degen_type, {})
    description = degen_type_data.get("description", "Brak opisu")
    strengths = degen_type_data.get("strengths", [])
    challenges = degen_type_data.get("challenges", [])
    strategy = degen_type_data.get("strategy", "")
    
    # Pobierz pełny opis z degen_details
    full_details = degen_details.get(degen_type, "")
    
    # Tytuł i opis
    st.markdown(f"## Twój typ degena: {degen_type}")
    
    # Opis krótki
    st.markdown(f"**{description}**")
    
    # Pełny opis w expander
    with st.expander("Szczegółowy opis Twojego typu", expanded=False):
        # Mocne strony
        st.markdown("#### 💪 Mocne strony:")
        for strength in strengths:
            st.markdown(f"- {strength}")
        
        # Wyzwania
        st.markdown("#### 🤔 Wyzwania:")
        for challenge in challenges:
            st.markdown(f"- {challenge}")
        
        # Strategia
        st.markdown("#### 🚀 Strategia rozwoju:")
        st.markdown(f"- {strategy}")
        
        # Pełny opis z degen_details jeśli istnieje
        if full_details:
            st.markdown("#### 📝 Pełny opis:")
            st.markdown(full_details)


def show_degen_explorer_content():
    """Wyświetla zawartość eksploratora typów degenów"""
    
    zen_header("Eksplorator Typów Degenów 🔍")
    
    st.markdown("""
    ## Poznaj wszystkie profile inwestora
    
    Każdy inwestor ma swój unikalny styl podejmowania decyzji. Poznaj charakterystyki wszystkich typów i ich
    mocne strony oraz wyzwania.
    """)
      # Wybierz typ do eksploracji
    degen_type = st.selectbox(
        "Wybierz typ degena do eksploracji:",
        list(DEGEN_TYPES.keys())
    )
    
    # Wyświetl szczegóły wybranego typu
    show_degen_type_details(degen_type)
    
    # Dodaj sekcję porównania
    with st.expander("Porównaj wszystkie typy", expanded=False):
        show_comparison_table()


def show_comparison_table():
    """Wyświetla tabelę porównawczą wszystkich typów degenów"""
    
    st.markdown("### Porównanie typów degenów")
    
    # Przygotuj dane do tabeli z faktycznych danych DEGEN_TYPES
    degen_types_list = list(DEGEN_TYPES.keys())
    descriptions = [DEGEN_TYPES[t].get("description", "") for t in degen_types_list]
    
    # Przygotuj listy mocnych stron i wyzwań
    strengths_list = []
    challenges_list = []
    strategies_list = []
    
    for t in degen_types_list:
        # Pozyskaj listę mocnych stron i połącz w string
        strengths = DEGEN_TYPES[t].get("strengths", [])
        strengths_str = ", ".join(strengths) if strengths else "Brak danych"
        strengths_list.append(strengths_str)
        
        # Pozyskaj listę wyzwań i połącz w string
        challenges = DEGEN_TYPES[t].get("challenges", [])
        challenges_str = ", ".join(challenges) if challenges else "Brak danych"
        challenges_list.append(challenges_str)
        
        # Pozyskaj strategię
        strategy = DEGEN_TYPES[t].get("strategy", "Brak danych")
        strategies_list.append(strategy)
    
    # Utwórz słownik danych do tabeli
    comparison_data = {
        'Typ degena': degen_types_list,
        'Opis': descriptions,
        'Mocne strony': strengths_list,
        'Wyzwania': challenges_list,
        'Strategia': strategies_list
    }
    
    # Wyświetl tabelę
    df = pd.DataFrame(comparison_data)
    st.table(df)
    
    # Dodaj wizualizację typów
    st.markdown("### Wizualizacja cech typów inwestora")    # Przygotuj dane do wykresu - najprostsze podejście z konkretnymi wartościami
    chart_data = pd.DataFrame({
        'Kategoria': ['Szybkość decyzji', 'Analityczność', 'Zarządzanie ryzykiem', 'Adaptacja do zmian'],
    })
    
    # Dodaj kolumny dla każdego typu degena
    for idx, degen_type in enumerate(DEGEN_TYPES.keys()):
        # Generowanie różnych wartości dla każdego typu używając indeksu
        values = []
        for i in range(4):
            # Generuj wartości w zakresie 20-90 bazując na indeksie typu i kategorii
            base_value = ((idx * 17) + (i * 19)) % 70 + 20
            values.append(base_value)
        
        # Dodaj jako nową kolumnę
        chart_data[degen_type] = values
    
    # Przekształć dane do formatu długiego
    chart_data_long = pd.melt(
        chart_data, 
        id_vars=['Kategoria'], 
        var_name='Typ degena', 
        value_name='Wartość'
    )
    
    # Stwórz wykres słupkowy porównawczy
    chart = alt.Chart(chart_data_long).mark_bar().encode(
        x=alt.X('Typ degena:N', title=None),
        y=alt.Y('Wartość:Q', title='Poziom cechy (0-100)'),
        color=alt.Color('Typ degena:N', legend=None),
        column=alt.Column('Kategoria:N', title=None)
    ).properties(
        width=alt.Step(80)
    )
    
    st.altair_chart(chart, use_container_width=True)
