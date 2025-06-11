#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ALTERNATIVE TABS IMPLEMENTATION - jeśli st.tabs() nie działa
"""

import streamlit as st

def create_alternative_tabs(tab_names, tab_contents, key_prefix="alt_tabs"):
    """
    Alternatywna implementacja kart używająca radio buttons
    """
    # Selectbox do wyboru karty
    selected_tab = st.selectbox(
        "Wybierz sekcję:",
        tab_names,
        key=f"{key_prefix}_selector"
    )
    
    # Wyświetl zawartość wybranej karty
    selected_index = tab_names.index(selected_tab)
    
    # Kontener dla zawartości
    with st.container():
        st.markdown(f"### {selected_tab}")
        if callable(tab_contents[selected_index]):
            tab_contents[selected_index]()
        else:
            st.write(tab_contents[selected_index])

def render_practical_exercises_alternative():
    """
    Alternatywna implementacja ćwiczeń praktycznych bez st.tabs()
    """
    st.title("🎯 Ćwiczenia Praktyczne - Wersja Alternatywna")
    
    # Definicja kart
    tab_names = [
        "🧠 Autotest",
        "📝 Refleksja", 
        "📊 Analiza",
        "🎯 Wdrożenie"
    ]
    
    def autotest_content():
        st.info("🧠 **Autotest** - Mini-quizy sprawdzające, testy wiedzy praktycznej i scenariusze decyzyjne")
        st.markdown("### Test: Rozpoznawanie pułapek emocjonalnych")
        st.write("Czy rozpoznasz sytuacje wysokiego ryzyka emocjonalnego?")
        
        with st.form("autotest_form"):
            st.write("**Scenariusz 1:**")
            st.write("Twoja akcja rośnie 5. dzień z rzędu o 40%. W grupie wszyscy piszą, że to dopiero początek.")
            risk_level = st.slider("Poziom ryzyka (1-5):", 1, 5, 3)
            reason = st.text_area("Powód:")
            
            if st.form_submit_button("Zapisz odpowiedź"):
                st.success("✅ Odpowiedź zapisana!")
                st.write(f"Wybrany poziom ryzyka: {risk_level}")
    
    def reflection_content():
        st.info("📝 **Refleksja** - Pytania do przemyślenia, samoocena i dziennik inwestora")
        st.markdown("### Inwestycyjny Flashback")
        st.write("Przypomnij sobie sytuację, w której podjąłeś decyzję pod wpływem emocji.")
        
        with st.form("reflection_form"):
            emotions = st.text_area("Jakie emocje Ci towarzyszyły?")
            trigger = st.text_area("Co było wyzwalaczem tej emocji?")
            consequences = st.text_area("Jakie były skutki tej decyzji?")
            
            if st.form_submit_button("Zapisz refleksję"):
                st.success("✅ Refleksja zapisana!")
    
    def analysis_content():
        st.info("📊 **Analiza** - Ćwiczenia analityczne, case studies i symulacje scenariuszy")
        st.markdown("### Analiza przypadku: Kryzys 2020")
        st.write("Wyobraź sobie, że jesteś inwestorem w marcu 2020. Rynki spadają o 30-40%.")
        
        with st.form("analysis_form"):
            scenario = st.selectbox("Twoja reakcja:", [
                "Sprzedajesz wszystko",
                "Trzymasz pozycje", 
                "Dokupujesz",
                "Rebalancujesz"
            ])
            justification = st.text_area("Uzasadnienie:")
            
            if st.form_submit_button("Zapisz analizę"):
                st.success("✅ Analiza zapisana!")
    
    def implementation_content():
        st.info("🎯 **Wdrożenie** - Konkretne zadania do wykonania, checklista działań i plan implementacji")
        st.markdown("### Plan awaryjny na emocjonalne kryzysy")
        st.write("Stwórz swój protokół bezpieczeństwa:")
        
        with st.form("implementation_form"):
            warning_signals = st.text_area("Sygnały ostrzegawcze:")
            immediate_actions = st.text_area("Natychmiastowe działania:")
            rules_24h = st.text_area("Zasady 24-godzinne:")
            
            if st.form_submit_button("Zapisz plan"):
                st.success("✅ Plan zapisany!")
    
    tab_contents = [
        autotest_content,
        reflection_content,
        analysis_content,
        implementation_content
    ]
    
    # Użyj alternatywnych kart
    create_alternative_tabs(tab_names, tab_contents, "practical_exercises")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Ćwiczenia Praktyczne - Alt",
        page_icon="🎯",
        layout="wide"
    )
    
    render_practical_exercises_alternative()
    
    st.markdown("---")
    st.subheader("📋 O tej wersji")
    st.markdown("""
    **To jest alternatywna wersja kart** która działa bez `st.tabs()`.
    
    **Jak działa:**
    - Używa `st.selectbox()` do wyboru sekcji
    - Każda sekcja ma pełną funkcjonalność
    - Wszystkie formularze działają poprawnie
    - Obsługuje polskie znaki i emoji
    
    **Kiedy używać:**
    - Gdy `st.tabs()` nie działa
    - Starsza wersja Streamlit
    - Problemy z kompatybilnością
    
    **Wdrożenie do głównej aplikacji:**
    Możemy zastąpić problematyczne `st.tabs()` tym rozwiązaniem.
    """)
