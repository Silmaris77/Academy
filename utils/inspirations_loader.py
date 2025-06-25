import streamlit as st
import json
import os
from pathlib import Path

def load_inspirations_data():
    """Ładuje dane inspiracji z pliku JSON"""
    try:
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "inspirations", "inspirations_data.json")
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Błąd ładowania danych inspiracji: {e}")
        return {"categories": {}, "inspirations": [], "featured": []}

def load_inspiration_content(content_path):
    """Ładuje treść inspiracji z pliku markdown"""
    try:
        base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "inspirations")
        full_path = os.path.join(base_path, content_path)
        
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return "## Treść w przygotowaniu\n\nTa inspiracja jest obecnie przygotowywana. Wróć wkrótce!"
    except Exception as e:
        return f"## Błąd ładowania treści\n\nNie można załadować treści: {e}"

def get_categories():
    """Pobiera listę kategorii"""
    data = load_inspirations_data()
    return data.get("categories", {})

def get_inspirations_by_category(category_id):
    """Pobiera inspiracje z konkretnej kategorii"""
    data = load_inspirations_data()
    inspirations = data.get("inspirations", [])
    return [insp for insp in inspirations if insp.get("category") == category_id]

def get_featured_inspirations():
    """Pobiera polecane inspiracje"""
    data = load_inspirations_data()
    featured_ids = data.get("featured", [])
    all_inspirations = data.get("inspirations", [])
    
    featured = []
    for insp in all_inspirations:
        if insp.get("id") in featured_ids:
            featured.append(insp)
    
    return featured

def get_inspiration_by_id(inspiration_id):
    """Pobiera konkretną inspirację po ID"""
    data = load_inspirations_data()
    inspirations = data.get("inspirations", [])
    
    for insp in inspirations:
        if insp.get("id") == inspiration_id:
            return insp
    return None

def search_inspirations(query):
    """Wyszukuje inspiracje po tytule i tagach"""
    data = load_inspirations_data()
    inspirations = data.get("inspirations", [])
    results = []
    
    query = query.lower()
    
    for insp in inspirations:
        # Szukaj w tytule
        if query in insp.get("title", "").lower():
            results.append(insp)
            continue
        
        # Szukaj w opisie
        if query in insp.get("description", "").lower():
            results.append(insp)
            continue
            
        # Szukaj w tagach
        tags = insp.get("tags", [])
        if any(query in tag.lower() for tag in tags):
            results.append(insp)
            continue
    
    return results

def get_all_inspirations():
    """Pobiera wszystkie inspiracje"""
    data = load_inspirations_data()
    return data.get("inspirations", [])

# Functions for user interactions (using session state)

def increment_inspiration_views(inspiration_id):
    """Zwiększa licznik wyświetleń inspiracji"""
    if 'inspiration_views' not in st.session_state:
        st.session_state.inspiration_views = {}
    
    current_views = st.session_state.inspiration_views.get(inspiration_id, 0)
    st.session_state.inspiration_views[inspiration_id] = current_views + 1

def get_inspiration_views(inspiration_id):
    """Pobiera liczbę wyświetleń inspiracji"""
    if 'inspiration_views' not in st.session_state:
        return 0
    return st.session_state.inspiration_views.get(inspiration_id, 0)

def mark_inspiration_as_favorite(inspiration_id):
    """Dodaje inspirację do ulubionych"""
    if 'favorite_inspirations' not in st.session_state:
        st.session_state.favorite_inspirations = []
    
    if inspiration_id not in st.session_state.favorite_inspirations:
        st.session_state.favorite_inspirations.append(inspiration_id)

def unmark_inspiration_as_favorite(inspiration_id):
    """Usuwa inspirację z ulubionych"""
    if 'favorite_inspirations' not in st.session_state:
        st.session_state.favorite_inspirations = []
    
    if inspiration_id in st.session_state.favorite_inspirations:
        st.session_state.favorite_inspirations.remove(inspiration_id)

def is_inspiration_favorite(inspiration_id):
    """Sprawdza czy inspiracja jest ulubiona"""
    if 'favorite_inspirations' not in st.session_state:
        return False
    return inspiration_id in st.session_state.favorite_inspirations

def get_favorite_inspirations():
    """Pobiera ulubione inspiracje"""
    if 'favorite_inspirations' not in st.session_state:
        return []
    
    favorite_ids = st.session_state.favorite_inspirations
    all_inspirations = get_all_inspirations()
    
    favorites = []
    for insp in all_inspirations:
        if insp.get("id") in favorite_ids:
            favorites.append(insp)
    
    return favorites

def get_difficulty_emoji(difficulty):
    """Zwraca emoji dla poziomu trudności"""
    emoji_map = {
        "beginner": "🟢",
        "intermediate": "🟡", 
        "advanced": "🔴"
    }
    return emoji_map.get(difficulty, "⚪")

def get_difficulty_text(difficulty):
    """Zwraca tekst dla poziomu trudności"""
    text_map = {
        "beginner": "Początkujący",
        "intermediate": "Średnio zaawansowany",
        "advanced": "Zaawansowany"
    }
    return text_map.get(difficulty, "Nieokreślony")

def get_random_inspiration():
    """Zwraca losową inspirację"""
    import random
    inspirations = get_all_inspirations()
    if inspirations:
        return random.choice(inspirations)
    return None

def mark_inspiration_as_read(inspiration_id):
    """Oznacza inspirację jako przeczytaną"""
    if 'read_inspirations' not in st.session_state:
        st.session_state.read_inspirations = []
    
    if inspiration_id not in st.session_state.read_inspirations:
        st.session_state.read_inspirations.append(inspiration_id)

def is_inspiration_read(inspiration_id):
    """Sprawdza czy inspiracja została przeczytana"""
    if 'read_inspirations' not in st.session_state:
        return False
    return inspiration_id in st.session_state.read_inspirations

def get_read_inspirations():
    """Pobiera listę przeczytanych inspiracji"""
    if 'read_inspirations' not in st.session_state:
        return []
    
    read_ids = st.session_state.read_inspirations
    all_inspirations = get_all_inspirations()
    
    read_list = []
    for insp in all_inspirations:
        if insp.get("id") in read_ids:
            read_list.append(insp)
    
    return read_list
