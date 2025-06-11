# -*- coding: utf-8 -*-
"""
Reset script for clearing session state issues
"""
import streamlit as st
import json
import os

st.set_page_config(
    page_title="Reset Session State",
    page_icon="🔄",
    layout="wide"
)

st.title("🔄 Reset Session State - Ćwiczenia Praktyczne")

st.info("Ten skrypt pomoże zresetować session state i przetestować nową funkcjonalność practical_exercises")

# Show current session state
st.subheader("Aktualny stan sesji:")
if st.session_state:
    for key, value in st.session_state.items():
        if 'lesson' in key.lower():
            st.write(f"**{key}:** {value}")

# Reset options
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🗑️ Wyczyść session state"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.success("Session state wyczyszczony!")
        st.rerun()

with col2:
    if st.button("🔄 Reset lekcji B1C1L4"):
        lesson_keys = [k for k in st.session_state.keys() if 'lesson' in k.lower() or 'B1C1L4' in str(k)]
        for key in lesson_keys:
            del st.session_state[key]
        st.success("Stan lekcji B1C1L4 zresetowany!")
        st.rerun()

with col3:
    if st.button("🎯 Ustaw na practical_exercises"):
        st.session_state.current_lesson = "B1C1L4"
        st.session_state.lesson_step = "practical_exercises"
        st.success("Ustawiono na krok practical_exercises!")

# Test practical_exercises structure
st.subheader("Test struktury practical_exercises:")

lesson_file = "data/lessons/B1C1L4.json"
if os.path.exists(lesson_file):
    try:
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        # Check if practical_exercises exists
        if 'practical_exercises' in lesson_data.get('sections', {}):
            pe = lesson_data['sections']['practical_exercises']
            st.success("✅ practical_exercises sekcja istnieje")
            
            if 'tabs' in pe:
                tabs = pe['tabs']
                st.success(f"✅ Znaleziono tabs: {list(tabs.keys())}")
                
                # Test each tab
                for tab_name, tab_data in tabs.items():
                    sections_count = len(tab_data.get('sections', []))
                    title = tab_data.get('title', 'Brak tytułu')
                    st.write(f"- **{tab_name}:** '{title}' ({sections_count} sekcji)")
                
                st.success("🎉 Struktura practical_exercises jest poprawna!")
            else:
                st.error("❌ Brak 'tabs' w practical_exercises")
        else:
            st.error("❌ Brak sekcji practical_exercises")
    except Exception as e:
        st.error(f"Błąd: {e}")

# Quick fix instructions
st.subheader("🛠️ Instrukcje naprawy:")
st.markdown("""
1. **Wyczyść session state** - kliknij przycisk powyżej
2. **Zrestartuj główną aplikację** - zatrzymaj Streamlit i uruchom ponownie
3. **Sprawdź encoding** - upewnij się, że polskie znaki wyświetlają się poprawnie
4. **Przejdź do B1C1L4** - wybierz lekcję i sprawdź czy pojawia się zakładka "Ćwiczenia praktyczne"
""")

# Test encoding
st.subheader("Test kodowania:")
test_text = "Ćwiczenia praktyczne - ąćęłńóśźż"
st.write(f"Test: {test_text}")

if "ć" in test_text and "ą" in test_text:
    st.success("✅ Kodowanie działa poprawnie")
else:
    st.error("❌ Problem z kodowaniem")

# Navigation
if st.button("🏠 Przejdź do głównej aplikacji"):
    st.switch_page("main.py")
