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
    # Zastosuj style Material 3 (tak jak w dashboard)
    apply_material3_theme()
    
    # Opcja wyboru urządzenia w trybie deweloperskim
    if st.session_state.get('dev_mode', False):
        toggle_device_view()
    
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    # Używamy naszego komponentu nagłówka - tak jak w dashboard
    zen_header("Inspiracje")
    
    # Initialize session state for inspirations
    if 'inspiration_view_mode' not in st.session_state:
        st.session_state.inspiration_view_mode = 'overview'
    if 'current_inspiration' not in st.session_state:
        st.session_state.current_inspiration = None
    if 'favorite_inspirations' not in st.session_state:
        st.session_state.favorite_inspirations = []
    
    # Add Material Design 3 styles for inspirations
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
    """Dodaje style Material Design 3 dla Inspiracji"""
    st.markdown("""
    <style>
    /* ===== INSPIRACJE - HEADER ===== */
    .inspirations-header {
        isolation: isolate;
        padding: 1rem !important;
    }
    
    /* ===== INSPIRACJE - NAWIGACJA ===== */
    .inspirations-nav-bar {
        background: rgba(255,255,255,0.95);
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        isolation: isolate;
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
        color: #334155 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
    
    /* ===== MD3 COMPONENTS ===== */
    .md3-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        isolation: isolate;
    }
    
    .md3-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transform: translateY(-2px);
        border-color: #cbd5e1;
    }
    
    .md3-elevated-card {
        box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06);
    }
    
    .md3-card-featured {
        border: 2px solid #3b82f6;
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    }
    
    .inspiration-meta {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin: 0.5rem 0;
        font-size: 0.875rem;
        color: #64748b;
    }
    
    .inspiration-tags {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        margin: 0.75rem 0;
    }
    
    .tag {
        background: #f1f5f9;
        color: #475569;
        padding: 0.25rem 0.75rem;
        border-radius: 16px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .category-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .quick-stats {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        text-align: center;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        display: block;
    }
    
    .stat-label {
        font-size: 0.875rem;
        opacity: 0.9;
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
    """Strona główna inspiracji z polecane i statystyki"""
    
    # Quick stats
    all_inspirations = get_all_inspirations()
    categories = get_categories()
    favorites = get_favorite_inspirations()
    
    st.markdown(f"""
    <div class="quick-stats">
        <h3 style="margin: 0; margin-bottom: 1rem;">Statystyki Inspiracji</h3>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-number">{len(all_inspirations)}</span>
                <span class="stat-label">Inspiracji</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{len(categories)}</span>
                <span class="stat-label">Kategorii</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{len(favorites)}</span>
                <span class="stat-label">Ulubionych</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured inspirations
    st.subheader("🌟 Polecane Inspiracje")
    featured = get_featured_inspirations()
    
    if featured:
        for inspiration in featured:
            show_inspiration_card(inspiration, featured=True)
    else:
        st.info("Brak polecanych inspiracji")
    
    # Quick access to categories
    st.subheader("🗂️ Szybki dostęp do kategorii")
    categories = get_categories()
    
    cols = st.columns(4)
    for i, (cat_id, cat_name) in enumerate(categories.items()):
        col_index = i % 4
        with cols[col_index]:
            if st.button(cat_name, key=f"quick_cat_{cat_id}", use_container_width=True):
                st.session_state.inspiration_view_mode = 'categories'
                st.session_state.selected_category = cat_id
                st.rerun()

def show_categories_view():
    """Widok kategorii inspiracji"""
    st.subheader("📂 Przeglądaj po kategoriach")
    
    categories = get_categories()
    
    # Category selector
    category_options = ["Wszystkie"] + list(categories.values())
    selected_cat_name = st.selectbox("Wybierz kategorię:", category_options)
    
    if selected_cat_name == "Wszystkie":
        inspirations = get_all_inspirations()
        st.write(f"Wyświetlane: wszystkie inspiracje ({len(inspirations)})")
    else:
        # Find category ID by name
        selected_cat_id = None
        for cat_id, cat_name in categories.items():
            if cat_name == selected_cat_name:
                selected_cat_id = cat_id
                break
        
        if selected_cat_id:
            inspirations = get_inspirations_by_category(selected_cat_id)
            st.write(f"Wyświetlane: {selected_cat_name} ({len(inspirations)})")
        else:
            inspirations = []
    
    # Display inspirations
    if inspirations:
        for inspiration in inspirations:
            show_inspiration_card(inspiration)
    else:
        st.info("Brak inspiracji w tej kategorii")

def show_search_view():
    """Widok wyszukiwania"""
    st.subheader("🔍 Wyszukaj inspiracje")
    
    search_query = st.text_input("Wpisz słowo kluczowe:", placeholder="np. motywacja, crypto, sukces...")
    
    if search_query:
        results = search_inspirations(search_query)
        
        if results:
            st.write(f"Znaleziono {len(results)} wyników dla: **{search_query}**")
            for inspiration in results:
                show_inspiration_card(inspiration)
        else:
            st.warning(f"Nie znaleziono inspiracji dla: **{search_query}**")
            st.info("Spróbuj innych słów kluczowych lub przeglądaj kategorie")
    else:
        st.info("Wprowadź słowo kluczowe aby wyszukać inspiracje")

def show_favorites_view():
    """Widok ulubionych inspiracji"""
    st.subheader("⭐ Twoje ulubione inspiracje")
    
    favorites = get_favorite_inspirations()
    
    if favorites:
        st.write(f"Masz {len(favorites)} ulubionych inspiracji")
        for inspiration in favorites:
            show_inspiration_card(inspiration)
    else:
        st.info("Nie masz jeszcze ulubionych inspiracji")
        st.write("💡 Dodaj inspiracje do ulubionych klikając ⭐ przy każdej inspiracji")

def show_inspiration_card(inspiration, featured=False):
    """Wyświetla kartę inspiracji"""
    card_class = "md3-card-featured" if featured else "md3-card"
    
    st.markdown(f'<div class="{card_class}">', unsafe_allow_html=True)
    
    # Title and favorite button
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"### {inspiration['title']}")
    with col2:
        is_fav = is_inspiration_favorite(inspiration['id'])
        fav_button_text = "⭐" if is_fav else "☆"
        if st.button(fav_button_text, key=f"fav_{inspiration['id']}"):
            if is_fav:
                unmark_inspiration_as_favorite(inspiration['id'])
            else:
                mark_inspiration_as_favorite(inspiration['id'])
            st.rerun()
    
    # Description
    st.write(inspiration['description'])
    
    # Meta information
    difficulty_emoji = get_difficulty_emoji(inspiration.get('difficulty', 'beginner'))
    difficulty_text = get_difficulty_text(inspiration.get('difficulty', 'beginner'))
    reading_time = inspiration.get('reading_time', 5)
    views = get_inspiration_views(inspiration['id'])
    
    st.markdown(f"""
    <div class="inspiration-meta">
        <span>{difficulty_emoji} {difficulty_text}</span>
        <span>📖 {reading_time} min</span>
        <span>👁️ {views} wyświetleń</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Tags
    if inspiration.get('tags'):
        tags_html = ' '.join([f'<span class="tag">{tag}</span>' for tag in inspiration['tags']])
        st.markdown(f'<div class="inspiration-tags">{tags_html}</div>', unsafe_allow_html=True)
    
    # Read button
    if st.button("📖 Czytaj", key=f"read_{inspiration['id']}", use_container_width=True):
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
        tags_html = ' '.join([f'<span class="tag">{tag}</span>' for tag in inspiration['tags']])
        st.markdown(f'<div class="inspiration-tags">{tags_html}</div>', unsafe_allow_html=True)
    
    # Favorite button
    is_fav = is_inspiration_favorite(inspiration['id'])
    if is_fav:
        if st.button("⭐ Usuń z ulubionych", key="remove_favorite"):
            unmark_inspiration_as_favorite(inspiration['id'])
            st.rerun()
    else:
        if st.button("☆ Dodaj do ulubionych", key="add_favorite"):
            mark_inspiration_as_favorite(inspiration['id'])
            st.rerun()
    
    st.divider()
    
    # Content
    content_path = inspiration.get('content_path', '')
    if content_path:
        content = load_inspiration_content(content_path)
        st.markdown(content)
    else:
        st.warning("Brak treści dla tej inspiracji")
    
    st.divider()
    
    # Rating section
    st.subheader("Oceń tę inspirację")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    emotions = ["😞", "😐", "🙂", "😊", "🤩"]
    emotion_labels = ["Słaba", "Przeciętna", "Dobra", "Bardzo dobra", "Fantastyczna"]
    
    for i, (emotion, label) in enumerate(zip(emotions, emotion_labels)):
        with [col1, col2, col3, col4, col5][i]:
            if st.button(f"{emotion}\n{label}", key=f"rate_{inspiration['id']}_{i}"):
                # Save rating to session state
                if 'inspiration_ratings' not in st.session_state:
                    st.session_state.inspiration_ratings = {}
                st.session_state.inspiration_ratings[inspiration['id']] = i + 1
                st.success(f"Dziękujemy za ocenę: {emotion}")
                st.rerun()
