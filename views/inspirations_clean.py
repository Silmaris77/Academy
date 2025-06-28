import streamlit as st
import random
from utils.components import zen_header, zen_button
from utils.material3_components import apply_material3_theme
from utils.layout import get_device_type, toggle_device_view
from utils.inspirations_loader import (
    load_inspirations_data, get_categories, get_featured_inspirations,
    get_inspirations_by_category, search_inspirations, get_inspiration_by_id,
    load_inspiration_content, increment_inspiration_views, get_inspiration_views,
    mark_inspiration_as_favorite, unmark_inspiration_as_favorite, 
    is_inspiration_favorite, get_favorite_inspirations, get_difficulty_emoji,
    get_difficulty_text, get_random_inspiration, get_all_inspirations
)

def show_inspirations_page():
    # Zastosuj style Material 3
    apply_material3_theme()
    
    # Opcja wyboru urządzenia w trybie deweloperskim
    if st.session_state.get('dev_mode', False):
        toggle_device_view()
    
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    # Używamy naszego komponentu nagłówka
    zen_header("Inspiracje")
    
    # Initialize session state for inspirations
    if 'inspiration_view_mode' not in st.session_state:
        st.session_state.inspiration_view_mode = 'overview'
    if 'current_inspiration' not in st.session_state:
        st.session_state.current_inspiration = None
    if 'favorite_inspirations' not in st.session_state:
        st.session_state.favorite_inspirations = []
    
    # Add basic styles
    add_inspirations_styles()
    
    # Main navigation
    show_navigation()
    
    # Content based on current view mode
    if st.session_state.inspiration_view_mode == 'overview':
        show_overview()
    elif st.session_state.inspiration_view_mode == 'categories':
        show_categories_view()
    elif st.session_state.inspiration_view_mode == 'search':
        show_search_view()
    elif st.session_state.inspiration_view_mode == 'favorites':
        show_favorites_view()
    elif st.session_state.inspiration_view_mode == 'detail':
        show_inspiration_detail()

def add_inspirations_styles():
    """Dodaje podstawowe style dla Inspiracji"""
    st.markdown("""
    <style>
    /* Podstawowe style */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Nawigacja */
    .inspirations-nav-bar {
        background: rgba(255,255,255,0.95);
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .inspirations-nav-bar [data-testid="stButton"] button {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%) !important;
        border: 1px solid #cbd5e1 !important;
        color: #475569 !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s ease !important;
        margin: 0 0.25rem !important;
    }
    
    .inspirations-nav-bar [data-testid="stButton"] button:hover {
        background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%) !important;
        border-color: #94a3b8 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
    
    /* Podstawowe hover dla przycisków */
    .stButton button {
        transition: all 0.3s ease !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
    }
    
    /* Mobile */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def show_navigation():
    """Wyświetla nawigację między sekcjami inspiracji"""
    st.markdown('<div class="inspirations-nav-bar">', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠 Przegląd", key="nav_overview"):
            st.session_state.inspiration_view_mode = 'overview'
            st.rerun()
    
    with col2:
        if st.button("📂 Kategorie", key="nav_categories"):
            st.session_state.inspiration_view_mode = 'categories'
            st.rerun()
    
    with col3:
        if st.button("🔍 Szukaj", key="nav_search"):
            st.session_state.inspiration_view_mode = 'search'
            st.rerun()
    
    with col4:
        if st.button("⭐ Ulubione", key="nav_favorites"):
            st.session_state.inspiration_view_mode = 'favorites'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_overview():
    """Strona główna inspiracji"""
    
    # Featured inspirations
    st.subheader("🌟 Polecane Inspiracje")
    featured = get_featured_inspirations()
    
    if featured:
        display_inspirations_grid(featured, featured=True)
    else:
        st.info("Brak polecanych inspiracji")
    
    # Quick access to categories
    st.subheader("🗂️ Kategorie")
    categories = get_categories()
    
    if categories:
        cols = st.columns(min(3, len(categories)))
        for i, category in enumerate(categories[:3]):
            with cols[i]:
                if st.button(f"📚 {category}", key=f"quick_cat_{i}"):
                    st.session_state.inspiration_view_mode = 'categories'
                    st.session_state.selected_category = category
                    st.rerun()

def show_categories_view():
    """Widok kategorii inspiracji"""
    st.subheader("📂 Przeglądaj po kategoriach")
    
    categories = get_categories()
    
    # Category selector
    category_options = ["Wszystkie"] + list(categories)
    selected_category = st.selectbox("Wybierz kategorię:", category_options, key="category_selector")
    
    if selected_category == "Wszystkie":
        inspirations = get_all_inspirations()
    else:
        inspirations = get_inspirations_by_category(selected_category)
    
    if inspirations:
        display_inspirations_grid(inspirations)
    else:
        st.info(f"Brak inspiracji w kategorii: {selected_category}")

def show_search_view():
    """Widok wyszukiwania inspiracji"""
    st.subheader("🔍 Szukaj inspiracji")
    
    # Search input
    search_query = st.text_input("Wpisz frazę do wyszukania:", key="search_input")
    
    if search_query:
        results = search_inspirations(search_query)
        
        if results:
            st.write(f"Znaleziono {len(results)} wyników dla: **{search_query}**")
            display_inspirations_grid(results)
        else:
            st.info(f"Brak wyników dla: {search_query}")
    else:
        st.info("Wprowadź frazę do wyszukania")

def show_favorites_view():
    """Widok ulubionych inspiracji"""
    st.subheader("⭐ Twoje ulubione inspiracje")
    
    favorites = get_favorite_inspirations()
    
    if favorites:
        display_inspirations_grid(favorites)
    else:
        st.info("Nie masz jeszcze ulubionych inspiracji. Dodaj je klikając ⭐ na kartach inspiracji.")

def display_inspirations_grid(inspirations, featured=False):
    """Wyświetla siatkę inspiracji w kolumnach"""
    
    # Podziel inspiracje na grupy po 2 dla dwóch kolumn
    for i in range(0, len(inspirations), 2):
        col1, col2 = st.columns(2, gap="large")
        
        # Pierwsza karta
        with col1:
            if i < len(inspirations):
                show_single_inspiration_card(inspirations[i], featured, i % 4)
        
        # Druga karta (jeśli istnieje)
        with col2:
            if i + 1 < len(inspirations):
                show_single_inspiration_card(inspirations[i + 1], featured, (i + 1) % 4)
            else:
                # Pusta kolumna dla symetrii
                st.empty()

def show_single_inspiration_card(inspiration, featured=False, card_index=0):
    """Wyświetla pojedynczą kartę inspiracji używając kolorowych kontenerów Streamlit"""
    
    # Przygotuj dane
    difficulty_emoji = get_difficulty_emoji(inspiration.get('difficulty', 'beginner'))
    difficulty_text = get_difficulty_text(inspiration.get('difficulty', 'beginner'))
    reading_time = inspiration.get('reading_time', 5)
    views = get_inspiration_views(inspiration['id'])
    is_fav = is_inspiration_favorite(inspiration['id'])
    fav_icon = "⭐" if is_fav else "☆"
    
    # Użyj kolorowego kontenera na podstawie typu
    if featured:
        container_type = "info"  # Niebieski kontener
        container_icon = "🌟"
    else:
        container_type = "success"  # Zielony kontener  
        container_icon = "💡"
    
    # Kontener z kolorem
    with st.container(border=True):
        # Używamy kolorowego alertu jako tła
        if featured:
            st.info(f"### {container_icon} {inspiration['title']}\n\n{inspiration['description']}", icon=container_icon)
        else:
            st.success(f"### {container_icon} {inspiration['title']}\n\n{inspiration['description']}", icon=container_icon)
        
        # Meta informacje
        col1, col2, col3 = st.columns(3)
        with col1:
            st.caption(f"{difficulty_emoji} {difficulty_text}")
        with col2:
            st.caption(f"📖 {reading_time} min")
        with col3:
            st.caption(f"👁️ {views} wyświetleń")
        
        # Tagi
        if inspiration.get('tags'):
            st.caption("🏷️ " + " • ".join(inspiration['tags'][:3]))
        
        # Przyciski
        col_fav, col_read = st.columns(2)
        
        with col_fav:
            if st.button(fav_icon, key=f"fav_{inspiration['id']}_{card_index}", help="Dodaj/usuń z ulubionych"):
                if is_fav:
                    unmark_inspiration_as_favorite(inspiration['id'])
                else:
                    mark_inspiration_as_favorite(inspiration['id'])
                st.rerun()
        
        with col_read:
            if st.button("📖 CZYTAJ", key=f"read_{inspiration['id']}_{card_index}", type="primary"):
                st.session_state.current_inspiration = inspiration['id']
                st.session_state.inspiration_view_mode = 'detail'
                increment_inspiration_views(inspiration['id'])
                st.rerun()

def show_inspiration_detail():
    """Wyświetla szczegóły inspiracji"""
    inspiration_id = st.session_state.current_inspiration
    inspiration = get_inspiration_by_id(inspiration_id)
    
    if not inspiration:
        st.error("Nie znaleziono inspiracji")
        if st.button("← Powrót do przeglądu"):
            st.session_state.inspiration_view_mode = 'overview'
            st.rerun()
        return
    
    # Back button
    if st.button("← Powrót", key="back_to_overview"):
        st.session_state.inspiration_view_mode = 'overview'
        st.rerun()
    
    # Title and meta
    st.title(inspiration['title'])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        difficulty_emoji = get_difficulty_emoji(inspiration.get('difficulty', 'beginner'))
        difficulty_text = get_difficulty_text(inspiration.get('difficulty', 'beginner'))
        st.write(f"{difficulty_emoji} **Poziom:** {difficulty_text}")
    with col2:
        reading_time = inspiration.get('reading_time', 5)
        st.write(f"📖 **Czas czytania:** {reading_time} min")
    with col3:
        views = get_inspiration_views(inspiration['id'])
        st.write(f"👁️ **Wyświetlenia:** {views}")
    
    # Tags
    if inspiration.get('tags'):
        st.write("**Tagi:** " + " • ".join([f"*{tag}*" for tag in inspiration['tags']]))
    
    # Content
    st.markdown("---")
    content = load_inspiration_content(inspiration['id'])
    if content:
        st.markdown(content)
    else:
        st.info("Zawartość inspiracji będzie dostępna wkrótce...")
    
    # Favorite button
    is_fav = is_inspiration_favorite(inspiration['id'])
    fav_text = "Usuń z ulubionych ⭐" if is_fav else "Dodaj do ulubionych ☆"
    
    if st.button(fav_text, key="detail_favorite", type="secondary"):
        if is_fav:
            unmark_inspiration_as_favorite(inspiration['id'])
        else:
            mark_inspiration_as_favorite(inspiration['id'])
        st.rerun()
    
    # Random inspiration suggestion
    st.markdown("---")
    if st.button("🎲 Losowa inspiracja", key="random_inspiration"):
        random_insp = get_random_inspiration()
        if random_insp:
            st.session_state.current_inspiration = random_insp['id']
            increment_inspiration_views(random_insp['id'])
            st.rerun()
