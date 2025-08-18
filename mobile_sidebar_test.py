#!/usr/bin/env python3
"""
Test UI dla automatycznego zamykania sidebar na mobile.
Uruchom: streamlit run mobile_sidebar_test.py
"""

import streamlit as st
import sys
import os

# Dodaj katalog główny do ścieżki
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.components import navigation_menu, zen_button

# Konfiguracja strony
st.set_page_config(
    page_title="Mobile Sidebar Test",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicjalizacja session state
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = True
if 'username' not in st.session_state:
    st.session_state.username = 'testuser'

# Sidebar z nawigacją
with st.sidebar:
    st.markdown("### 📱 Test Mobile Sidebar")
    st.markdown("Na urządzeniu mobilnym (szerokość < 768px) sidebar powinien się automatycznie zamknąć po kliknięciu w nawigację.")
    
    # Wywołaj funkcję nawigacji z nowym skryptem auto-close
    navigation_menu()

# Główna treść
st.title("📱 Test Automatycznego Zamykania Sidebar")

st.markdown("""
## 🎯 Cel testu

Sprawdzenie czy sidebar automatycznie się zamyka na urządzeniach mobilnych po kliknięciu w dowolną opcję nawigacji.

## 📋 Instrukcje testowania

1. **Otwórz narzędzia deweloperskie** (F12)
2. **Przełącz na widok mobilny** (Ctrl+Shift+M lub ikona telefonu)
3. **Ustaw szerokość na < 768px** (np. iPhone, Samsung Galaxy)
4. **Otwórz sidebar** (kliknij w strzałkę lub przycisk menu)
5. **Kliknij w dowolną opcję nawigacji** w sidebar
6. **Sprawdź czy sidebar się automatycznie zamknął**

## ✅ Oczekiwane zachowanie

- **Desktop (≥ 768px):** Sidebar pozostaje otwarty po nawigacji
- **Mobile (< 768px):** Sidebar automatycznie się zamyka po kliknięciu w nawigację

## 🔧 Mechanizm działania

Skrypt JavaScript:
- Wykrywa szerokość ekranu < 768px
- Nasłuchuje na kliknięcia w przyciski nawigacji
- Automatycznie klika przycisk zamykania sidebar po nawigacji
- Używa MutationObserver do wykrywania nowych przycisków

## 📊 Status testu
""")

current_page = st.session_state.get('page', 'dashboard')
st.success(f"✅ Aktualna strona: **{current_page}**")

# Dodaj informacje o viewport
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    const updateViewportInfo = () => {
        const width = window.innerWidth;
        const height = window.innerHeight;
        const isMobile = width < 768;
        
        const statusElement = document.getElementById('viewport-status');
        if (statusElement) {
            statusElement.innerHTML = `
                <div style="background: ${isMobile ? '#e8f5e8' : '#f0f0f0'}; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                    <strong>Viewport:</strong> ${width}x${height}px<br>
                    <strong>Urządzenie:</strong> ${isMobile ? '📱 Mobile' : '🖥️ Desktop'}<br>
                    <strong>Auto-close:</strong> ${isMobile ? '✅ Aktywny' : '❌ Nieaktywny'}
                </div>
            `;
        }
    };
    
    updateViewportInfo();
    window.addEventListener('resize', updateViewportInfo);
});
</script>

<div id="viewport-status"></div>
""", unsafe_allow_html=True)

st.markdown("---")

# Dodaj testowe przyciski
col1, col2, col3 = st.columns(3)

with col1:
    if zen_button("🏠 Test Dashboard", key="test_dashboard", use_container_width=True):
        st.session_state.page = 'dashboard'
        st.rerun()

with col2:
    if zen_button("📚 Test Lekcje", key="test_lessons", use_container_width=True):
        st.session_state.page = 'lesson'
        st.rerun()

with col3:
    if zen_button("👤 Test Profil", key="test_profile", use_container_width=True):
        st.session_state.page = 'profile'
        st.rerun()

st.info("💡 **Tip:** Te przyciski w głównej treści nie powodują zamykania sidebar - tylko przyciski w sidebar mają tę funkcjonalność.")

# Dodaj szczegóły techniczne
with st.expander("🔍 Szczegóły techniczne"):
    st.code("""
    // Główna funkcja zamykania sidebar
    function closeSidebarOnMobile() {
        if (window.innerWidth < 768) {
            const sidebarCloseButton = parent.document.querySelector('[data-testid="collapsedControl"]');
            if (sidebarCloseButton) {
                sidebarCloseButton.click();
            }
        }
    }
    
    // Automatyczne wykrywanie przycisków nawigacji
    // Używa MutationObserver do śledzenia zmian DOM
    // Obsługuje różne selektory przycisków Streamlit
    """, language="javascript")
    
    st.markdown("**Testowane selektory przycisków:**")
    selectors = [
        "`.stSidebar [data-testid='stButton'] button`",
        "`.stSidebar button[kind='primary']`", 
        "`.stSidebar button[kind='secondary']`",
        "`.stSidebar .stButton button`",
        "`[data-testid='stSidebar'] button`"
    ]
    for selector in selectors:
        st.code(selector)
