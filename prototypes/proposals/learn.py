# views/learn.py
"""
Learn View - Nauka
Połączona sekcja dla Lekcji i Umiejętności
"""

import streamlit as st
from utils.components import zen_header

def show_learn():
    """Display the combined learn section with lessons and skills"""
      # Page header
    zen_header("📚 Nauka", "Lekcje i umiejętności zintegrowane w jednym miejscu - kompletna ścieżka rozwoju")
    
    # Check if user is logged in
    if not st.session_state.get('logged_in', False):
        st.warning("⚠️ Musisz być zalogowany, aby uzyskać dostęp do materiałów edukacyjnych.")
        return
      # Create tabs for different learning sections
    tab1, tab2, tab3 = st.tabs(["🎓 Lekcje", "🗺️ Mapa Kursu", "🌳 Umiejętności"])
    
    with tab1:
        st.markdown("### 🎓 Materiały kursu i Umiejętności")
        st.markdown("Lekcje, materiały edukacyjne oraz interaktywne drzewo umiejętności w jednym miejscu")
        
        # Create sub-tabs within the Lessons tab to include Skills content
        lessons_subtab1, lessons_subtab2 = st.tabs(["📚 Lekcje", "🌳 Umiejętności"])
        
        with lessons_subtab1:
            st.markdown("#### 📚 Dostępne lekcje")
            # Use existing lesson functionality
            try:
                show_lesson_content()
            except Exception as e:
                st.error(f"Błąd ładowania lekcji: {e}")
                # Fallback content
                st.info("System lekcji jest tymczasowo niedostępny.")
                
                # Show basic lesson structure
                st.markdown("#### Dostępne lekcje:")
                
                lessons = [
                    {"id": "B1C1L1", "title": "Strach przed stratą", "tag": "Psychologia inwestowania"},
                    {"id": "B1C1L4", "title": "Emocjonalna zmienność", "tag": "Zarządzanie emocjami"}
                ]
                
                for lesson in lessons:
                    with st.container(border=True):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.markdown(f"**{lesson['title']}**")
                            st.markdown(f"*{lesson['tag']}*")
                        with col2:
                            if st.button("Rozpocznij", key=f"lesson_{lesson['id']}"):
                                st.session_state.selected_lesson = lesson['id']
                                st.session_state.page = 'lesson'
                                st.rerun()
        
        with lessons_subtab2:
            st.markdown("#### 🌳 Drzewo umiejętności")
            st.markdown("Śledź swój postęp i rozwijaj kompetencje")
            
            # Include the complete skills functionality here
            try:
                show_skills_in_lessons_tab()
            except Exception as e:
                st.error(f"Błąd ładowania umiejętności: {e}")
                # Fallback skills content
                st.info("System umiejętności jest tymczasowo niedostępny.")
                
                # Basic skills overview
                skills_categories = {
                    "Analiza fundamentalna": ["Analiza sprawozdań", "Wycena spółek", "Analiza sektorowa"],
                    "Analiza techniczna": ["Wzorce świecowe", "Wskaźniki techniczne", "Teoria Dow"],
                    "Zarządzanie ryzykiem": ["Stop loss", "Position sizing", "Dywersyfikacja"],
                    "Psychologia": ["Kontrola emocji", "Dyscyplina", "Długoterminowe myślenie"]
                }
                
                for category, skills in skills_categories.items():
                    with st.expander(f"📂 {category}"):
                        for skill in skills:
                            progress = st.slider(skill, 0, 100, 25, disabled=True)
    
    with tab2:
        st.markdown("### 🗺️ Interaktywna mapa kursu")
        st.markdown("Wizualna reprezentacja struktury całego kursu")
        
        # Check if course map is available
        try:
            from utils.course_map import create_course_structure_map, show_course_statistics
            
            # Course statistics
            st.markdown("#### 📊 Statystyki kursu")
            show_course_statistics()
            
            st.markdown("---")
            
            # Course map options
            map_type = st.selectbox(
                "Wybierz typ mapy:",
                ["Uproszczona mapa", "Pełna struktura"],
                help="Uproszczona mapa pokazuje główną strukturę, pełna zawiera wszystkie lekcje"
            )
            
            if map_type == "Uproszczona mapa":
                from utils.course_map import create_simplified_course_map
                create_simplified_course_map()
            else:
                create_course_structure_map()
                
        except ImportError:
            st.info("🗺️ Mapa kursu zostanie wkrótce dodana")
            
            # Fallback course overview
            st.markdown("#### Struktura kursu:")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Moduły", "5")
            with col2:
                st.metric("Kategorie", "15") 
            with col3:
                st.metric("Lekcje", "150+")
            with col4:
                st.metric("Ukończone", "2")
            
            # Basic course structure
            with st.expander("🏗️ Struktura kursu", expanded=True):
                st.markdown("""
                **Block 1: Podstawy inwestowania**
                - C1: Psychologia inwestowania
                  - L1: Strach przed stratą ✅
                  - L4: Emocjonalna zmienność ✅
                - C2: Analiza fundamentalna
                - C3: Analiza techniczna
                
                **Block 2: Zarządzanie portfelem**
                - C1: Dywersyfikacja
                - C2: Zarządzanie ryzykiem
                - C3: Optymalizacja portfela
                  **Block 3: Psychologia rynku**
                - C1: Behawioralne finanse
                - C2: Emocje w inwestowaniu
                - C3: Pułapki mentalne
                """)
    
    with tab3:
        st.markdown("### 🌳 Drzewo umiejętności (rozszerzone)")
        st.markdown("Zaawansowany widok umiejętności z mapą kursu i szczegółowymi statystykami")
        
        # Use existing skills functionality - full view with all tabs
        try:
            show_skill_tree_content()
        except Exception as e:
            st.error(f"Błąd ładowania umiejętności: {e}")
            # Fallback skills content
            st.info("System umiejętności jest tymczasowo niedostępny.")
            
            # Basic skills overview
            skills_categories = {
                "Analiza fundamentalna": ["Analiza sprawozdań", "Wycena spółek", "Analiza sektorowa"],
                "Analiza techniczna": ["Wzorce świecowe", "Wskaźniki techniczne", "Teoria Dow"],
                "Zarządzanie ryzykiem": ["Stop loss", "Position sizing", "Dywersyfikacja"],
                "Psychologia": ["Kontrola emocji", "Dyscyplina", "Długoterminowe myślenie"]
            }
            
            for category, skills in skills_categories.items():
                with st.expander(f"📂 {category}"):
                    for skill in skills:
                        progress = st.slider(skill, 0, 100, 25, disabled=True)

def show_lesson_content():
    """Display lesson content (fallback if lesson view import fails)"""
    # This will be called from the lesson tab
    # Import the actual lesson functionality or provide fallback
    try:
        from views.lesson import show_lesson
        # Call the lesson view but handle it carefully
        show_lesson()
    except Exception as e:
        st.error(f"Błąd importu lekcji: {e}")
        # Fallback lesson content
        st.info("System lekcji jest tymczasowo niedostępny.")
        
        # Show basic lesson structure
        st.markdown("#### Dostępne lekcje:")
        
        lessons = [
            {"id": "B1C1L1", "title": "Strach przed stratą", "tag": "Psychologia inwestowania"},
            {"id": "B1C1L4", "title": "Emocjonalna zmienność", "tag": "Zarządzanie emocjami"}
        ]
        
        for lesson in lessons:
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{lesson['title']}**")
                    st.markdown(f"*{lesson['tag']}*")
                with col2:
                    if st.button("Rozpocznij", key=f"lesson_{lesson['id']}"):
                        st.session_state.selected_lesson = lesson['id']
                        st.session_state.page = 'lesson'
                        st.rerun()

def show_skills_in_lessons_tab():
    """Display complete skills functionality within the lessons tab"""
    try:
        # Import skills functionality
        from views.skills_new import show_skills_content, add_custom_css
        from data.users import load_user_data, get_current_user_data
        from data.course_data import get_blocks, get_categories
        from utils.layout import get_device_type
        
        # Apply custom CSS for skills
        add_custom_css()
        
        # Get user data
        users_data = load_user_data()
        user_data = get_current_user_data(st.session_state.username)
        user_skills = user_data.get("skills", {})
        user_xp = user_data.get("xp", 0)
        user_completed_lessons = set(user_data.get("completed_lessons", []))
        
        # Get course data
        blocks = get_blocks()
        categories_data = get_categories()
        device_type = get_device_type()
        
        # Build categories structure (simplified version for lessons tab)
        categories = {}
        
        # Show skills content directly (without the tabs structure)
        show_skills_content(user_skills, user_xp, user_completed_lessons, categories, blocks, categories_data, users_data, user_data, device_type)
        
    except Exception as e:
        st.error(f"Błąd ładowania systemu umiejętności: {e}")
        # Fallback skills content
        st.info("System umiejętności jest tymczasowo niedostępny.")
        
        # Basic skills overview
        skills_categories = {
            "Analiza fundamentalna": ["Analiza sprawozdań", "Wycena spółek", "Analiza sektorowa"],
            "Analiza techniczna": ["Wzorce świecowe", "Wskaźniki techniczne", "Teoria Dow"],
            "Zarządzanie ryzykiem": ["Stop loss", "Position sizing", "Dywersyfikacja"],
            "Psychologia": ["Kontrola emocji", "Dyscyplina", "Długoterminowe myślenie"]
        }
        
        for category, skills in skills_categories.items():
            with st.expander(f"📂 {category}"):
                for skill in skills:
                    progress = st.slider(skill, 0, 100, 25, disabled=True)

def show_skill_tree_content():
    """Display skills content (fallback if skills view import fails)"""
    try:
        from views.skills_new import show_skill_tree
        # Call the skills view
        show_skill_tree()
    except Exception as e:
        st.error(f"Błąd importu umiejętności: {e}")
        # Fallback skills content
        st.info("System umiejętności jest tymczasowo niedostępny.")
        
        # Basic skills overview
        skills_categories = {
            "Analiza fundamentalna": ["Analiza sprawozdań", "Wycena spółek", "Analiza sektorowa"],
            "Analiza techniczna": ["Wzorce świecowe", "Wskaźniki techniczne", "Teoria Dow"],
            "Zarządzanie ryzykiem": ["Stop loss", "Position sizing", "Dywersyfikacja"],
            "Psychologia": ["Kontrola emocji", "Dyscyplina", "Długoterminowe myślenie"]
        }
        
        for category, skills in skills_categories.items():
            with st.expander(f"📂 {category}"):
                for skill in skills:
                    progress = st.slider(skill, 0, 100, 25, disabled=True)
