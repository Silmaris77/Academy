#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import json
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    st.set_page_config(
        page_title="Test Ćwiczenia praktyczne",
        page_icon="🧪",
        layout="wide"
    )
    
    st.title("🧪 Test sekcji: Ćwiczenia praktyczne")
    
    # Test 1: Basic Polish characters
    st.header("Test 1: Polskie znaki")
    st.write("Ćwiczenia praktyczne - ąęśćżźłóń")
    
    # Test 2: Load B1C1L4 data
    st.header("Test 2: Ładowanie danych B1C1L4")
    
    try:
        lesson_file = "data/lessons/B1C1L4.json"
        if os.path.exists(lesson_file):
            with open(lesson_file, 'r', encoding='utf-8') as f:
                lesson_data = json.load(f)
            
            st.success(f"✅ B1C1L4.json załadowany pomyślnie")
            
            # Test practical_exercises section
            if 'sections' in lesson_data and 'practical_exercises' in lesson_data['sections']:
                practical_data = lesson_data['sections']['practical_exercises']
                st.success("✅ Znaleziono sekcję practical_exercises")
                
                if 'tabs' in practical_data:
                    tabs_data = practical_data['tabs']
                    st.success(f"✅ Znaleziono tabs: {list(tabs_data.keys())}")
                    
                    # Test 3: Display tabs like in lesson.py
                    st.header("Test 3: Wyświetlanie zakładek")
                    
                    available_tabs = []
                    tab_keys = []
                    
                    if 'reflection' in tabs_data:
                        available_tabs.append("📝 Refleksja")
                        tab_keys.append('reflection')
                    
                    if 'implementation' in tabs_data:
                        available_tabs.append("🎯 Wdrożenie")
                        tab_keys.append('implementation')
                    
                    if 'analysis' in tabs_data:
                        available_tabs.append("📊 Analiza")
                        tab_keys.append('analysis')
                    
                    if 'autotest' in tabs_data:
                        available_tabs.append("🧠 Autotest")
                        tab_keys.append('autotest')
                    
                    if available_tabs:
                        st.success(f"✅ Przygotowano {len(available_tabs)} zakładek")
                        
                        # Create actual tabs
                        tabs = st.tabs(available_tabs)
                        
                        for i, (tab_key, tab_title) in enumerate(zip(tab_keys, available_tabs)):
                            with tabs[i]:
                                tab_data = tabs_data[tab_key]
                                
                                st.write(f"**Zakładka:** {tab_data.get('title', tab_key)}")
                                
                                if 'sections' in tab_data:
                                    for j, section in enumerate(tab_data['sections']):
                                        with st.expander(f"{j+1}. {section.get('title', 'Sekcja')}"):
                                            st.markdown(section.get('content', 'Brak treści'), unsafe_allow_html=True)
                                else:
                                    st.warning("Brak sekcji w tej zakładce")
                    else:
                        st.error("❌ Nie znaleziono żadnych zakładek")
                else:
                    st.error("❌ Brak klucza 'tabs' w practical_exercises")
            else:
                st.error("❌ Brak sekcji practical_exercises")
        else:
            st.error(f"❌ Nie znaleziono pliku: {lesson_file}")
            
    except Exception as e:
        st.error(f"❌ Błąd: {str(e)}")
        st.code(f"Traceback: {e}")

if __name__ == "__main__":
    main()
