#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import json
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="Debug Tabs",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Debug: Dlaczego karty nie działają?")

# Check Streamlit version
st.subheader("1. Sprawdzenie wersji Streamlit")
try:
    st.write(f"**Streamlit version:** {st.__version__}")
    st.write(f"**st.tabs available:** {hasattr(st, 'tabs')}")
    
    if hasattr(st, 'tabs'):
        st.success("✅ st.tabs jest dostępne")
    else:
        st.error("❌ st.tabs nie jest dostępne - za stara wersja Streamlit")
        st.info("Wymagana wersja Streamlit >= 1.15.0 dla st.tabs")
except Exception as e:
    st.error(f"Błąd przy sprawdzaniu wersji: {e}")

# Test basic tabs functionality
st.subheader("2. Test podstawowy st.tabs")
try:
    test_tabs = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    
    with test_tabs[0]:
        st.write("Zawartość Tab 1")
        st.success("✅ Tab 1 działa")
    
    with test_tabs[1]:
        st.write("Zawartość Tab 2")
        st.success("✅ Tab 2 działa")
    
    with test_tabs[2]:
        st.write("Zawartość Tab 3") 
        st.success("✅ Tab 3 działa")
    
    st.success("✅ Podstawowe karty działają poprawnie")
    
except Exception as e:
    st.error(f"❌ Błąd z st.tabs: {e}")
    st.info("Spróbuj zainstalować nowszą wersję Streamlit: pip install streamlit --upgrade")

# Test lesson data loading
st.subheader("3. Test ładowania danych lekcji")
try:
    lesson_file = "data/lessons/B1C1L4.json"
    if os.path.exists(lesson_file):
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        st.success("✅ B1C1L4.json załadowany pomyślnie")
        
        if 'sections' in lesson_data and 'practical_exercises' in lesson_data['sections']:
            practical_data = lesson_data['sections']['practical_exercises']
            st.success("✅ Sekcja practical_exercises znaleziona")
            
            if 'tabs' in practical_data:
                tabs_data = practical_data['tabs']
                st.success(f"✅ Tabs znalezione: {list(tabs_data.keys())}")
                
                # Test actual practical exercises tabs
                st.subheader("4. Test kart ćwiczeń praktycznych")
                
                # Prepare tabs like in lesson.py
                available_tabs = []
                tab_keys = []
                
                if 'autotest' in tabs_data:
                    available_tabs.append("🧠 Autotest")
                    tab_keys.append('autotest')
                
                if 'reflection' in tabs_data:
                    available_tabs.append("📝 Refleksja")
                    tab_keys.append('reflection')
                
                if 'analysis' in tabs_data:
                    available_tabs.append("📊 Analiza")
                    tab_keys.append('analysis')
                
                if 'implementation' in tabs_data:
                    available_tabs.append("🎯 Wdrożenie")
                    tab_keys.append('implementation')
                
                if available_tabs:
                    st.write(f"**Przygotowano {len(available_tabs)} kart:**")
                    for i, tab in enumerate(available_tabs):
                        st.write(f"{i+1}. {tab}")
                    
                    # Create actual tabs
                    try:
                        practical_tabs = st.tabs(available_tabs)
                        
                        for i, (tab_key, tab_title) in enumerate(zip(tab_keys, available_tabs)):
                            with practical_tabs[i]:
                                tab_data = tabs_data[tab_key]
                                
                                st.write(f"**Zakładka:** {tab_data.get('title', tab_key)}")
                                
                                if 'description' in tab_data:
                                    st.info(tab_data['description'])
                                
                                if 'sections' in tab_data:
                                    st.write(f"**Liczba sekcji:** {len(tab_data['sections'])}")
                                    for j, section in enumerate(tab_data['sections']):
                                        with st.expander(f"{j+1}. {section.get('title', 'Sekcja')}"):
                                            st.markdown(section.get('content', 'Brak treści')[:200] + "...")
                                            if section.get('interactive'):
                                                st.write("🔄 Sekcja interaktywna")
                                else:
                                    st.warning("Brak sekcji w tej zakładce")
                        
                        st.success("🎉 Karty ćwiczeń praktycznych działają poprawnie!")
                        
                    except Exception as e:
                        st.error(f"❌ Błąd przy tworzeniu kart ćwiczeń: {e}")
                        st.code(str(e))
                        
                else:
                    st.error("❌ Brak dostępnych kart")
            else:
                st.error("❌ Brak sekcji 'tabs' w practical_exercises")
        else:
            st.error("❌ Brak sekcji practical_exercises")
    else:
        st.error(f"❌ Nie znaleziono pliku: {lesson_file}")
        
except Exception as e:
    st.error(f"❌ Błąd podczas ładowania danych: {e}")
    st.code(str(e))

# Session state inspection
st.subheader("5. Sprawdzenie session state")
if st.checkbox("Pokaż session state"):
    st.write("**Session state keys:**")
    for key in st.session_state.keys():
        st.write(f"- {key}: {type(st.session_state[key])}")

# Final recommendations
st.subheader("🎯 Rekomendacje")
st.markdown("""
**Jeśli karty nie działają w głównej aplikacji, sprawdź:**

1. **Wersja Streamlit**: Upewnij się, że masz Streamlit >= 1.15.0
2. **Błędy składniowe**: Sprawdź czy nie ma błędów w lesson.py
3. **Import problemy**: Sprawdź czy wszystkie moduły się ładują poprawnie
4. **Session state**: Sprawdź czy session state nie jest zepsuty
5. **Browser cache**: Wyczyść pamięć podręczną przeglądarki

**Jeśli ten test pokazuje, że karty działają, ale w głównej aplikacji nie - problem jest w lesson.py.**
""")

# Debug button
if st.button("🔄 Odśwież test"):
    st.rerun()
