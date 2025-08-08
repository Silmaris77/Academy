import streamlit as st
from data.users_fixed import add_recent_activity, load_user_data
from views.dashboard import show_recent_activities
from datetime import datetime, timezone

st.set_page_config(page_title="Test Ostatnich Aktywności", layout="wide")

st.title("🧪 Test Systemu Ostatnich Aktywności")

if 'username' not in st.session_state:
    st.session_state.username = st.text_input("Podaj swoją nazwę użytkownika:")

if st.session_state.username:
    st.subheader(f"Test dla użytkownika: {st.session_state.username}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dodaj testowe aktywności")
        
        if st.button("➕ Dodaj aktywność: Ukończono lekcję"):
            add_recent_activity(
                st.session_state.username,
                "lesson_completed",
                {"lesson_id": "B1C1L1"}
            )
            st.success("Dodano aktywność ukończenia lekcji!")
            st.rerun()
        
        if st.button("🧬 Dodaj aktywność: Odkryto typ degena"):
            add_recent_activity(
                st.session_state.username,
                "degen_type_discovered",
                {"degen_type": "Hodler"}
            )
            st.success("Dodano aktywność odkrycia typu degena!")
            st.rerun()
        
        if st.button("🏆 Dodaj aktywność: Zdobyto odznakę"):
            add_recent_activity(
                st.session_state.username,
                "badge_earned",
                {"badge_names": ["Pierwszy Krok"]}
            )
            st.success("Dodano aktywność zdobycia odznaki!")
            st.rerun()
        
        if st.button("🔥 Dodaj aktywność: Rozpoczęto passę"):
            add_recent_activity(
                st.session_state.username,
                "daily_streak_started",
                {}
            )
            st.success("Dodano aktywność rozpoczęcia passy!")
            st.rerun()
    
    with col2:
        st.subheader("Aktualne aktywności")
        
        # Pobierz dane użytkownika
        users_data = load_user_data()
        user_data = users_data.get(st.session_state.username, {})
        
        if user_data:
            # Wyświetl ostatnie aktywności używając funkcji z dashboard
            show_recent_activities(user_data)
        else:
            st.warning(f"Nie znaleziono użytkownika: {st.session_state.username}")
    
    st.markdown("---")
    
    # Debugowanie - pokaż surowe dane
    with st.expander("🔍 Debugowanie - surowe dane aktywności"):
        users_data = load_user_data()
        user_data = users_data.get(st.session_state.username, {})
        recent_activities = user_data.get('recent_activities', [])
        
        if recent_activities:
            st.json(recent_activities[:5])  # Pokaż pierwsze 5 aktywności
        else:
            st.info("Brak aktywności dla tego użytkownika")
    
    # Przycisk do czyszczenia aktywności
    if st.button("🗑️ Wyczyść wszystkie aktywności"):
        users_data = load_user_data()
        if st.session_state.username in users_data:
            users_data[st.session_state.username]['recent_activities'] = []
            from data.users import save_user_data
            save_user_data(users_data)
            st.success("Wyczyszczono wszystkie aktywności!")
            st.rerun()

else:
    st.info("Wprowadź nazwę użytkownika, aby rozpocząć test.")
