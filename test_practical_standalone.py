# -*- coding: utf-8 -*-
import streamlit as st
import json
import os

st.set_page_config(
    page_title="Test Ćwiczeń Praktycznych",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Test Sekcji: Ćwiczenia Praktyczne")

# Test loading B1C1L4
lesson_file = "data/lessons/B1C1L4.json"

if os.path.exists(lesson_file):
    try:
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson_data = json.load(f)
        
        st.success("✅ B1C1L4.json załadowany pomyślnie")
        
        if 'sections' in lesson_data and 'practical_exercises' in lesson_data['sections']:
            practical_data = lesson_data['sections']['practical_exercises']
            st.success("✅ Znaleziono sekcję practical_exercises")
            
            st.write("**Klucze w practical_exercises:**", list(practical_data.keys()))
            
            if 'tabs' in practical_data:
                tabs_data = practical_data['tabs']
                st.success(f"✅ Znaleziono tabs: {list(tabs_data.keys())}")
                
                # Simulate the lesson.py logic
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
                    
                    # Test step_order logic
                    st.subheader("Test logiki step_order")
                    step_order = ['intro', 'opening_quiz', 'content']
                    
                    if 'practical_exercises' in lesson_data.get('sections', {}):
                        step_order.append('practical_exercises')
                        st.success("✅ practical_exercises dodane do step_order")
                    else:
                        st.error("❌ practical_exercises NIE zostało dodane do step_order")
                    
                    step_order.extend(['closing_quiz', 'summary'])
                    st.write("**Finalne step_order:**", step_order)
                    
                    # Test step_names
                    step_names = {
                        'intro': 'Wprowadzenie',
                        'opening_quiz': 'Samorefleksja',
                        'content': 'Materiał',
                        'practical_exercises': 'Ćwiczenia praktyczne',
                        'closing_quiz': 'Quiz końcowy',
                        'summary': 'Podsumowanie'
                    }
                    
                    if 'practical_exercises' in step_names:
                        practical_name = step_names['practical_exercises']
                        st.success(f"✅ Nazwa kroku: '{practical_name}'")
                    else:
                        st.error("❌ Brak nazwy dla practical_exercises")
                    
                    # Display the actual tabs
                    st.subheader("Test wyświetlania zakładek")
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
                st.write("**Dostępne klucze:**", list(practical_data.keys()))
        else:
            st.error("❌ Brak sekcji practical_exercises")
    except Exception as e:
        st.error(f"❌ Błąd podczas ładowania: {str(e)}")
else:
    st.error(f"❌ Nie znaleziono pliku: {lesson_file}")

# Test encoding
st.subheader("Test kodowania znaków")
test_string = "Ćwiczenia praktyczne - test polskich znaków: ąćęłńóśźż"
st.write(test_string)
st.success("✅ Polskie znaki wyświetlają się poprawnie" if "ą" in test_string else "❌ Problem z polskimi znakami")
