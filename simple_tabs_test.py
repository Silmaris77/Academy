#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SIMPLE TABS TEST - sprawdzenie czy st.tabs() działa poprawnie w Streamlit
"""

import streamlit as st
import sys
import os

st.set_page_config(
    page_title="Test Kart Streamlit",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Test: Czy karty Streamlit działają?")

# Test podstawowych kart
st.subheader("1. Test podstawowych kart")

try:
    # Test czy st.tabs istnieje
    if not hasattr(st, 'tabs'):
        st.error("❌ st.tabs() nie jest dostępne w tej wersji Streamlit")
        st.info("Wymagana wersja Streamlit >= 1.15.0")
        st.code(f"Aktualna wersja Streamlit: {st.__version__}")
    else:
        st.success("✅ st.tabs() jest dostępne")
        
        # Utwórz testowe karty
        test_tabs = st.tabs(["Karta 1", "Karta 2", "Karta 3", "Karta 4"])
        
        with test_tabs[0]:
            st.write("🎯 **Zawartość karty 1**")
            st.info("Jeśli widzisz ten tekst po kliknięciu na 'Karta 1', karty działają!")
            
        with test_tabs[1]:
            st.write("📝 **Zawartość karty 2**")
            st.success("Karty działają poprawnie!")
            
        with test_tabs[2]:
            st.write("📊 **Zawartość karty 3**")
            with st.form("test_form"):
                text_input = st.text_area("Testowy formularz:")
                if st.form_submit_button("Test"):
                    st.success("Formularz działa w karcie!")
                    
        with test_tabs[3]:
            st.write("🧠 **Zawartość karty 4**")
            st.warning("Wszystkie karty działają jak należy!")

except Exception as e:
    st.error(f"❌ Błąd z kartami: {e}")
    st.code(str(e))

# Test informacji o środowisku
st.subheader("2. Informacje o środowisku")
st.write(f"**Streamlit version:** {st.__version__}")
st.write(f"**Python version:** {sys.version}")
st.write(f"**st.tabs dostępne:** {hasattr(st, 'tabs')}")

# Test emulacji kart ćwiczeń praktycznych
st.subheader("3. Test kart ćwiczeń praktycznych")

try:
    practical_tabs = st.tabs(["🧠 Autotest", "📝 Refleksja", "📊 Analiza", "🎯 Wdrożenie"])
    
    with practical_tabs[0]:
        st.info("🧠 **Autotest** - Mini-quizy sprawdzające, testy wiedzy praktycznej i scenariusze decyzyjne")
        st.markdown("### Test przykład")
        st.write("To jest przykładowa zawartość karty Autotest")
        
        with st.form("autotest_form"):
            response = st.text_area("Przykładowa odpowiedź:")
            if st.form_submit_button("Zapisz"):
                st.success("✅ Formularz w karcie Autotest działa!")
        
    with practical_tabs[1]:
        st.info("📝 **Refleksja** - Pytania do przemyślenia, samoocena i dziennik inwestora")
        st.markdown("### Refleksja przykład")
        st.write("To jest przykładowa zawartość karty Refleksja")
        
    with practical_tabs[2]:
        st.info("📊 **Analiza** - Ćwiczenia analityczne, case studies i symulacje scenariuszy")
        st.markdown("### Analiza przykład")
        st.write("To jest przykładowa zawartość karty Analiza")
        
    with practical_tabs[3]:
        st.info("🎯 **Wdrożenie** - Konkretne zadania do wykonania, checklista działań i plan implementacji")
        st.markdown("### Wdrożenie przykład")
        st.write("To jest przykładowa zawartość karty Wdrożenie")
        
    st.success("🎉 Wszystkie karty ćwiczeń praktycznych działają poprawnie!")
    
except Exception as e:
    st.error(f"❌ Problem z kartami ćwiczeń: {e}")

# Instrukcje
st.subheader("📋 Wyniki testu")

st.markdown("""
**Co powinieneś zobaczyć:**
- ✅ 4 klikalne karty u góry każdej sekcji
- ✅ Zawartość zmienia się po kliknięciu na różne karty
- ✅ Formularze działają wewnątrz kart
- ✅ Emoji i polskie znaki wyświetlają się poprawnie

**Jeśli karty nie działają:**
- 🔧 Zaktualizuj Streamlit: `pip install streamlit --upgrade`
- 🔧 Sprawdź wersję: `streamlit --version`
- 🔧 Wymagana wersja: >= 1.15.0

**Następny krok:**
Jeśli ten test pokazuje, że karty działają, problem może być w głównej aplikacji.
Uruchom główną aplikację i przejdź do B1C1L4 → Ćwiczenia praktyczne.
""")

# Quick restart instructions
st.subheader("🔄 Szybka naprawa")
st.markdown("""
```bash
# 1. Zaktualizuj Streamlit
pip install streamlit --upgrade

# 2. Uruchom główną aplikację
streamlit run main.py

# 3. Przejdź do: Kurs → B1C1L4 → Ćwiczenia praktyczne
```
""")
