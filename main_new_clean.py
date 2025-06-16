# main_new.py - Nowa wersja głównego pliku aplikacji (Clean Version)
import streamlit as st
import os
import sys
import traceback
from datetime import datetime

# Konfiguracja strony musi być pierwsza
try:
    from config.settings import PAGE_CONFIG
    st.set_page_config(**PAGE_CONFIG)
except:
    st.set_page_config(
        page_title="ZenDegenAcademy",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

# Ścieżka do głównego katalogu aplikacji
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.append(APP_DIR)

def show_error_page(error_msg, error_traceback):
    """Show error page when imports fail"""
    st.error("🚨 Błąd ładowania aplikacji")
    st.markdown("### Szczegóły błędu:")
    st.code(error_msg)
    
    with st.expander("Pełny ślad błędu"):
        st.code(error_traceback)
    
    st.markdown("### Możliwe rozwiązania:")
    st.markdown("""
    1. **Sprawdź instalację Streamlit**: `pip install streamlit --upgrade`
    2. **Sprawdź zależności**: `pip install -r requirements.txt`
    3. **Sprawdź pliki konfiguracyjne**: Upewnij się, że wszystkie moduły są dostępne
    4. **Uruchom starą wersję**: `streamlit run main.py`
    """)

def load_css():
    """Ładuje style CSS"""
    css_path = os.path.join(os.path.dirname(__file__), "static", "css", "style.css")
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # Use some basic CSS
        st.markdown("""
        <style>
        .main > div {
            padding-top: 2rem;
        }
        </style>
        """, unsafe_allow_html=True)

def simple_login_page():
    """Simple login page fallback"""
    st.title("🧠 ZenDegenAcademy")
    st.markdown("### Zaloguj się, aby kontynuować")
    
    username = st.text_input("Nazwa użytkownika:")
    password = st.text_input("Hasło:", type="password")
    
    if st.button("Zaloguj się"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Zalogowano pomyślnie!")
            st.rerun()
        else:
            st.error("Proszę podać nazwę użytkownika i hasło")

def simple_dashboard():
    """Simple dashboard fallback"""
    st.title(f"🏠 Dashboard - Witaj {st.session_state.get('username', 'User')}!")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Level", "7")
    with col2:
        st.metric("XP", "1245")
    with col3:
        st.metric("Streak", "7 dni")
    with col4:
        st.metric("DegenCoins", "150")
    
    st.markdown("---")
    st.markdown("### 🎯 Daily Missions")
    st.info("System misji zostanie wkrótce przywrócony.")
    
    st.markdown("### 📚 Continue Learning")
    if st.button("📖 Przejdź do lekcji"):
        st.session_state.page = 'lessons'
        st.rerun()

def simple_navigation():
    """Simple navigation fallback"""
    st.sidebar.markdown(f"### Witaj, {st.session_state.get('username', 'User')}!")
    
    if st.sidebar.button("🏠 Dashboard"):
        st.session_state.page = 'dashboard'
        st.rerun()
    
    if st.sidebar.button("📚 Lekcje"):
        st.session_state.page = 'lessons'
        st.rerun()
    
    if st.sidebar.button("⚡ Praktyka"):
        st.session_state.page = 'practice'
        st.rerun()
    
    if st.sidebar.button("👤 Profil"):
        st.session_state.page = 'profile'
        st.rerun()
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Wyloguj się"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

def simple_lessons_page():
    """Simple lessons page"""
    st.title("📚 Lekcje")
    st.info("System lekcji zostanie wkrótce przywrócony w nowej formie.")
    
    st.markdown("### Dostępne kursy:")
    st.markdown("- 🎯 Block 1: Podstawy inwestowania")
    st.markdown("- 🧠 Block 2: Psychologia rynku") 
    st.markdown("- 💼 Block 3: Zarządzanie portfelem")

def simple_practice_page():
    """Simple practice page"""
    st.title("⚡ Praktyka")
    st.markdown("*Zastosuj wiedzę w rzeczywistych wyzwaniach*")
    
    st.markdown("### 🎯 Misje Praktyczne")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Wszystkie misje", 3)
    with col2:
        st.metric("Ukończone", 1)
    with col3:
        st.metric("Zdobyte XP", 75)
    with col4:
        st.metric("Postęp", "33%")
    
    st.markdown("---")
    st.info("System misji praktycznych zostanie wkrótce przywrócony.")

def simple_profile_page():
    """Simple profile page"""
    st.title("👤 Profil")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### 🎭 Avatar")
        st.markdown("🧠")
    
    with col2:
        st.markdown("### Statystyki")
        st.markdown(f"**Użytkownik:** {st.session_state.get('username', 'User')}")
        st.markdown("**Typ Degen:** Aggressive Investor")
        st.markdown("**Level:** 7")
        st.markdown("**XP:** 1245")
        st.markdown("**Streak:** 7 dni")

def main():
    """Główna funkcja aplikacji"""
    
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'page' not in st.session_state:
        st.session_state.page = 'dashboard'
    if 'username' not in st.session_state:
        st.session_state.username = 'User'
    
    # Load CSS
    load_css()
    
    # Try to import advanced modules
    try:
        from utils.session import init_session_state, clear_session
        from views.login import show_login_page
        from views.dashboard import show_dashboard
        from views.implementation import show_implementation
        
        # Advanced functionality available
        init_session_state()
        
        if not st.session_state.logged_in:
            show_login_page()
            return
        
        # Try to load new navigation
        try:
            from utils.new_navigation import initialize_new_navigation
            nav_system = initialize_new_navigation()
            current_section = nav_system.render_sidebar_navigation()
            
            if current_section == "logout":
                clear_session()
                st.rerun()
                return
            
            # New interface
            if current_section == 'start':
                show_dashboard()
            elif current_section == 'practice':
                show_implementation()
            else:
                st.info(f"Sekcja '{current_section}' w budowie...")
                show_dashboard()
                
        except Exception as e:
            # Fallback to simple navigation
            st.warning("⚠️ Używam uproszczonej nawigacji")
            simple_navigation()
            
            page = st.session_state.get('page', 'dashboard')
            if page == 'dashboard':
                try:
                    show_dashboard()
                except:
                    simple_dashboard()
            elif page == 'practice':
                try:
                    show_implementation()
                except:
                    simple_practice_page()
            else:
                simple_dashboard()
        
    except Exception as e:
        # Complete fallback mode
        st.warning("⚠️ Używam trybu awaryjnego - podstawowe funkcje")
        
        if not st.session_state.logged_in:
            simple_login_page()
            return
        
        simple_navigation()
        
        page = st.session_state.get('page', 'dashboard')
        if page == 'dashboard':
            simple_dashboard()
        elif page == 'lessons':
            simple_lessons_page()
        elif page == 'practice':
            simple_practice_page()
        elif page == 'profile':
            simple_profile_page()
        else:
            simple_dashboard()

if __name__ == "__main__":
    main()
