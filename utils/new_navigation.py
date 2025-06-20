# utils/new_navigation.py
import streamlit as st
from typing import Dict, List, Optional

class NewNavigationSystem:
    """
    Nowy system nawigacji oparty na prototypie HTML
    4 główne sekcje: START, NAUKA, PRAKTYKA, PROFIL
    """
    
    def __init__(self):
        self.sections = {
            "start": {
                "icon": "🏠",
                "label": "START", 
                "description": "Twój punkt wejścia",
                "subsections": [
                    "continue_lesson",
                    "daily_missions", 
                    "streak",
                    "progress_overview",
                    "statistics"
                ]
            },
            "learn": {
                "icon": "📚",
                "label": "NAUKA",
                "description": "Materiały edukacyjne",
                "subsections": [
                    "lessons",
                    "course_map",
                    "inspirations",
                    "my_notes"
                ]
            },
            "practice": {
                "icon": "⚡",
                "label": "PRAKTYKA", 
                "description": "Aplikacja wiedzy",
                "subsections": [
                    "lesson_exercises",
                    "daily_weekly_missions",
                    "lesson_quizzes", 
                    "flashcards",
                    "comprehensive_quiz"
                ]
            },
            "profile": {
                "icon": "👤",
                "label": "PROFIL",
                "description": "Twoja tożsamość",
                "subsections": [
                    "degen_test",
                    "achievements",
                    "statistics",
                    "rankings", 
                    "shop_equipment"
                ]
            }
        }
    
    def render_sidebar_navigation(self):
        """Renderuje sidebar z nową nawigacją"""
        st.sidebar.markdown("### 🧘‍♂️💰 ZenDegenAcademy")
        
        # Inicjalizacja domyślnej sekcji
        if 'current_section' not in st.session_state:
            st.session_state.current_section = 'start'
        
        # Renderowanie głównych sekcji
        for section_key, section_data in self.sections.items():
            
            # Przycisk sekcji
            if st.sidebar.button(
                f"{section_data['icon']} {section_data['label']}", 
                key=f"nav_{section_key}",
                use_container_width=True,
                type="primary" if st.session_state.current_section == section_key else "secondary"
            ):
                st.session_state.current_section = section_key
                st.session_state.current_subsection = None
                st.rerun()
        
        # Wylogowanie na dole
        st.sidebar.markdown("---")
        if st.sidebar.button("🚪 WYLOGUJ", key="logout_nav", use_container_width=True):
            return "logout"
        
        return st.session_state.current_section
    
    def render_mobile_navigation(self):
        """Renderuje bottom navigation dla mobile"""
        # Ten kod będzie używany w kontekstach mobilnych
        pass
    
    def get_section_title(self, section: str) -> str:
        """Zwraca tytuł sekcji"""
        section_data = self.sections.get(section, {})
        return f"{section_data.get('icon', '🏠')} {section_data.get('label', 'START')} - {section_data.get('description', '')}"
    
    def render_section_content(self, section: str):
        """Renderuje zawartość sekcji"""
        if section == "start":
            self._render_start_section()
        elif section == "learn":
            self._render_learn_section()
        elif section == "practice":
            self._render_practice_section()
        elif section == "profile":
            self._render_profile_section()
    
    def _render_start_section(self):
        """Renderuje sekcję START"""
        st.title("🏠 START - Twój Punkt Wejścia")
        st.markdown("*Co robimy dziś? Sprawdź swoje cele i kontynuuj naukę*")
        
        # Quick Actions
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### 🎯 Kontynuuj Lekcję")
                if 'current_lesson' in st.session_state:
                    lesson_info = st.session_state.get('current_lesson', 'B1C1L1')
                    st.markdown(f"**{lesson_info}**: Analiza Fundamentalna")
                    st.markdown("*pozostało ~15 min*")
                    if st.button("▶️ Kontynuuj", key="continue_lesson_start"):
                        st.session_state.current_section = 'learn'
                        st.session_state.page = 'lesson'
                        st.rerun()
                else:
                    st.markdown("Brak aktywnej lekcji")
                    if st.button("🎯 Rozpocznij naukę", key="start_learning"):
                        st.session_state.current_section = 'learn'
                        st.rerun()
        
        with col2:
            with st.container(border=True):
                st.markdown("### ✅ Dzisiejsze Misje")                # Importujemy system misji
                try:
                    # from utils.daily_missions import get_daily_missions_status
                    # missions_status = get_daily_missions_status()
                    # completed = missions_status.get('completed', 0)
                    # total = missions_status.get('total', 3)
                    # st.markdown(f"**{completed}/{total}** zadania wykonane")
                    
                    # Temporary fallback
                    st.markdown("**2/3** zadania wykonane")
                    if st.button("🎯 Zobacz misje", key="view_missions_start"):
                        st.session_state.current_section = 'practice'
                        st.rerun()
                except ImportError:
                    st.markdown("**2/3** zadania wykonane")
                    if st.button("🎯 Zobacz misje", key="view_missions_start_fallback"):
                        st.session_state.current_section = 'practice'
                        st.rerun()
        
        # Streak i Postęp
        col3, col4 = st.columns(2)
        with col3:
            with st.container(border=True):
                st.markdown("### 🔥 Streak")
                streak_days = st.session_state.get('streak_days', 7)
                st.markdown(f"**{streak_days} dni z rzędu**")
                st.markdown("*Fantastycznie! Utrzymaj momentum*")
        
        with col4:
            with st.container(border=True):
                st.markdown("### 📊 Twój Postęp")
                level = st.session_state.get('user_level', 7)
                xp = st.session_state.get('total_xp', 1245)
                xp_to_next = st.session_state.get('xp_to_next_level', 255)
                st.markdown(f"**Level {level}** - {xp} XP")
                st.markdown(f"*do następnego: {xp_to_next} XP*")
          # Statystyki
        st.markdown("### 📈 Statystyki")
        stat_cols = st.columns(4)
        
        stats = {
            "Ukończone lekcje": st.session_state.get('completed_lessons', 12),
            "Zdobyte XP": st.session_state.get('total_xp', 1245), 
            "Dni z rzędu": st.session_state.get('streak_days', 7),
            "Zdobyte odznaki": st.session_state.get('badges_count', 3)
        }
        
        for i, (label, value) in enumerate(stats.items()):
            with stat_cols[i]:
                st.metric(label, value)
    
    def _render_learn_section(self):
        """Renderuje sekcję NAUKA - używa enhanced learn view"""
        try:
            # Use the enhanced learn view with integrated skills
            from views.learn import show_learn
            show_learn()
        except Exception as e:
            # Fallback to the original learn section if there's an error
            st.title("📚 NAUKA - Materiały Edukacyjne")
            st.markdown("*Lekcje, kursy i inspiracje w jednym miejscu*")
            st.error(f"Błąd ładowania systemu nauki: {e}")
            
            # Tabs dla podsekcji
            tab1, tab2, tab3, tab4 = st.tabs([
                "📖 Lekcje", 
                "🗺️ Mapa Kursu", 
                "💡 Inspiracje",
                "📝 Moje Notatki"
            ])
            
            with tab1:
                st.markdown("### 📖 Lekcje")
                st.markdown("**6-etapowa struktura**: Wstęp → Opening Case Study → Quiz Samooceny → Materiał → Closing Case Study → Podsumowanie")
                
                if st.button("🎯 Przejdź do lekcji", key="go_to_lessons"):
                    st.session_state.page = 'lesson'
                    st.rerun()
            
            with tab2:
                st.markdown("### 🗺️ Mapa Kursu")
                st.markdown("Interaktywna wizualizacja całego programu nauki")
                
                if st.button("🗺️ Otwórz mapę", key="open_course_map"):
                    st.session_state.page = 'skills'
                    st.rerun()
            
            with tab3:
                st.markdown("### 💡 Inspiracje")
                st.markdown("**Blog** • **Tutoriale** • **Przewodnik po typach degenów** • **Ciekawostki**")
                
                if st.button("🎭 Przewodnik po degenach", key="degen_guide"):
                    st.session_state.page = 'degen_explorer'
                    st.rerun()
            
            with tab4:
                st.markdown("### 📝 Moje Notatki")
                st.markdown("Zapisane fragmenty i własne spostrzeżenia")
                
                # Tutaj można dodać funkcjonalność notatek
                if st.text_area("Dodaj notatkę", key="add_note"):
                    st.success("Notatka zapisana!")
    
    def _render_practice_section(self):
        """Renderuje sekcję PRAKTYKA"""
        st.title("⚡ PRAKTYKA - Aplikacja Wiedzy")
        st.markdown("*Zadania praktyczne, misje i wdrażanie wiedzy*")
        
        # Tabs dla podsekcji
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🎯 Ćwiczenia",
            "📅 Misje", 
            "❓ Quizy",
            "🃏 Flashcards",
            "🏆 Test Kompletny"
        ])
        
        with tab1:
            st.markdown("### 🎯 Ćwiczenia do Lekcji")
            st.markdown("**Autorefleksja** • **Analiza** • **Wdrożenie**")
            
            if st.button("📝 Przejdź do ćwiczeń", key="go_to_exercises"):
                st.session_state.page = 'implementation'
                st.rerun()
        
        with tab2:
            st.markdown("### 📅 Misje Dzienne/Tygodniowe")
            
            # Misje dnia - sekcja specjalna
            with st.container(border=True):
                st.markdown("#### 🎯 Misje Dnia")
                
                missions = [
                    {"name": "Market Pulse Check", "time": "10 min", "status": "completed", "xp": 75},
                    {"name": "Investment Journal", "time": "5 min", "status": "pending", "xp": 40},
                    {"name": "Risk Analysis Challenge", "time": "15 min", "status": "locked", "xp": 120}
                ]
                
                completed = sum(1 for m in missions if m["status"] == "completed")
                total = len(missions)
                
                st.markdown(f"**{completed}/{total} ukończone**")
                
                for mission in missions:
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        icon = "✅" if mission["status"] == "completed" else "🔄" if mission["status"] == "pending" else "🔒"
                        st.markdown(f"{icon} **{mission['name']}** ({mission['time']})")
                    
                    with col2:
                        st.markdown(f"**+{mission['xp']} XP**")
                    
                    with col3:
                        if mission["status"] == "pending":
                            if st.button("START", key=f"start_{mission['name'].replace(' ', '_')}"):
                                st.success(f"Rozpoczęto: {mission['name']}")
                
                # Progress bar
                progress = completed / total
                st.progress(progress)
                st.markdown(f"**Streak: 🔥 7 dni** • Następna misja odblokowana o 16:00")
        
        with tab3:
            st.markdown("### ❓ Quizy do Lekcji")
            st.markdown("Sprawdź swoją wiedzę po każdej lekcji")
            
            # Lista dostępnych quizów
            if st.button("🎯 Otwórz quiz", key="open_quiz"):
                st.session_state.page = 'lesson'  # Można przekierować do odpowiedniej sekcji
                st.rerun()
        
        with tab4:
            st.markdown("### 🃏 Flashcards")
            st.markdown("Powtórka kluczowych pojęć z całego kursu")
            
            if st.button("🃏 Rozpocznij powtórkę", key="start_flashcards"):
                st.info("Funkcja flashcards - w przygotowaniu")
        
        with tab5:
            st.markdown("### 🏆 Quiz dla Całego Kursu")
            st.markdown("Kompleksowe sprawdzenie wiedzy - 50 pytań")
            
            if st.button("🏆 Rozpocznij test", key="start_comprehensive_quiz"):
                st.info("Kompleksowy quiz - w przygotowaniu")
        
        # Statystyki praktyki
        st.markdown("### 📊 Statystyki Praktyki")
        practice_cols = st.columns(4)
        
        practice_stats = {
            "Misje wykonane": 25,
            "Quizy ukończone": 8,
            "Flashcards przejrzane": 156,
            "Skuteczność": "92%"
        }
        
        for i, (label, value) in enumerate(practice_stats.items()):
            with practice_cols[i]:
                st.metric(label, value)
    
    def _render_profile_section(self):
        """Renderuje sekcję PROFIL"""
        st.title("👤 PROFIL - Twoja Tożsamość Degena")
        st.markdown("*Test degena, osiągnięcia, statystyki i rozwój*")
        
        # Tabs dla podsekcji
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🧬 Test Degena",
            "🏆 Osiągnięcia", 
            "📊 Statystyki",
            "🥇 Rankingi",
            "🛍️ Sklep"
        ])
        
        with tab1:
            st.markdown("### 🧬 Test na Typ Degena")
            degen_type = st.session_state.get('degen_type', 'Aggressive Investor')
            st.markdown(f"**Twój typ**: {degen_type}")
            
            if st.button("🧬 Przejdź do testu", key="go_to_degen_test"):
                st.session_state.page = 'degen_explorer'
                st.rerun()
        
        with tab2:
            st.markdown("### 🏆 Osiągnięcia")
            badges_count = st.session_state.get('badges_count', 15)
            st.markdown(f"**{badges_count}/50** odznak zdobytych")
            
            if st.button("🏆 Zobacz osiągnięcia", key="view_achievements"):
                st.session_state.page = 'profile'
                st.rerun()
        
        with tab3:
            st.markdown("### 📊 Statystyki")
            st.markdown("Szczegółowe dane o Twoim postępie")
            
            if st.button("📊 Szczegółowe statystyki", key="detailed_stats"):
                st.session_state.page = 'profile'
                st.rerun()
        
        with tab4:
            st.markdown("### 🥇 Rankingi")
            st.markdown("**#3** w klasie, **#45** globalnie")
            
            if st.button("🥇 Zobacz rankingi", key="view_rankings"):
                st.info("Rankingi - w przygotowaniu")
        
        with tab5:
            st.markdown("### 🛍️ Sklep i Ekwipunek")
            degencoins = st.session_state.get('degencoins', 150)
            st.markdown(f"**{degencoins} DegenCoins** do wydania")
            
            # Mini sklep preview
            with st.container(border=True):
                st.markdown("#### 🛒 Dostępne przedmioty:")
                
                shop_cols = st.columns(3)
                items = [
                    {"name": "XP Booster", "icon": "🎯", "price": 50},
                    {"name": "Hint Token", "icon": "🔮", "price": 25}, 
                    {"name": "Premium Theme", "icon": "⭐", "price": 100}
                ]
                
                for i, item in enumerate(items):
                    with shop_cols[i]:
                        st.markdown(f"**{item['icon']} {item['name']}**")
                        st.markdown(f"*{item['price']} DC*")
                        if st.button("Kup", key=f"buy_{item['name'].replace(' ', '_')}"):
                            if degencoins >= item['price']:
                                st.success(f"Kupiono: {item['name']}")
                            else:
                                st.error("Brak wystarczających DegenCoins")
            
            if st.button("🛍️ Przejdź do sklepu", key="go_to_shop"):
                st.session_state.page = 'shop'
                st.rerun()
        
        # Statystyki profilu
        st.markdown("### 📊 Statystyki Profilu")
        profile_cols = st.columns(4)
        
        profile_stats = {
            "Aktualny Level": st.session_state.get('user_level', 7),
            "DegenCoins": st.session_state.get('degencoins', 150),
            "Zdobyte odznaki": st.session_state.get('badges_count', 15),
            "Miejsce w klasie": "#3"
        }
        
        for i, (label, value) in enumerate(profile_stats.items()):
            with profile_cols[i]:
                st.metric(label, value)

# Funkcja pomocnicza do inicjalizacji nowego systemu
def initialize_new_navigation():
    """Inicjalizuje nowy system nawigacji"""
    if 'new_navigation' not in st.session_state:
        st.session_state.new_navigation = NewNavigationSystem()
    return st.session_state.new_navigation
