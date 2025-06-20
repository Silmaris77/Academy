"""
Implementation View - Wdrożenie
Standalone page for practical missions (Misje Praktyczne)
"""

import streamlit as st
from utils.components import zen_header
from utils.mission_components import render_missions_page

# Simple fallback mission manager
class FallbackMissionManager:
    def load_lesson_missions(self, lesson_id: str):
        return {
            'missions': [
                {
                    'id': f'{lesson_id}_mission_1',
                    'title': 'Autorefleksja',
                    'description': 'Przemyśl materiał lekcji',
                    'difficulty': 'Łatwy',
                    'estimated_time': '10 min',
                    'xp_reward': 25
                }
            ]
        }
    
    def get_lesson_mission_summary(self, username: str, lesson_id: str):
        return {
            'completed_missions': 1,
            'total_missions': 2,
            'total_xp_earned': 25,
            'completion_percentage': 50.0
        }

mission_manager = FallbackMissionManager()


def show_implementation():
    """Display the implementation page with practical missions"""
    
    # Page header
    zen_header("🎯 Wdrożenie", "Praktyczne misje pomagające zastosować wiedzę w rzeczywistości")
    
    # Check if user is logged in
    if not st.session_state.get('logged_in', False):
        st.warning("⚠️ Musisz być zalogowany, aby uzyskać dostęp do misji praktycznych.")
        return
    
    username = st.session_state.get('username', 'user')
      # Introduction section
    st.markdown("""
    ### 🎯 O sekcji Wdrożenie
    
    Sekcja **Wdrożenie** to miejsce, gdzie teoria spotyka się z praktyką. Tutaj znajdziesz:
    
    - 🧠 **Misje praktyczne** - strukturalne zadania wielodniowe
    - 📈 **Śledzenie postępu** - monitoruj swoje osiągnięcia
    - 🎮 **System XP** - zdobywaj punkty za ukończone zadania
    - 🏆 **Odznaki** - otrzymuj nagrody za konsekwencję
    
    Każda misja została starannie zaprojektowana, aby pomóc Ci zastosować wiedzę zdobytą podczas lekcji w rzeczywistych sytuacjach inwestycyjnych.
    
    ---
    """)
    
    # Display user's mission stats
    display_mission_stats(username)
    
    # Get available lessons with missions
    available_lessons = get_lessons_with_missions()
    
    if not available_lessons:
        st.info("🔄 **Misje w przygotowaniu**\n\nAktualnie przygotowujemy praktyczne misje dla różnych lekcji. Wkrótce będą dostępne!")
        return
    
    # Display missions for each available lesson    for lesson_info in available_lessons:
        lesson_id = lesson_info['id']
        lesson_title = lesson_info['title']
        
        # Create expandable section for each lesson
        with st.expander(f"📚 {lesson_title}", expanded=(lesson_id == 'B1C1L1')):
            st.markdown(f"### 🎯 Misje praktyczne: {lesson_title}")
            st.markdown("Praktyczne zadania pomagające zastosować wiedzę z tej lekcji w rzeczywistych sytuacjach:")
            
            try:
                render_missions_page(username, lesson_id)
            except Exception as e:
                st.warning(f"⚠️ Misje dla lekcji {lesson_title} nie są obecnie dostępne.")
                with st.expander("Szczegóły błędu (dla deweloperów)"):
                    st.error(str(e))
    
    # Additional information section
    if available_lessons:
        st.markdown("---")
        st.markdown("""
        ### 💡 Wskazówki do misji
        
        **Jak skutecznie realizować misje praktyczne:**
        
        1. **Regularity is key** 🗓️ - Wykonuj zadania codziennie w tym samym czasie
        2. **Bądź szczery** 📝 - Zapisuj prawdziwe obserwacje i odczucia
        3. **Nie rezygnuj** 💪 - Każdy dzień przynosi nowe doświadczenia
        4. **Aplikuj wiedzę** 🧠 - Łącz teorie z lekcji z praktycznymi działaniami
        5. **Śledzenie postępu** 📊 - Regularnie sprawdzaj swoje osiągnięcia
        
        **Pamiętaj**: Misje są zaprojektowane tak, aby pomóc Ci stopniowo budować nowe nawyki i umiejętności. 
        Każde zadanie ma konkretny cel edukacyjny i jest częścią większego planu rozwoju.
        """)
    else:
        st.markdown("---")
        st.info("""
        ### 🔄 Rozbudowa systemu misji
        
        Aktualnie przygotowujemy więcej praktycznych misji dla różnych lekcji kursu. 
        Nowe misje będą dodawane regularnie, aby pomóc Ci zastosować wiedzę z każdego modułu w praktyce.
        
        **Co planujemy:**
        - Misje dla wszystkich lekcji bloku B1
        - Zaawansowane wyzwania długoterminowe  
        - Misje grupowe i współzawodnictwo
        - Personalizowane rekomendacje zadań
        
        Śledź aktualizacje w sekcji Dashboard! 📈
        """)


def get_lessons_with_missions():
    """Get list of lessons that have missions available"""
    # For now, we only have missions for B1C1L1
    # This can be expanded as more lessons get missions
    lessons_with_missions = [
        {
            'id': 'B1C1L1',
            'title': 'Strach przed stratą'
        }
    ]
    
    # Filter to only include lessons that actually have mission data
    available_lessons = []
    for lesson in lessons_with_missions:
        lesson_id = lesson['id']
        missions = mission_manager.load_lesson_missions(lesson_id)
        if missions:
            available_lessons.append(lesson)
    
    return available_lessons


def display_mission_stats(username: str):
    """Display user's overall mission statistics"""
    # Calculate overall stats
    total_missions = 0
    completed_missions = 0
    active_missions = 0
    total_xp_earned = 0
    
    # Get stats for all lessons with missions
    available_lessons = get_lessons_with_missions()
    
    for lesson_info in available_lessons:
        lesson_id = lesson_info['id']
        summary = mission_manager.get_lesson_mission_summary(username, lesson_id)
        
        total_missions += summary.get('total_missions', 0)
        completed_missions += summary.get('completed_missions', 0)
        active_missions += summary.get('active_missions', 0)
        total_xp_earned += summary.get('total_xp_earned', 0)
    
    # Display stats in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🎯 Łącznie misji",
            value=total_missions,
            help="Całkowita liczba dostępnych misji"
        )
    
    with col2:
        st.metric(
            label="✅ Ukończone",
            value=completed_missions,
            delta=f"{(completed_missions/total_missions*100):.0f}%" if total_missions > 0 else "0%",
            help="Liczba ukończonych misji"
        )
    
    with col3:
        st.metric(
            label="🔄 Aktywne",
            value=active_missions,
            help="Liczba misji w trakcie realizacji"
        )
    
    with col4:
        st.metric(
            label="💎 XP z misji",
            value=total_xp_earned,
            help="Punkty doświadczenia zdobyte za misje"
        )
    
    st.markdown("---")
