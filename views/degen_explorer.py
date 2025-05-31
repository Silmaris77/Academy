import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from data.test_questions import DEGEN_TYPES, TEST_QUESTIONS
from data.degen_details import degen_details
from data.users import load_user_data, save_user_data
from utils.components import zen_header, content_section, quote_block, tip_block, notification, zen_button, progress_bar
from utils.material3_components import apply_material3_theme
from utils.layout import get_device_type, responsive_grid, responsive_container, toggle_device_view, apply_responsive_styles, get_responsive_figure_size
from utils.achievements import check_achievements
import re

# Poprawka dla funkcji clean_html, aby była bardziej skuteczna
def clean_html(text):
    """Usuwa wszystkie tagi HTML z tekstu i normalizuje białe znaki"""
    # Najpierw usuń wszystkie tagi HTML
    text_without_tags = re.sub(r'<.*?>', '', text)
    # Normalizuj białe znaki (zamień wiele spacji, tabulacji, nowych linii na pojedyncze spacje)
    normalized_text = re.sub(r'\s+', ' ', text_without_tags)
    return normalized_text.strip()

def calculate_test_results(scores):
    """Calculate the dominant degen type based on test scores"""
    return max(scores.items(), key=lambda x: x[1])[0]

def plot_radar_chart(scores, device_type=None):
    """Generate a radar chart for test results
    
    Args:
        scores: Dictionary of degen types and their scores
        device_type: Device type ('mobile', 'tablet', or 'desktop')
    """
    # Jeśli device_type nie został przekazany, pobierz go
    if device_type is None:
        device_type = get_device_type()
        
    # Upewnij się, że labels i values są listami o tym samym rozmiarze
    labels = list(scores.keys())
    values = [float(v) for v in scores.values()]
    
    # Utwórz kąty i od razu skonwertuj na stopnie
    num_vars = len(labels)
    angles_degrees = np.linspace(0, 360, num_vars, endpoint=False)
    angles_radians = np.radians(angles_degrees)
    
    # Tworzenie zamkniętych list bez używania wycinków [:-1]
    values_closed = np.concatenate((values, [values[0]]))
    angles_radians_closed = np.concatenate((angles_radians, [angles_radians[0]]))
    
    # Użyj funkcji helper do ustalenia rozmiaru wykresu
    fig_size = get_responsive_figure_size(device_type)
    
    # Dostosuj pozostałe parametry w zależności od urządzenia
    if device_type == 'mobile':
        title_size = 14
        font_size = 6.5
        grid_alpha = 0.3
        line_width = 1.5
        marker_size = 4
    elif device_type == 'tablet':
        title_size = 16
        font_size = 8
        grid_alpha = 0.4
        line_width = 2
        marker_size = 5
    else:  # desktop
        title_size = 18
        font_size = 9
        grid_alpha = 0.5
        line_width = 2.5
        marker_size = 6
    
    # Tworzenie i konfiguracja wykresu
    fig, ax = plt.subplots(figsize=fig_size, subplot_kw=dict(polar=True))
    
    # Dodaj przezroczyste tło za etykietami dla lepszej czytelności
    ax.set_facecolor('white')
    if device_type == 'mobile':
        # Na telefonach zwiększ kontrast
        ax.set_facecolor('#f8f8f8')
    
    # Plot the radar chart with marker size adjusted for device
    ax.plot(angles_radians_closed, values_closed, 'o-', linewidth=line_width, markersize=marker_size)
    ax.fill(angles_radians_closed, values_closed, alpha=0.25)
    
    # Ensure we have a valid limit
    max_val = max(values) if max(values) > 0 else 1
    y_max = max_val * 1.2  # Add some padding at the top
    ax.set_ylim(0, y_max)
    
    # Adjust label positions and appearance for better device compatibility
    # For mobile, rotate labels to fit better on small screens
    if device_type == 'mobile':
        # Use shorter labels on mobile
        ax.set_thetagrids(angles_degrees, labels, fontsize=font_size-1)
        plt.setp(ax.get_xticklabels(), rotation=67.5)  # Rotate labels for better fit
    else:
        ax.set_thetagrids(angles_degrees, labels, fontsize=font_size)
    
    # Set title with responsive size
    ax.set_title("Twój profil inwestycyjny", size=title_size, pad=20)
    
    # Dostosuj siatkę i oś
    ax.grid(True, alpha=grid_alpha)
    
    # Dodaj etykiety z wartościami
    # Dostosuj odległość etykiet od wykresu
    label_pad = max_val * (0.05 if device_type == 'mobile' else 0.1)
    
    # Poprawiona wersja:
    for i, (angle, value) in enumerate(zip(angles_radians, values)):
        color = DEGEN_TYPES[labels[i]].get("color", "#3498db")
        
        # Na telefonach wyświetl tylko nazwę typu bez wyniku
        if device_type == 'mobile':
            display_text = f"{labels[i].split()[0]}"  # Use only the first word
        else:
            display_text = f"{labels[i]}\n({value})"
            
        # Add text labels with background for better visibility
        ax.text(angle, value + label_pad, display_text, 
                horizontalalignment='center', verticalalignment='center',
                fontsize=font_size, color=color, fontweight='bold',
                bbox=dict(facecolor='white', alpha=0.7, pad=1.5, edgecolor='none'))
    
    # Optimize layout
    plt.tight_layout(pad=1.0 if device_type == 'mobile' else 1.5)
    
    # Use high DPI for better rendering on high-resolution displays
    fig.set_dpi(120 if device_type == 'mobile' else 100)
    
    return fig

def show_degen_explorer():
    """
    Wyświetla stronę umożliwiającą eksplorację typów degenów oraz wykonanie testu
    """    
    # Zastosuj style Material 3
    apply_material3_theme()
    
    # Zastosuj responsywne style
    apply_responsive_styles()
    
    # Opcja wyboru urządzenia w trybie deweloperskim
    if st.session_state.get('dev_mode', False):
        toggle_device_view()
    
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    zen_header("Typy Degenów")
    
    # Utwórz tabs dla podsekcji
    tab1, tab2 = st.tabs(["Test Degena", "Eksplorator Typów"])
    
    with tab1:
        show_degen_test_tab()
    
    with tab2:
        show_degen_explorer_tab()
        
def show_degen_explorer_tab():
    """
    Wyświetla zakładkę umożliwiającą eksplorację wszystkich typów degenów 
    wraz z ich szczegółowymi opisami.
    """
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    # Wprowadzenie do typów degenów
    st.markdown("""
    ## 🔍 Poznaj różne style inwestycyjne
    
    Każdy inwestor ma unikalne podejście do rynków finansowych, uwarunkowane cechami osobowości,
    emocjami, strategiami i wzorcami zachowań. Poniżej znajdziesz szczegółowe opisy wszystkich
    typów degenów, które pomogą Ci zrozumieć różne style inwestycyjne i ich implikacje.
    
    Wybierz interesujący Cię typ degena z listy i odkryj:
    - Charakterystykę głównych cech
    - Profil emocjonalny
    - Zachowania i postawy
    - Neurobiologiczne podstawy
    - Kluczowe wyzwania
    - Ścieżkę rozwoju inwestorskiego
    """)
    
    # Wybór typu degena
    selected_type = st.selectbox(
        "Wybierz typ degena do szczegółowej analizy:",
        list(DEGEN_TYPES.keys()),
        format_func=lambda x: f"{x} - {DEGEN_TYPES[x]['description'][:50]}..."
    )
    
    if selected_type:
        # Tworzenie sekcji dla wybranego typu
        color = DEGEN_TYPES[selected_type]["color"]
        content_section(
            f"{selected_type}", 
            DEGEN_TYPES[selected_type]["description"],
            icon="🔍",
            border_color=color,
            collapsed=False
        )
        
        # Mocne strony i wyzwania w dwóch kolumnach
        if device_type == 'mobile':
            # Na telefonach wyświetl sekcje jedna pod drugą
            content_section("Mocne strony:", 
                           "\n".join([f"- ✅ {strength}" for strength in DEGEN_TYPES[selected_type]["strengths"]]), 
                           icon="💪", 
                           collapsed=False)
            
            content_section("Wyzwania:", 
                           "\n".join([f"- ⚠️ {challenge}" for challenge in DEGEN_TYPES[selected_type]["challenges"]]), 
                           icon="🚧", 
                           collapsed=False)
        else:
            col1, col2 = st.columns(2)
            with col1:
                content_section("Mocne strony:", 
                                "\n".join([f"- ✅ {strength}" for strength in DEGEN_TYPES[selected_type]["strengths"]]), 
                                icon="💪", 
                                collapsed=False)
            
            with col2:
                content_section("Wyzwania:", 
                            "\n".join([f"- ⚠️ {challenge}" for challenge in DEGEN_TYPES[selected_type]["challenges"]]), 
                            icon="🚧", 
                            collapsed=False)
        
        # Rekomendowana strategia jako tip_block
        tip_block(clean_html(DEGEN_TYPES[selected_type]["strategy"]), title="Rekomendowana strategia", icon="🎯")
        
        # Szczegółowy opis z degen_details.py
        st.markdown("---")
        st.subheader("Szczegółowa analiza typu")
        if selected_type in degen_details:
            content_section(
                "Pełny opis",
                degen_details[selected_type],
                icon="📚",
                collapsed=True
            )
        else:
            notification("Szczegółowy opis dla tego typu degena nie jest jeszcze dostępny.", type="warning")
        
        # Porównanie z innymi typami
        st.markdown("---")
        st.subheader("Porównaj z innymi typami")
        
        # Pozwól użytkownikowi wybrać drugi typ do porównania
        comparison_type = st.selectbox(
            "Wybierz typ degena do porównania:",
            [t for t in DEGEN_TYPES.keys() if t != selected_type],
            format_func=lambda x: f"{x} - {DEGEN_TYPES[x]['description'][:50]}..."
        )
        if comparison_type:
            # Tabela porównawcza
            col1, col2 = st.columns(2)
            
            # Przygotuj listy poza f-stringiem dla pierwszego typu
            strengths_list_1 = "\n".join([f"- ✅ {strength}" for strength in DEGEN_TYPES[selected_type]["strengths"]])
            challenges_list_1 = "\n".join([f"- ⚠️ {challenge}" for challenge in DEGEN_TYPES[selected_type]["challenges"]])
            strategy_text_1 = clean_html(DEGEN_TYPES[selected_type]["strategy"])
            
            # Dla pierwszego typu (wybranego)
            with col1:
                content_section(
                    selected_type,
                    f"""**Opis:** {DEGEN_TYPES[selected_type]['description']}
        
**Mocne strony:**
{strengths_list_1}

**Wyzwania:**
{challenges_list_1}

**Strategia:**
{strategy_text_1}
                    """,
                    icon="🔍",
                    border_color=DEGEN_TYPES[selected_type]["color"],
                    collapsed=False
                )
            
            # Przygotuj listy poza f-stringiem dla drugiego typu
            strengths_list_2 = "\n".join([f"- ✅ {strength}" for strength in DEGEN_TYPES[comparison_type]["strengths"]])
            challenges_list_2 = "\n".join([f"- ⚠️ {challenge}" for challenge in DEGEN_TYPES[comparison_type]["challenges"]])
            strategy_text_2 = clean_html(DEGEN_TYPES[comparison_type]["strategy"])
            
            # Dla drugiego typu (porównywanego)
            with col2:
                content_section(
                    comparison_type,
                    f"""**Opis:** {DEGEN_TYPES[comparison_type]['description']}
        
**Mocne strony:**
{strengths_list_2}

**Wyzwania:**
{challenges_list_2}

**Strategia:**
{strategy_text_2}
                    """,
                    icon="🔍",
                    border_color=DEGEN_TYPES[comparison_type]["color"],
                    collapsed=False
                )
      # Nawigacja
    st.markdown("---")
    
    # Przycisk do powrotu do dashboardu
    if zen_button("🏠 Powrót do dashboardu", key="back_to_dashboard", use_container_width=True):
        st.session_state.page = 'dashboard'
        st.rerun()

def show_degen_test_tab():
    """
    Wyświetla zakładkę z testem typu degena na stronie eksploratora.
    """
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    # Informacja o teście
    if 'show_test_info' not in st.session_state:
        st.session_state.show_test_info = True
    
    if st.session_state.show_test_info:
        st.markdown("""
        ### 👉 Jak działa ten test?

        Ten test pomoże Ci sprawdzić, **jakim typem inwestora (degena)** jesteś.

        - Każde pytanie ma **8 odpowiedzi** – każda reprezentuje inny styl inwestycyjny.
        - **Wybierz tę odpowiedź, która najlepiej opisuje Twoje zachowanie lub sposób myślenia.**
        - Po zakończeniu zobaczysz graficzny wynik w postaci wykresu radarowego.        🧩 Gotowy? 
        """)
        if zen_button("Rozpocznij test"):
            st.session_state.show_test_info = False
            if 'test_step' not in st.session_state:
                st.session_state.test_step = 0
                st.session_state.test_scores = {degen_type: 0 for degen_type in DEGEN_TYPES}
            st.rerun()
    
    # Tryb testu    
    elif 'test_step' not in st.session_state:
        st.session_state.test_step = 0
        st.session_state.test_scores = {degen_type: 0 for degen_type in DEGEN_TYPES}
        st.rerun()
    
    elif st.session_state.test_step < len(TEST_QUESTIONS):
        # Display current question
        question = TEST_QUESTIONS[st.session_state.test_step]
        
        st.markdown("<div class='st-bx'>", unsafe_allow_html=True)
        st.subheader(f"Pytanie {st.session_state.test_step + 1} z {len(TEST_QUESTIONS)}")
        st.markdown(f"### {question['question']}")
        
        # Render options in two columns
        options = question['options']
        
        # Użyj responsywnego układu w zależności od typu urządzenia
        if device_type == 'mobile':
            # Na telefonach wyświetl opcje jedna pod drugą
            for i in range(len(options)):
                if zen_button(f"{options[i]['text']}", key=f"q{st.session_state.test_step}_opt{i}", use_container_width=True):
                    # Add scores for the answer
                    for degen_type, score in options[i]['scores'].items():
                        st.session_state.test_scores[degen_type] += score
                    
                    st.session_state.test_step += 1
                    st.rerun()
        else:
            # Na tabletach i desktopach użyj dwóch kolumn
            col1, col2 = st.columns(2)
            for i in range(len(options)):
                if i < len(options) // 2:
                    with col1:
                        if zen_button(f"{options[i]['text']}", key=f"q{st.session_state.test_step}_opt{i}", use_container_width=True):
                            # Add scores for the answer
                            for degen_type, score in options[i]['scores'].items():
                                st.session_state.test_scores[degen_type] += score
                            
                            st.session_state.test_step += 1
                            st.rerun()
                else:
                    with col2:
                        if zen_button(f"{options[i]['text']}", key=f"q{st.session_state.test_step}_opt{i}", use_container_width=True):
                            # Add scores for the answer
                            for degen_type, score in options[i]['scores'].items():
                                st.session_state.test_scores[degen_type] += score
                            
                            st.session_state.test_step += 1
                            st.rerun()
        
        # Progress bar
        progress_value = st.session_state.test_step / len(TEST_QUESTIONS)
        progress_bar(progress=progress_value, color="#4CAF50")
        st.markdown(f"**Postęp testu: {int(progress_value * 100)}%**")
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        # Show test results
        show_test_results()

def show_test_results():
    """
    Wyświetla wyniki testu typu degena.
    """
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    # Calculate dominant type
    dominant_type = calculate_test_results(st.session_state.test_scores)      # Update user data
    users_data = load_user_data()
    from utils.time_utils import get_current_timestamp
    
    users_data[st.session_state.username]["degen_type"] = dominant_type
    users_data[st.session_state.username]["test_taken"] = True
    users_data[st.session_state.username]["test_scores"] = st.session_state.test_scores  # Save test scores
    users_data[st.session_state.username]["test_completion_date"] = get_current_timestamp()  # Save completion timestamp
    users_data[st.session_state.username]["xp"] += 50  # Bonus XP for completing the test
    save_user_data(users_data)
    
    # Check for achievements after test completion
    check_achievements(st.session_state.username)
    
    st.markdown("<div class='st-bx'>", unsafe_allow_html=True)
    st.subheader("Wyniki testu")
    
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h2>Twój dominujący typ Degena to:</h2>
        <h1 style='color: {DEGEN_TYPES[dominant_type]["color"]};'>{dominant_type}</h1>
        <p>{DEGEN_TYPES[dominant_type]["description"]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Radar chart
    radar_fig = plot_radar_chart(st.session_state.test_scores, device_type=device_type)
    
    # Add mobile-specific styles for the chart container
    if device_type == 'mobile':
        st.markdown("""
        <style>
        .radar-chart-container {
            margin: 0 -20px; /* Negative margin to use full width on mobile */
            padding-bottom: 15px;
        }
        </style>
        <div class="radar-chart-container">
        """, unsafe_allow_html=True)
        
    st.pyplot(radar_fig)
    
    if device_type == 'mobile':
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Display strengths and challenges based on device type
    if device_type == 'mobile':
        # Na telefonach wyświetl sekcje jedna pod drugą
        content_section(
            "Twoje mocne strony:", 
            "\n".join([f"- ✅ {strength}" for strength in DEGEN_TYPES[dominant_type]["strengths"]]),
            icon="💪",
            collapsed=False
        )
        
        content_section(
            "Twoje wyzwania:", 
            "\n".join([f"- ⚠️ {challenge}" for challenge in DEGEN_TYPES[dominant_type]["challenges"]]),
            icon="🚧",
            collapsed=False
        )
    else:
        # Na tabletach i desktopach użyj dwóch kolumn
        col1, col2 = st.columns(2)
        with col1:
            content_section(
                "Twoje mocne strony:", 
                "\n".join([f"- ✅ {strength}" for strength in DEGEN_TYPES[dominant_type]["strengths"]]),
                icon="💪",
                collapsed=False
            )
        with col2:
            content_section(
                "Twoje wyzwania:", 
                "\n".join([f"- ⚠️ {challenge}" for challenge in DEGEN_TYPES[dominant_type]["challenges"]]),
                icon="🚧",
                collapsed=False
            )
    
    tip_block(DEGEN_TYPES[dominant_type]["strategy"], title="Rekomendowana strategia", icon="🎯")
    
    # Dodanie szczegółowych informacji o typie degena
    content_section(
        "Szczegółowy opis twojego typu degena", 
        degen_details.get(dominant_type, "Szczegółowy opis dla tego typu degena nie jest jeszcze dostępny."),
        icon="🔍",
        collapsed=True
    )
      # Additional options
    if zen_button("Wykonaj test ponownie"):
        st.session_state.test_step = 0
        st.session_state.test_scores = {degen_type: 0 for degen_type in DEGEN_TYPES}
        st.session_state.show_test_info = True
        st.rerun()
