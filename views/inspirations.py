import streamlit as st
import random
from utils.components import zen_header, zen_button
from utils.material3_components import apply_material3_theme
from utils.layout import get_device_type, toggle_device_view
from utils.inspirations_loader import (
    load_inspirations_data, get_categories,
    get_inspirations_by_category, search_inspirations, get_inspiration_by_id,
    load_inspiration_content, increment_inspiration_views, get_inspiration_views,
    mark_inspiration_as_favorite, unmark_inspiration_as_favorite, 
    toggle_inspiration_favorite,  # Add toggle function
    is_inspiration_favorite, get_favorite_inspirations,
    get_random_inspiration, get_all_inspirations,
    mark_inspiration_as_read, is_inspiration_read, get_read_inspirations
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
    elif st.session_state.inspiration_view_mode == 'read':
        show_read_view()
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
      /* Style dla kart inspiracji - wyrównanie przycisków */
    .inspiration-card-buttons {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        gap: 0.75rem !important;
        margin-top: 1rem !important;
    }
    
    .inspiration-card-buttons .stButton:first-child button {
        margin-right: auto !important;
        justify-content: flex-start !important;
    }
    
    .inspiration-card-buttons .stButton:last-child button {
        margin-left: auto !important;
        justify-content: flex-end !important;
    }
    
    /* Lepsze wyrównanie przycisków w kartach */
    [data-testid="column"]:nth-child(1) [data-testid="stButton"] button {
        width: 100% !important;
        text-align: left !important;
        justify-content: flex-start !important;
    }
    
    [data-testid="column"]:nth-child(2) [data-testid="stButton"] button {
        width: 100% !important;
        text-align: right !important;
        justify-content: flex-end !important;
    }
    
    /* Mobile */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        /* Na mobile przyciski zajmują całą szerokość */
        [data-testid="column"] [data-testid="stButton"] button {
            width: 100% !important;
            text-align: center !important;
            justify-content: center !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def show_navigation():
    """Wyświetla nawigację między sekcjami inspiracji"""
    st.markdown('<div class="inspirations-nav-bar">', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
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
    
    with col5:
        if st.button("✅ Przeczytane", key="nav_read"):
            st.session_state.inspiration_view_mode = 'read'
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_overview():
    """Strona główna inspiracji - wszystkie artykuły"""
    
    # Wszystkie inspiracje
    st.subheader("📚 Wszystkie Inspiracje")
    all_inspirations = get_all_inspirations()
    
    if all_inspirations:
        st.info(f"📖 Dostępnych jest **{len(all_inspirations)}** inspiracji do przeczytania!")
        display_inspirations_grid(all_inspirations, featured=False)
    else:
        st.info("Brak dostępnych inspiracji")
    
    # Quick access to categories
    st.subheader("🗂️ Przeglądaj po kategoriach")
    categories = get_categories()
    
    if categories:
        # Upewnij się, że categories to lista
        if isinstance(categories, dict):
            category_list = list(categories.keys())
        elif isinstance(categories, (list, tuple)):
            category_list = list(categories)
        else:
            category_list = list(categories) if categories else []
        
        # Pokaż maksymalnie 3 kategorie
        display_categories = category_list[:3]
        
        if display_categories:
            cols = st.columns(len(display_categories))
            for i, category in enumerate(display_categories):
                with cols[i]:
                    if st.button(f"📚 {category}", key=f"quick_cat_{i}"):
                        st.session_state.inspiration_view_mode = 'categories'
                        st.session_state.selected_category = category
                        st.rerun()

def show_categories_view():
    """Widok kategorii inspiracji"""
    st.subheader("📂 Przeglądaj po kategoriach")
    
    categories = get_categories()
    
    # Upewnij się, że categories to lista
    if isinstance(categories, dict):
        category_list = list(categories.keys())
    elif isinstance(categories, (list, tuple)):
        category_list = list(categories)
    else:
        category_list = list(categories) if categories else []
    
    # Category selector
    category_options = ["Wszystkie"] + category_list
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

def show_read_view():
    """Widok przeczytanych inspiracji"""
    st.subheader("✅ Przeczytane inspiracje")
    
    read_inspirations = get_read_inspirations()
    
    if read_inspirations:
        st.info(f"📖 Przeczytałeś już **{len(read_inspirations)}** inspiracji!")
        display_inspirations_grid(read_inspirations)
    else:
        st.info("Nie przeczytałeś jeszcze żadnej inspiracji. Rozpocznij czytanie w sekcji Przegląd!")

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
    reading_time = inspiration.get('reading_time', 5)
    views = get_inspiration_views(inspiration['id'])
    is_fav = is_inspiration_favorite(inspiration['id'])
    is_read = is_inspiration_read(inspiration['id'])
    fav_icon = "⭐" if is_fav else "☆"
    
    # Wszystkie karty używają tego samego stylu (zielony kontener z ikoną 💡)
    container_icon = "💡"
    
    # Kontener z kolorem - przyciski WEWNĄTRZ kontenera
    with st.container(border=True):
        st.success(f"### {inspiration['title']}\n\n{inspiration['description']}", icon=container_icon)
        
        # Meta informacje (bez poziomu trudności)
        col1, col2 = st.columns(2)
        with col1:
            st.caption(f"📖 {reading_time} min")
        with col2:
            st.caption(f"👁️ {views} wyświetleń")
        
        # Tagi
        tags = inspiration.get('tags', [])
        if tags and isinstance(tags, (list, tuple)):
            # Pokaż maksymalnie 3 tagi
            display_tags = tags[:3] if len(tags) > 3 else tags
            st.caption("🏷️ " + " • ".join(display_tags))        # Przyciski WEWNĄTRZ kontenera - wyrównane do krawędzi
        # Sprawdź czy artykuł został przeczytany i dostosuj tekst przycisku
        if is_read:
            button_text = "✅ PRZECZYTANE"
            button_type = "secondary"
            help_text = "Artykuł przeczytany - kliknij by czytać ponownie"
        else:
            button_text = "📖 CZYTAJ"
            button_type = "primary"
            help_text = "Przeczytaj inspirację"
        
        # Div z klasą CSS dla lepszego wyrównania
        st.markdown('<div class="inspiration-card-buttons">', unsafe_allow_html=True)
          # Kolumny z gap dla przycisków
        col_fav, col_read = st.columns([1, 1], gap="medium")
        
        with col_fav:
            if st.button(f"{fav_icon} Ulubione", key=f"fav_{inspiration['id']}_{card_index}", help="Dodaj/usuń z ulubionych", use_container_width=True):
                toggle_inspiration_favorite(inspiration['id'])
                st.rerun()
        
        with col_read:
            if st.button(button_text, key=f"read_{inspiration['id']}_{card_index}", type=button_type, help=help_text, use_container_width=True):
                st.session_state.current_inspiration = inspiration['id']
                st.session_state.inspiration_view_mode = 'detail'
                increment_inspiration_views(inspiration['id'])
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

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
    
    col1, col2 = st.columns(2)
    with col1:
        reading_time = inspiration.get('reading_time', 5)
        st.write(f"📖 **Czas czytania:** {reading_time} min")
    with col2:
        views = get_inspiration_views(inspiration['id'])
        st.write(f"👁️ **Wyświetlenia:** {views}")
      # Tags
    tags = inspiration.get('tags', [])
    if tags and isinstance(tags, (list, tuple)):
        formatted_tags = [f"*{tag}*" for tag in tags]
        st.write("**Tagi:** " + " • ".join(formatted_tags))
      # Content
    st.markdown("---")
    content = load_inspiration_content(inspiration['id'])
    if content:
        st.markdown(content)
        # Oznacz inspirację jako przeczytaną gdy treść zostanie wyświetlona
        mark_inspiration_as_read(inspiration['id'])
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
