#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test aplikacji Streamlit - sprawdzenie czy karty praktyczne działają
Uruchom: streamlit run test_tabs_in_app.py
"""

import streamlit as st
import json
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="Test Kart w Aplikacji",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Test: Czy karty działają w Streamlit?")

# Initialize session state if needed
if 'lesson_step' not in st.session_state:
    st.session_state.lesson_step = 'practical_exercises'

# Test 1: Basic tabs functionality
st.subheader("Test 1: Podstawowe karty Streamlit")
test_tabs = st.tabs(["Test 1", "Test 2", "Test 3"])

with test_tabs[0]:
    st.write("✅ Karta 1 działa!")
    
with test_tabs[1]:
    st.write("✅ Karta 2 działa!")
    
with test_tabs[2]:
    st.write("✅ Karta 3 działa!")

st.success("✅ Podstawowe karty działają poprawnie")

# Test 2: Load lesson data and simulate practical_exercises
st.subheader("Test 2: Symulacja sekcji Ćwiczenia praktyczne")

try:
    lesson_file = "data/lessons/B1C1L4.json"
    if os.path.exists(lesson_file):
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        st.success("✅ B1C1L4.json załadowany")
        
        if 'sections' in lesson_data and 'practical_exercises' in lesson_data['sections']:
            practical_data = lesson_data['sections']['practical_exercises']
            st.success("✅ Sekcja practical_exercises znaleziona")
            
            if 'tabs' in practical_data:
                tabs_data = practical_data['tabs']
                st.success(f"✅ Znaleziono tabs: {list(tabs_data.keys())}")
                
                # Prepare tabs exactly like in lesson.py
                available_tabs = []
                tab_keys = []
                
                # 1. Autotest
                if 'autotest' in tabs_data:
                    available_tabs.append("🧠 Autotest")
                    tab_keys.append('autotest')
                
                # 2. Refleksja 
                if 'reflection' in tabs_data:
                    available_tabs.append("📝 Refleksja")
                    tab_keys.append('reflection')
                
                # 3. Analiza
                if 'analysis' in tabs_data:
                    available_tabs.append("📊 Analiza")
                    tab_keys.append('analysis')
                
                # 4. Wdrożenie
                if 'implementation' in tabs_data:
                    available_tabs.append("🎯 Wdrożenie")
                    tab_keys.append('implementation')
                
                st.info(f"Przygotowano {len(available_tabs)} kart: {available_tabs}")
                
                if available_tabs:
                    # Create tabs exactly like in lesson.py
                    try:
                        st.info("🔧 Tworzenie kart ćwiczeń praktycznych...")
                        
                        practical_tabs = st.tabs(available_tabs)
                        
                        st.success("✅ Karty utworzone pomyślnie!")
                        
                        for i, (tab_key, tab_title) in enumerate(zip(tab_keys, available_tabs)):
                            with practical_tabs[i]:
                                tab_data = tabs_data[tab_key]
                                
                                st.write(f"**Karta:** {tab_data.get('title', tab_key)}")
                                
                                if 'description' in tab_data:
                                    st.info(tab_data['description'])
                                
                                if 'sections' in tab_data:
                                    st.write(f"**Sekcje:** {len(tab_data['sections'])}")
                                    
                                    for j, section in enumerate(tab_data['sections']):
                                        with st.expander(f"{j+1}. {section.get('title', 'Sekcja')}"):
                                            st.markdown(section.get('content', 'Brak treści')[:300] + "...")
                                            
                                            if section.get('interactive'):
                                                st.write("🔄 **Sekcja interaktywna**")
                                                
                                                # Test interactive form
                                                with st.form(key=f"test_form_{tab_key}_{j}"):
                                                    user_input = st.text_area("Test odpowiedzi:")
                                                    submitted = st.form_submit_button("Test zapisz")
                                                    
                                                    if submitted:
                                                        st.success("✅ Formularz działa!")
                                else:
                                    st.warning("Brak sekcji w tej karcie")
                        
                        st.success("🎉 Wszystkie karty ćwiczeń praktycznych działają poprawnie!")
                        
                    except Exception as e:
                        st.error(f"❌ Błąd przy tworzeniu kart: {e}")
                        st.code(str(e))
                        
                        # Fallback to expanders
                        st.warning("Używam expanders jako fallback:")
                        
                        for tab_key, tab_title in zip(tab_keys, available_tabs):
                            with st.expander(tab_title):
                                tab_data = tabs_data[tab_key]
                                st.write(f"Fallback dla: {tab_data.get('title', tab_key)}")
                
                else:
                    st.error("❌ Brak dostępnych kart")
            else:
                st.error("❌ Brak 'tabs' w practical_exercises")
        else:
            st.error("❌ Brak sekcji practical_exercises")
    else:
        st.error(f"❌ Nie znaleziono pliku: {lesson_file}")

except Exception as e:
    st.error(f"❌ Błąd ogólny: {e}")
    st.code(str(e))

# Test 3: Environment info
st.subheader("Test 3: Informacje o środowisku")
st.write(f"**Streamlit version:** {st.__version__}")
st.write(f"**st.tabs available:** {hasattr(st, 'tabs')}")
st.write(f"**Python version:** {sys.version}")
st.write(f"**Working directory:** {os.getcwd()}")

# Instructions
st.subheader("📋 Instrukcje")
st.markdown("""
**Jeśli ten test pokazuje, że karty działają:**
1. Problem może być w głównej aplikacji - sprawdź lesson.py
2. Sprawdź czy session state nie powoduje problemów
3. Sprawdź import errors w głównej aplikacji

**Jeśli karty nie działają tutaj:**
1. Zaktualizuj Streamlit: `pip install streamlit --upgrade`
2. Sprawdź wersję Streamlit (wymagana >= 1.15.0)
3. Sprawdź czy nie ma błędów importu

**Następny krok:** Uruchom główną aplikację i przejdź do B1C1L4 → Ćwiczenia praktyczne
""")
