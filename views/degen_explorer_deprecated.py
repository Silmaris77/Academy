# DEPRECATED - PRZENIESIONY DO PROFILE.PY
# 
# Ten plik jest przestarzały i został zastąpiony.
# Wszystkie funkcje z tego pliku zostały przeniesione do:
# views/profile.py
#
# Zakładka "Eksplorator" została usunięta z nawigacji.
# Wszystkie funkcje (Test Degena, Eksplorator Typów) są teraz dostępne
# w zakładce "Profil" jako pod-zakładki.
#
# Ten plik może zostać usunięty po potwierdzeniu, że aplikacja działa poprawnie.
#
# Data migracji: 2025-06-20
# Status: DEPRECATED - DO NOT USE

import streamlit as st

def show_degen_explorer():
    """DEPRECATED - Funkcja przeniesiona do views/profile.py"""
    st.error("⚠️ Ta funkcja została przeniesiona do zakładki Profil!")
    st.info("Przejdź do zakładki 'Profil' aby uzyskać dostęp do testu Degena i eksploratora typów.")
    if st.button("Przejdź do Profilu"):
        st.session_state.page = 'profile'
        st.rerun()

# Pozostałe funkcje zostały przeniesione do views/profile.py:
# - plot_radar_chart -> views/profile.py
# - show_degen_test_section -> views/profile.py  
# - show_degen_explorer_section -> views/profile.py
# - calculate_degen_scores -> views/profile.py
# - show_test_question -> views/profile.py
# - show_test_results -> views/profile.py
# - show_degen_types_explorer -> views/profile.py
# - show_degen_type_details -> views/profile.py
# - show_degen_type_card -> views/profile.py
