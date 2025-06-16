# main_new.py - Nowa wersja głównego pliku aplikacji
import streamlit as st
import os
import sys
import traceback
from datetime import datetime
from config.settings import PAGE_CONFIG

# Konfiguracja strony musi być pierwsza
st.set_page_config(**PAGE_CONFIG)

# Ścieżka do głównego katalogu aplikacji
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.append(APP_DIR)

# Importy z obsługą błędów
IMPORTS_OK = True
import_error = ""
import_traceback = ""

try:
    from utils.session import init_session_state, clear_session
    from utils.new_navigation import initialize_new_navigation
    from views.login import show_login_page
    
    # Import starych views (będą stopniowo zastępowane)
    from views.dashboard import show_dashboard  
    from views.lesson import show_lesson
    from views.profile import show_profile
    from views.degen_explorer import show_degen_explorer
    from views.skills_new import show_skill_tree
    from views.admin import show_admin_dashboard
    from views.implementation import show_implementation
    
except Exception as e:
    IMPORTS_OK = False
    import_error = str(e)
    import_traceback = traceback.format_exc()
    
    # Create fallback functions
    def init_session_state():
        if 'logged_in' not in st.session_state:
            st.session_state.logged_in = False
    
    def clear_session():
        for key in list(st.session_state.keys()):
            del st.session_state[key]
    
    def show_login_page():
        st.error("Import error - login functionality unavailable")
    
    def initialize_new_navigation():
        return None
    
    def show_dashboard():
        st.error("Dashboard unavailable due to import errors")
    
    def show_lesson():
        st.error("Lessons unavailable due to import errors")
    
    def show_profile():
        st.error("Profile unavailable due to import errors")
    
    def show_degen_explorer():
        st.error("Degen Explorer unavailable due to import errors")
    
    def show_skill_tree():
        st.error("Skills unavailable due to import errors")
    
    def show_admin_dashboard():
        st.error("Admin unavailable due to import errors")
    
    def show_implementation():
        st.error("Implementation unavailable due to import errors")

# Załaduj CSS
def load_css():
    """Ładuje style CSS"""
    css_path = os.path.join(os.path.dirname(__file__), "static", "css", "style.css")
    try:
        with open(css_path, "r", encoding="utf-8") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Nie znaleziono pliku CSS - używam domyślnych stylów")

def initialize_user_data():
    """Inicjalizuje dane użytkownika dla nowego systemu"""
    defaults = {
        'current_section': 'start',
        'current_subsection': None,
        'streak_days': 7,
        'user_level': 7,
        'total_xp': 1245,
        'xp_to_next_level': 255,
        'completed_lessons': 12,
        'badges_count': 15,
        'degencoins': 150,
        'degen_type': 'Aggressive Investor',
        'current_lesson': 'B1C1L4'
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def handle_legacy_routing():
    """Obsługuje stary system routingu dla zachowania kompatybilności"""
    legacy_page = st.session_state.get('page', 'dashboard')
    
    # Mapowanie starych stron na nowe sekcje
    page_to_section = {
        'dashboard': 'start',
        'lesson': 'learn', 
        'implementation': 'practice',
        'degen_explorer': 'profile',
        'profile': 'profile',
        'skills': 'learn',
        'shop': 'profile',
        'admin': 'start'
    }
    
    if legacy_page in page_to_section:
        st.session_state.current_section = page_to_section[legacy_page]

def show_new_interface():
    """Pokazuje nowy interfejs oparty na prototypie"""
    
    # Inicjalizacja nowego systemu nawigacji
    nav_system = initialize_new_navigation()
    
    # Renderowanie nawigacji w sidebar
    current_section = nav_system.render_sidebar_navigation()
    
    # Obsługa wylogowania
    if current_section == "logout":
        clear_session()
        st.rerun()
        return
    
    # Header z informacjami o użytkowniku
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown(f"### Witaj, **{st.session_state.username}**! 👋")
    with col2:
        st.markdown(f"**Level {st.session_state.user_level}** | **{st.session_state.total_xp} XP**")
    with col3:
        st.markdown(f"**🔥 {st.session_state.streak_days} dni** | **💰 {st.session_state.degencoins} DC**")
    
    st.markdown("---")
    
    # Renderowanie zawartości sekcji
    if current_section == 'start':
        nav_system._render_start_section()
    elif current_section == 'learn':
        nav_system._render_learn_section()
    elif current_section == 'practice':
        nav_system._render_practice_section() 
    elif current_section == 'profile':
        nav_system._render_profile_section()

def show_legacy_interface():
    """Pokazuje stary interfejs dla kompatybilności wstecznej"""
    
    # Stary system nawigacji w sidebar
    with st.sidebar:
        st.markdown(f"### Witaj, {st.session_state.username}!")
        
        # Import starej nawigacji
        try:
            from utils.components import navigation_menu
            navigation_menu()
        except ImportError:
            # Fallback navigation
            if st.button("🏠 Dashboard"):
                st.session_state.page = 'dashboard'
                st.rerun()
            if st.button("📚 Lekcje"):
                st.session_state.page = 'lesson'
                st.rerun()
            if st.button("⚡ Praktyka"):
                st.session_state.page = 'implementation'
                st.rerun()
            if st.button("👤 Profil"):
                st.session_state.page = 'profile'
                st.rerun()
        
        # Przycisk wylogowania
        if st.button("🚪 Wyloguj się", key="logout_legacy"):
            clear_session()
            st.rerun()
    
    # Routing do starych widoków
    page = st.session_state.get('page', 'dashboard')
    
    if page == 'dashboard':
        show_dashboard()
    elif page == 'lesson':
        show_lesson()
    elif page == 'profile':
        show_profile()
    elif page == 'degen_explorer':
        show_degen_explorer()
    elif page == 'skills':
        show_skill_tree()
    elif page == 'implementation':
        show_implementation()
    elif page == 'shop':
        try:
            from views.shop_new import show_shop
            show_shop()
        except ImportError:
            st.error("Błąd ładowania sklepu")
    elif page == 'admin':
        show_admin_dashboard()

def main():
    """Główna funkcja aplikacji"""
    
    # Check if imports were successful
    if not IMPORTS_OK:
        st.error(f"Błąd podczas importowania modułów: {import_error}")
        st.code(import_traceback)
        st.stop()
        return
    
    # Ładowanie CSS
    load_css()
    
    # Inicjalizacja session state
    init_session_state()
    
    # Inicjalizacja danych użytkownika dla nowego systemu
    initialize_user_data()
    
    # Jeśli użytkownik nie jest zalogowany - pokaż stronę logowania
    if not st.session_state.logged_in:
        show_login_page()
        return
    
    # Sprawdzenie czy użytkownik chce używać nowego interfejsu
    use_new_interface = st.session_state.get('use_new_interface', True)
    
    # Toggle między starym a nowym interfejsem (tymczasowo dla testów)
    with st.sidebar:
        st.markdown("---")
        new_interface = st.checkbox(
            "🆕 Nowy interfejs", 
            value=use_new_interface,
            help="Przełącz między starym a nowym interfejsem"
        )
        
        if new_interface != use_new_interface:
            st.session_state.use_new_interface = new_interface
            st.rerun()
    
    # Obsługa kompatybilności wstecznej
    if not use_new_interface:
        handle_legacy_routing()
    
    # Wyświetlenie odpowiedniego interfejsu
    if use_new_interface:
        show_new_interface()
    else:
        show_legacy_interface()

if __name__ == "__main__":
    main()
