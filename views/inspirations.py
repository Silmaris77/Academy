import streamlit as st
from utils.components import zen_header
from utils.material3_components import apply_material3_theme
from utils.layout import get_device_type, toggle_device_view

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
    
    st.write("w budowie")
