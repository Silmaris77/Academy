﻿import streamlit as st
from data.lessons import load_lessons
from data.users import load_user_data, save_user_data
from utils.components import zen_header, zen_button, notification, content_section, tip_block, quote_block, progress_bar, embed_content, lesson_card
from utils.material3_components import apply_material3_theme
from utils.layout import get_device_type, responsive_grid, responsive_container, toggle_device_view
from utils.lesson_progress import (
    award_fragment_xp, get_lesson_fragment_progress, calculate_lesson_completion,
    is_lesson_fully_completed, get_fragment_xp_breakdown, mark_lesson_as_completed
)
from utils.real_time_updates import get_live_user_stats, live_xp_indicator, show_xp_notification

def get_difficulty_stars(difficulty):
    """Konwertuje poziom trudności (liczba lub tekst) na odpowiednią liczbę gwiazdek."""
    difficulty_map = {
        "beginner": 1,
        "podstawowy": 1,
        "intermediate": 2,
        "średni": 2,
        "średniozaawansowany": 3,
        "advanced": 4,
        "zaawansowany": 4,
        "expert": 5,
        "ekspercki": 5
    }
    
    if isinstance(difficulty, str):
        difficulty_level = difficulty_map.get(difficulty.lower(), 1)
    else:
        pass
        try:
            difficulty_level = int(difficulty)
        except (ValueError, TypeError):
            difficulty_level = 1
    
    return '⭐' * difficulty_level

def show_lesson():
    """Show lesson view"""
    
    # Zastosuj style Material 3
    apply_material3_theme()
    
    # Opcja wyboru urządzenia w trybie deweloperskim
    if st.session_state.get('dev_mode', False):
        toggle_device_view()
    
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    zen_header("Kurs Zen Degen Academy")
    lessons = load_lessons()
    
    # Check if we're viewing a specific lesson or the overview
    if 'current_lesson' not in st.session_state or not st.session_state.current_lesson:
        # WIDOK PRZEGLĄDU LEKCJI
        st.subheader("Dostępne lekcje")
          # Pobierz dane użytkownika dla oznaczenia ukończonych lekcji
        from data.users import get_current_user_data
        user_data = get_current_user_data(st.session_state.username)
        completed_lessons = user_data.get('completed_lessons', [])
        
        # Grupuj lekcje według kategorii
        lessons_by_category = {}
        for lesson_id, lesson in lessons.items():
            category = lesson.get("category", "Inne")
            if category not in lessons_by_category:
                lessons_by_category[category] = []
            lessons_by_category[category].append((lesson_id, lesson))
          # Wyświetl lekcje w podziale na kategorie
        for category, category_lessons in lessons_by_category.items():
            st.markdown(f"## {category}")         
            #    # Wyświetlaj każdą kartę lekcji na całą szerokość wiersza
            # for i, (lesson_id, lesson) in enumerate(category_lessons):
            #     # Sprawdź, czy lekcja jest ukończona
            #     is_completed = lesson_id in completed_lessons
                
            #     # Użyj komponentu lesson_card zamiast ręcznego HTML
            #     lesson_card(
            #         title=lesson.get('title', 'Lekcja'),
            #         description=lesson.get('description', 'Ta lekcja wprowadza podstawowe zasady...'),
            #         xp=lesson.get('xp_reward', 30),
            #         difficulty=lesson.get('difficulty', 'beginner'),
            #         category=lesson.get('tag', category),
            #         completed=is_completed,                    button_text="Powtórz lekcję" if is_completed else "Rozpocznij",
            #         button_key=f"start_{lesson_id}",
            #         lesson_id=lesson_id,
            #         on_click=lambda lesson_id=lesson_id: (
            #             setattr(st.session_state, 'current_lesson', lesson_id),
            #             setattr(st.session_state, 'lesson_step', 'intro'),
            #             setattr(st.session_state, 'quiz_score', 0) if 'quiz_score' in st.session_state else None,
            #             st.rerun()
            #         )
            #     )
                        # Utwórz kolumny dla responsywnego układu
            # Na urządzeniach mobilnych - 1 kolumna, na desktopie - 2 kolumny
            if device_type == 'mobile':
                columns = st.columns(1)
            else:
                columns = st.columns(2)
            
            # Wyświetlaj lekcje w kolumnach
            for i, (lesson_id, lesson) in enumerate(category_lessons):
                # Sprawdź, czy lekcja jest ukończona
                is_completed = lesson_id in completed_lessons
                
                # Wybierz kolumnę (naprzemiennie dla 2 kolumn, zawsze pierwsza dla 1 kolumny)
                column_index = i % len(columns)
                
                with columns[column_index]:
                    lesson_card(
                        title=lesson.get('title', 'Lekcja'),
                        description=lesson.get('description', 'Ta lekcja wprowadza podstawowe zasady...'),
                        xp=lesson.get('xp_reward', 30),
                        difficulty=lesson.get('difficulty', 'beginner'),
                        category=lesson.get('tag', category),
                        completed=is_completed,
                        button_text="Powtórz lekcję" if is_completed else "Rozpocznij",
                        button_key=f"start_{lesson_id}",
                        lesson_id=lesson_id,
                        on_click=lambda lesson_id=lesson_id: (
                            setattr(st.session_state, 'current_lesson', lesson_id),
                            setattr(st.session_state, 'lesson_step', 'intro'),
                            setattr(st.session_state, 'quiz_score', 0) if 'quiz_score' in st.session_state else None,
                            st.rerun()
                        )
                    )
   
    else:
        # Kod wyświetlania pojedynczej lekcji
        lesson_id = st.session_state.current_lesson
        if lesson_id not in lessons:
            st.error("Nie znaleziono wybranej lekcji.")
            return
            
        lesson = lessons[lesson_id]
        
        if 'lesson_step' not in st.session_state:
            st.session_state.lesson_step = 'intro'
        if 'quiz_score' not in st.session_state:
            st.session_state.quiz_score = 0
          # Get current user's lesson progress using the new fragment system
        fragment_progress = get_lesson_fragment_progress(lesson_id)        # Initialize legacy session progress for UI compatibility
        if 'lesson_progress' not in st.session_state:
            st.session_state.lesson_progress = {
                'intro': fragment_progress.get('intro_completed', False),
                'opening_quiz': fragment_progress.get('opening_quiz_completed', False),
                'content': fragment_progress.get('content_completed', False),
                'practical_exercises': fragment_progress.get('practical_exercises_completed', False),
                'reflection': fragment_progress.get('reflection_completed', False),  # backward compatibility
                'application': fragment_progress.get('application_completed', False),  # backward compatibility
                'closing_quiz': fragment_progress.get('closing_quiz_completed', False),
                'summary': fragment_progress.get('summary_completed', False),
                'total_xp_earned': fragment_progress.get('total_xp_earned', 0),
                'steps_completed': 0,
                'quiz_scores': {},
                'answers': {}
            }
        
        # Oblicz całkowitą liczbę dostępnych kroków w tej lekcji
        available_steps = ['intro', 'content', 'summary']
        if 'sections' in lesson:
            if 'opening_quiz' in lesson.get('sections', {}):
                available_steps.append('opening_quiz')
            if 'practical_exercises' in lesson.get('sections', {}):
                available_steps.append('practical_exercises')
            elif 'reflection' in lesson.get('sections', {}) or 'application' in lesson.get('sections', {}):
                # Backward compatibility dla starszych lekcji
                if 'reflection' in lesson.get('sections', {}):
                    available_steps.append('reflection')
                if 'application' in lesson.get('sections', {}):
                    available_steps.append('application')
            if 'closing_quiz' in lesson.get('sections', {}):
                available_steps.append('closing_quiz')
        
        # Ustal kolejność kroków
        step_order = ['intro']
        if 'opening_quiz' in available_steps:
            step_order.append('opening_quiz')
        step_order.extend(['content'])
        
        # Nowa sekcja ćwiczeń praktycznych zamiast osobnych reflection i application
        if 'practical_exercises' in available_steps:
            step_order.append('practical_exercises')
        elif 'reflection' in available_steps or 'application' in available_steps:
            # Backward compatibility dla starszych lekcji
            if 'reflection' in available_steps:
                step_order.append('reflection')
            if 'application' in available_steps:
                step_order.append('application')
        
        if 'closing_quiz' in available_steps:
            step_order.append('closing_quiz')
        step_order.append('summary')
        
        total_steps = len(step_order)
        base_xp = lesson.get('xp_reward', 100)

        # Mapowanie kroków do nazw wyświetlanych
        step_names = {
            'intro': 'Wprowadzenie',
            'opening_quiz': 'Samorefleksja',
            'content': 'Materiał',
            'practical_exercises': 'Ćwiczenia praktyczne',
            'reflection': 'Refleksja',  # backward compatibility
            'application': 'Zadania praktyczne',  # backward compatibility
            'closing_quiz': 'Quiz końcowy',
            'summary': 'Podsumowanie'
        }

        # Mapowanie kroków do wartości XP (nowy system procentowy)
        step_xp_values = {
            'intro': int(base_xp * 0.05),          # 5% całkowitego XP
            'opening_quiz': int(base_xp * 0.00),   # 0% całkowitego XP
            'content': int(base_xp * 0.30),        # 30% całkowitego XP (Merytoryka)
            'practical_exercises': int(base_xp * 0.40),  # 40% całkowitego XP (nowa połączona sekcja)
            'reflection': int(base_xp * 0.20),     # 20% całkowitego XP (backward compatibility)
            'application': int(base_xp * 0.20),    # 20% całkowitego XP (backward compatibility)
            'closing_quiz': int(base_xp * 0.20),   # 20% całkowitego XP
            'summary': int(base_xp * 0.05)         # 5% całkowitego XP
        }
        
        # Oblicz rzeczywiste maksimum XP jako sumę wszystkich dostępnych kroków
        max_xp = sum(step_xp_values[step] for step in step_order)
          # Znajdź indeks obecnego kroku i następnego kroku
        current_step_idx = step_order.index(st.session_state.lesson_step) if st.session_state.lesson_step in step_order else 0
        next_step_idx = min(current_step_idx + 1, len(step_order) - 1)
        next_step = step_order[next_step_idx]
        
        # Style dla paska postępu i interfejsu
        st.markdown("""
        <style>
        .progress-container {
            background-color: #f0f2f6;
            border-radius: 10px;
            padding: 10px 15px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .progress-text {
            font-weight: bold;
            font-size: 16px;
        }
        .xp-counter {
            color: #4CAF50;
            font-weight: bold;
            font-size: 18px;
        }
        .stTabs [data-baseweb="tab-panel"] {
            padding: 25px 15px 15px 15px;
        }        .next-button {
            margin-top: 20px;
            text-align: center;
        }
        
        /* Style dla expanderów */
        .st-emotion-cache-1oe5cao {
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 16px;
            background-color: rgba(248,249,251,0.8);
        }
        .st-emotion-cache-1oe5cao:hover {
            background-color: rgba(242,244,248,1); 
        }
        .st-emotion-cache-16idsys p {
            font-size: 1rem;
            line-height: 1.6;
        }
        .st-expander {
            border: none !important;
        }

        /* Specjalne style dla urządzeń mobilnych */
        @media (max-width: 768px) {
            /* Większy obszar klikalny dla expanderów */
            .st-expander {
                margin-bottom: 12px;
            }
            
            .st-expander .st-emotion-cache-16idsys p {
                font-size: 0.95rem; /* Nieco mniejsza czcionka na małych ekranach */
            }
            
            /* Zwiększony obszar kliknięcia dla nagłówka expandera */
            .st-expander-header {
                padding: 15px 10px !important;
                font-size: 1.1rem !important;
                font-weight: 600 !important;
                min-height: 50px;
            }
            
            /* Dodaj wskaźnik rozwijania */
            .st-expander:not(.st-emotion-cache-xujm5h) .st-expander-header::after {
                content: '▼';
                float: right;
                margin-left: 10px;
                transition: transform 0.3s;
            }
            
            .st-expander.st-emotion-cache-xujm5h .st-expander-header::after {
                content: '▲';
                float: right;
                margin-left: 10px;
            }        }
        </style>
        """, unsafe_allow_html=True)

        # Lesson navigation in sidebar
        with st.sidebar:
            st.markdown("<h3>Nawigacja lekcji</h3>", unsafe_allow_html=True)
            
            # Dodaj przycisk powrotu do przeglądu lekcji
            if zen_button("Wszystkie lekcje", use_container_width=True):
                st.session_state.current_lesson = None
                st.rerun()
            
            # Wyświetl pełną mapę kroków lekcji z zaznaczeniem obecnego
            st.markdown("<h4>Mapa lekcji:</h4>", unsafe_allow_html=True)
            
            # Dodaj style dla przycisków nawigacji
            st.markdown("""
            <style>
            .nav-btn-current {
                background-color: #2196F3 !important;
                color: white !important;
                font-weight: bold !important;
                pointer-events: none;
            }
            .nav-btn-completed {
                background-color: #4CAF50 !important;
                color: white !important;
            }
            .nav-btn-locked {
                background-color: #f0f2f6 !important;
                color: #666 !important;
                pointer-events: none;
            }
            </style>
            """, unsafe_allow_html=True)

            for i, step in enumerate(step_order):
                if step in available_steps:
                    step_name = step_names.get(step, step.capitalize())
                    
                    # Sprawdź status kroku
                    is_completed = st.session_state.lesson_progress.get(step, False)
                    is_current = (step == st.session_state.lesson_step)
                    
                    # Ikony statusu
                    check_icon = "✅ " if is_completed else ""
                    current_icon = "👉 " if is_current else ""
                    
                    # Tekst przycisku - bez ikony dla aktualnego kroku jeśli jest już ikona ukończenia
                    if is_current and is_completed:
                        button_text = f"{current_icon}{i+1}. {step_name}"
                    else:
                        button_text = f"{current_icon if is_current else ''}{check_icon if is_completed and not is_current else ''}{i+1}. {step_name}"
                    
                    # Wyświetl element w odpowiednim stylu
                    if is_current:
                        # Element aktualny - niebieski przycisk (ten sam kształt co ukończone elementy)
                        st.button(button_text, key=f"current_step_{step}", disabled=True, use_container_width=True)
                        # Stylizuj przycisk za pomocą CSS
                        st.markdown("""
                        <style>
                        button[data-testid="baseButton-secondary"]:disabled {
                            background-color: #1976D2 !important;
                            color: white !important;
                            opacity: 1 !important;
                            font-weight: bold !important;
                            cursor: default !important;
                            border-radius: 5px !important;
                            box-shadow: none !important;
                        }
                        </style>
                        """, unsafe_allow_html=True)
                    elif is_completed:
                        # Ukończony element - zielony, klikalny
                        if st.button(button_text, key=f"completed_step_{step}", use_container_width=True):
                            # Przejdź do wybranego kroku po kliknięciu
                            st.session_state.lesson_step = step
                            st.rerun()
                        # Stylizuj przycisk za pomocą CSS
                        st.markdown("""
                        <style>
                        button[data-testid="baseButton-secondary"]:not(:disabled) {
                            background-color: #4CAF50 !important;
                            color: white !important;
                            border-radius: 5px !important;
                        }
                        </style>
                        """, unsafe_allow_html=True)
                    else:
                        # Przyszły element - szary div
                        st.markdown(
                            f"""
                            <div style="color: #666; padding: 8px; 
                                      border-radius: 5px; margin-bottom: 5px; text-align: center;">
                                {i+1}. {step_name}
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )

        # Main content
        st.markdown("<div class='st-bx'>", unsafe_allow_html=True)
          # Nagłówek sekcji
        current_section_title = step_names.get(st.session_state.lesson_step, st.session_state.lesson_step.capitalize())
        if st.session_state.lesson_step == 'opening_quiz':
            current_section_title = "🪞 Narzędzie Samorefleksji"
        st.markdown(f"<h1>{current_section_title}</h1>", unsafe_allow_html=True)
        
        # Main content logic for each step
        if st.session_state.lesson_step == 'intro':
            # Podziel wprowadzenie na dwie zakładki
            intro_tabs = st.tabs(["Wprowadzenie", "Case Study"])
            
            with intro_tabs[0]:
                # Wyświetl główne wprowadzenie
                if isinstance(lesson.get("intro"), dict) and "main" in lesson["intro"]:
                    st.markdown(lesson["intro"]["main"], unsafe_allow_html=True)
                elif isinstance(lesson.get("intro"), str):
                    st.markdown(lesson["intro"], unsafe_allow_html=True)
                else:
                    st.warning("Brak treści wprowadzenia.")
            
            with intro_tabs[1]:
                # Wyświetl studium przypadku
                if isinstance(lesson.get("intro"), dict) and "case_study" in lesson["intro"]:
                    st.markdown(lesson["intro"]["case_study"], unsafe_allow_html=True)
                else:
                    st.warning("Brak studium przypadku w tej lekcji.")
              # Przycisk "Dalej" po wprowadzeniu            st.markdown("<div class='next-button'>", unsafe_allow_html=True)
            if zen_button(f"Dalej: {step_names.get(next_step, next_step.capitalize())}", use_container_width=False):
                # Award fragment XP using the new system
                success, xp_awarded = award_fragment_xp(lesson_id, 'intro', step_xp_values['intro'])
                
                if success and xp_awarded > 0:
                    # Update session state for UI compatibility
                    st.session_state.lesson_progress['intro'] = True
                    st.session_state.lesson_progress['steps_completed'] += 1
                    st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                      # Show real-time XP notification
                    show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za ukończenie wprowadzenia!")
                    
                    # Refresh user data for real-time updates
                    from utils.real_time_updates import refresh_user_data
                    refresh_user_data()                # Przejdź do następnego kroku
                st.session_state.lesson_step = next_step
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        elif st.session_state.lesson_step == 'opening_quiz' and 'opening_quiz' in lesson.get('sections', {}):
            # Wyświetl quiz startowy (diagnostyczny)
            st.info("🪞 **Narzędzie Samorefleksji** - Ten quiz pomaga Ci lepiej poznać siebie jako inwestora. Nie ma tu dobrych ani złych odpowiedzi - chodzi o szczerą autorefleksję. Twoje odpowiedzi nie wpływają na postęp w lekcji.")
            
            quiz_data = lesson['sections']['opening_quiz']
            quiz_complete, _, earned_points = display_quiz(quiz_data)
            
            # Natychmiast oznacz quiz jako ukończony w nawigacji po ukończeniu
            if quiz_complete:
                st.session_state.lesson_progress['opening_quiz'] = True
              # Dodaj opcję pominięcia quizu
            st.markdown("---")
            st.markdown("**Twoje opcje:**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Przycisk "Pomiń quiz" - zawsze dostępny
                st.markdown("<div class='next-button'>", unsafe_allow_html=True)
                if zen_button("⏭️ Przejdź do lekcji", use_container_width=True):
                    # Oznacz quiz jako pominięty (ale ukończony dla nawigacji)
                    st.session_state.lesson_progress['opening_quiz'] = True
                    
                    # Nie przyznawaj XP za pominięcie quizu
                    st.info("💭 W porządku! Przejdźmy do materiału lekcji. Zawsze możesz wrócić do samorefleksji później.")
                      # Przejdź do następnego kroku
                    st.session_state.lesson_step = next_step
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2:
                # Przycisk "Dalej" po quizie startowym - dostępny zawsze (niezależnie od wyniku)
                st.markdown("<div class='next-button'>", unsafe_allow_html=True)
                button_text = "Rozpocznij refleksję" if not quiz_complete else "Kontynuuj"
                if zen_button(button_text, use_container_width=True):
                    # Award fragment XP using the new system for quiz participation (nie za wynik)
                    success, xp_awarded = award_fragment_xp(lesson_id, 'opening_quiz', step_xp_values['opening_quiz'])
                    
                    if success and xp_awarded > 0:
                        # Update session state for UI compatibility
                        st.session_state.lesson_progress['opening_quiz'] = True
                        st.session_state.lesson_progress['steps_completed'] += 1
                        st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                        
                        # Show real-time XP notification
                        show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za szczerą samorefleksję!")
                        
                        # Refresh user data for real-time updates
                        from utils.real_time_updates import refresh_user_data
                        refresh_user_data()
                    
                    # Przejdź do następnego kroku
                    st.session_state.lesson_step = next_step
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
        
        elif st.session_state.lesson_step == 'content':
            # Diagnozowanie problemu z wyświetlaniem treści
            if 'sections' not in lesson:
                st.error("Lekcja nie zawiera klucza 'sections'!")
            elif 'learning' not in lesson.get('sections', {}):
                st.error("Lekcja nie zawiera sekcji 'learning'!")
            elif 'sections' not in lesson['sections'].get('learning', {}):
                st.error("Sekcja 'learning' nie zawiera klucza 'sections'!")
            else:                # Sprawdź, czy sekcja learning istnieje i czy zawiera sections
                for i, section in enumerate(lesson["sections"]["learning"]["sections"]):
                    with st.expander(section.get("title", f"Sekcja {i+1}"), expanded=False):
                        st.markdown(section.get("content", "Brak treści"), unsafe_allow_html=True)            # Przycisk "Dalej" po treści lekcji
            st.markdown("<div class='next-button'>", unsafe_allow_html=True)
            if zen_button(f"Dalej: {step_names.get(next_step, next_step.capitalize())}", use_container_width=False):
                # Award fragment XP using the new system
                success, xp_awarded = award_fragment_xp(lesson_id, 'content', step_xp_values['content'])
                
                if success and xp_awarded > 0:
                    # Update session state for UI compatibility
                    st.session_state.lesson_progress['content'] = True
                    st.session_state.lesson_progress['steps_completed'] += 1
                    st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                      # Show real-time XP notification
                    show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za zapoznanie się z materiałem!")
                    
                    # Refresh user data for real-time updates
                    from utils.real_time_updates import refresh_user_data
                    refresh_user_data()
                
                # Przejdź do następnego kroku
                st.session_state.lesson_step = next_step
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        elif st.session_state.lesson_step == 'practical_exercises':
            # Nowa sekcja ćwiczeń praktycznych z pod-zakładkami
            if 'sections' not in lesson:
                st.error("Lekcja nie zawiera klucza 'sections'!")
            elif 'practical_exercises' not in lesson.get('sections', {}):
                st.error("Lekcja nie zawiera sekcji 'practical_exercises'!")
            else:
                practical_data = lesson['sections']['practical_exercises']
                
                # Sprawdź czy dane zawierają tabs
                if 'tabs' not in practical_data:
                    st.error("Sekcja 'practical_exercises' nie zawiera 'tabs'!")
                else:
                    # Przygotuj zakładki dla różnych typów ćwiczeń
                    sub_tabs_data = practical_data['tabs']
                    available_tabs = []
                    tab_keys = []
                      # Sprawdź które zakładki są dostępne i przygotuj je w logicznej kolejności uczenia się
                    # 1. Autotest - sprawdzenie aktualnego stanu
                    if 'autotest' in sub_tabs_data:
                        available_tabs.append("🧠 Autotest")
                        tab_keys.append('autotest')
                    
                    # 2. Refleksja - przemyślenie własnych doświadczeń
                    if 'reflection' in sub_tabs_data:
                        available_tabs.append("📝 Refleksja")
                        tab_keys.append('reflection')
                    
                    # 3. Analiza - case studies i scenariusze
                    if 'analysis' in sub_tabs_data:
                        available_tabs.append("📊 Analiza")
                        tab_keys.append('analysis')
                    
                    # 4. Wdrożenie - konkretny plan działania
                    if 'implementation' in sub_tabs_data:
                        available_tabs.append("🎯 Wdrożenie")
                        tab_keys.append('implementation')
                    
                    if available_tabs:
                        # Wyświetl pod-zakładki
                        tabs = st.tabs(available_tabs)
                        
                        for i, (tab_key, tab_title) in enumerate(zip(tab_keys, available_tabs)):
                            with tabs[i]:
                                tab_data = sub_tabs_data[tab_key]
                                
                                # Wyświetl opis zakładki jeśli istnieje
                                if 'description' in tab_data:
                                    st.info(tab_data['description'])
                                
                                # Wyświetl sekcje w zakładce
                                if 'sections' in tab_data:
                                    for section in tab_data['sections']:
                                        st.markdown(f"### {section.get('title', 'Sekcja')}")
                                        st.markdown(section.get('content', 'Brak treści'), unsafe_allow_html=True)
                                        
                                        # Jeśli sekcja wymaga odpowiedzi użytkownika
                                        if section.get('interactive', False):
                                            # Generuj klucz dla przechowywania odpowiedzi
                                            section_key = f"practical_{tab_key}_{section.get('title', '').replace(' ', '_').lower()}"
                                            
                                            # Użyj formularza dla lepszego UX
                                            with st.form(key=f"form_{section_key}"):
                                                # Pobierz istniejącą odpowiedź (jeśli jest)
                                                existing_response = st.session_state.get(section_key, "")
                                                
                                                # Wyświetl pole tekstowe z istniejącą odpowiedzią
                                                user_response = st.text_area(
                                                    "Twoja odpowiedź:",
                                                    value=existing_response,
                                                    height=200,
                                                    key=f"input_{section_key}"
                                                )
                                                
                                                # Przycisk do zapisywania odpowiedzi w formularzu
                                                submitted = st.form_submit_button("Zapisz odpowiedź")
                                                
                                                if submitted:
                                                    # Zapisz odpowiedź w stanie sesji
                                                    st.session_state[section_key] = user_response
                                                    st.success("Twoja odpowiedź została zapisana!")
                                else:
                                    st.warning(f"Zakładka '{tab_title}' nie zawiera sekcji do wyświetlenia.")
                    else:
                        st.warning("Nie znaleziono dostępnych pod-zakładek w sekcji ćwiczeń praktycznych.")
            
            # Przycisk "Dalej" po ćwiczeniach praktycznych
            st.markdown("<div class='next-button'>", unsafe_allow_html=True)
            if zen_button(f"Dalej: {step_names.get(next_step, next_step.capitalize())}", use_container_width=False):
                # Award fragment XP using the new system
                success, xp_awarded = award_fragment_xp(lesson_id, 'practical_exercises', step_xp_values['practical_exercises'])
                
                if success and xp_awarded > 0:
                    # Update session state for UI compatibility
                    st.session_state.lesson_progress['practical_exercises'] = True
                    st.session_state.lesson_progress['steps_completed'] += 1
                    st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                    
                    # Show real-time XP notification
                    show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za ukończenie ćwiczeń praktycznych!")
                    
                    # Refresh user data for real-time updates
                    from utils.real_time_updates import refresh_user_data
                    refresh_user_data()
                
                # Przejdź do następnego kroku
                st.session_state.lesson_step = next_step
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        elif st.session_state.lesson_step == 'reflection':
            # Wyświetl sekcje refleksji
            if 'sections' not in lesson:
                st.error("Lekcja nie zawiera klucza 'sections'!")
            elif 'reflection' not in lesson.get('sections', {}):
                st.error("Lekcja nie zawiera sekcji 'reflection'!")
            elif 'sections' not in lesson['sections'].get('reflection', {}):
                st.error("Sekcja 'reflection' nie zawiera klucza 'sections'!")
            else:
                # Wyświetl sekcje refleksji
                for section in lesson["sections"]["reflection"]["sections"]:
                    st.markdown(f"### {section.get('title', 'Zadanie refleksyjne')}")
                    st.markdown(section.get("content", "Brak treści"), unsafe_allow_html=True)
                    
                    # Generuj klucz dla przechowywania odpowiedzi
                    reflection_key = f"reflection_{section.get('title', '').replace(' ', '_').lower()}"
                    
                    # Generuj INNY klucz dla widgetu tekstowego
                    widget_key = f"input_{reflection_key}"
                    
                    # Użyj formularza, aby uniknąć problemów z aktualizacją stanu sesji
                    with st.form(key=f"form_{reflection_key}"):
                        # Pobierz istniejącą odpowiedź (jeśli jest)
                        existing_response = st.session_state.get(reflection_key, "")
                        
                        # Wyświetl pole tekstowe z istniejącą odpowiedzią
                        user_reflection = st.text_area(
                            "Twoja odpowiedź:",
                            value=existing_response,
                            height=200,
                            key=widget_key
                        )
                        
                        # Przycisk do zapisywania odpowiedzi w formularzu
                        submitted = st.form_submit_button("Zapisz odpowiedź")
                        
                        if submitted:
                            # Zapisz odpowiedź w stanie sesji
                            st.session_state[reflection_key] = user_reflection
                            st.success("Twoja odpowiedź została zapisana!")
              # Przycisk "Dalej" po refleksji
            st.markdown("<div class='next-button'>", unsafe_allow_html=True)
            if zen_button(f"Dalej: {step_names.get(next_step, next_step.capitalize())}", use_container_width=False):                
                # Award fragment XP using the new system
                success, xp_awarded = award_fragment_xp(lesson_id, 'reflection', step_xp_values['reflection'])
                
                if success and xp_awarded > 0:
                    # Update session state for UI compatibility
                    st.session_state.lesson_progress['reflection'] = True
                    st.session_state.lesson_progress['steps_completed'] += 1
                    st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                    
                    # Show real-time XP notification
                    show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za wykonanie zadań refleksyjnych!")
                    
                    # Refresh user data for real-time updates
                    from utils.real_time_updates import refresh_user_data
                    refresh_user_data()
                
                # Przejdź do następnego kroku
                st.session_state.lesson_step = next_step
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        elif st.session_state.lesson_step == 'application':
            # Wyświetl zadania praktyczne
            if 'sections' not in lesson:
                st.error("Lekcja nie zawiera klucza 'sections'!")
            elif 'application' not in lesson.get('sections', {}):
                st.error("Lekcja nie zawiera sekcji 'application'!")
            elif 'sections' not in lesson['sections'].get('application', {}):
                st.error("Sekcja 'application' nie zawiera klucza 'sections'!")
            else:
                # Wyświetl zadania praktyczne
                for section in lesson["sections"]["application"]["sections"]:
                    st.markdown(f"### {section.get('title', 'Zadanie praktyczne')}")
                    st.markdown(section.get("content", "Brak treści"), unsafe_allow_html=True)
                    
                    # Generuj klucz dla przechowywania odpowiedzi
                    task_key = f"application_{section.get('title', '').replace(' ', '_').lower()}"
                    
                    # Użyj formularza, aby uniknąć problemów z aktualizacją stanu sesji
                    with st.form(key=f"form_{task_key}"):
                        # Pobierz istniejącą odpowiedź (jeśli jest)
                        existing_solution = st.session_state.get(task_key, "")
                        
                        # Wyświetl pole tekstowe z istniejącą odpowiedzią
                        user_solution = st.text_area(
                            "Twoje rozwiązanie:",
                            value=existing_solution,
                            height=200,
                            key=f"input_{task_key}"
                        )
                        
                        # Przycisk do zapisywania odpowiedzi w formularzu
                        submitted = st.form_submit_button("Zapisz rozwiązanie")
                        
                        if submitted:
                            # Zapisz odpowiedź w stanie sesji
                            st.session_state[task_key] = user_solution
                            st.success("Twoje rozwiązanie została zapisana!")
                            # Dodaj odświeżenie strony po zapisaniu
                            st.rerun()
              # Przycisk "Dalej" po zadaniach praktycznych
            st.markdown("<div class='next-button'>", unsafe_allow_html=True)
            if zen_button(f"Dalej: {step_names.get(next_step, next_step.capitalize())}", use_container_width=False):
                # Award fragment XP using the new system
                success, xp_awarded = award_fragment_xp(lesson_id, 'application', step_xp_values['application'])
                
                if success and xp_awarded > 0:
                    # Update session state for UI compatibility
                    st.session_state.lesson_progress['application'] = True
                    st.session_state.lesson_progress['steps_completed'] += 1
                    st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                    
                    # Show real-time XP notification
                    show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za wykonanie zadań praktycznych!")
                    
                    # Refresh user data for real-time updates
                    from utils.real_time_updates import refresh_user_data
                    refresh_user_data()
                  # Przejdź do następnego kroku
                st.session_state.lesson_step = next_step
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        
        elif st.session_state.lesson_step == 'closing_quiz':
            # Wyświetl quiz końcowy
            if 'sections' not in lesson:
                st.error("Lekcja nie zawiera klucza 'sections'!")
            elif 'closing_quiz' not in lesson.get('sections', {}):
                st.error("Lekcja nie zawiera sekcji 'closing_quiz'!")
            else:
                # Użyj funkcji display_quiz do wyświetlenia quizu z wymaganiem 75%
                quiz_completed, quiz_passed, earned_points = display_quiz(lesson['sections']['closing_quiz'], passing_threshold=75)
                
                # Natychmiast oznacz quiz jako ukończony w nawigacji po ukończeniu
                if quiz_completed:
                    st.session_state.lesson_progress['closing_quiz'] = True
                    
                    # Sprawdź czy quiz został zdany z wymaganym wynikiem 75%
                    if quiz_passed:
                        # Przycisk "Dalej" po quizie końcowym - tylko jeśli zdany z 75%
                        st.markdown("<div class='next-button'>", unsafe_allow_html=True)
                        if zen_button(f"Dalej: {step_names.get(next_step, next_step.capitalize())}", use_container_width=False):
                            # Award fragment XP using the new system
                            success, xp_awarded = award_fragment_xp(lesson_id, 'closing_quiz', step_xp_values['closing_quiz'])
                            
                            if success and xp_awarded > 0:
                                # Update session state for UI compatibility
                                st.session_state.lesson_progress['steps_completed'] += 1
                                st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                                
                                # Show real-time XP notification
                                show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za ukończenie quizu końcowego!")
                                
                                # Refresh user data for real-time updates
                                from utils.real_time_updates import refresh_user_data
                                refresh_user_data()
                            
                            # Przejdź do następnego kroku
                            st.session_state.lesson_step = next_step
                            st.rerun()
                        st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        # Quiz ukończony ale nie zdany - wyświetl komunikat o konieczności uzyskania 75%
                        st.error("Aby przejść dalej, musisz uzyskać przynajmniej 75% poprawnych odpowiedzi w quizie końcowym. Spróbuj ponownie!")
                        
                        # Przycisk do powtórzenia quizu
                        st.markdown("<div class='next-button'>", unsafe_allow_html=True)
                        if zen_button("🔄 Spróbuj ponownie", use_container_width=False):                            # Resetuj stan quizu końcowego
                            quiz_session_key = f"quiz_{lesson['sections']['closing_quiz'].get('title', '').replace(' ', '_').lower()}"
                            if quiz_session_key in st.session_state:
                                del st.session_state[quiz_session_key]
                            st.rerun()
                        st.markdown("</div>", unsafe_allow_html=True)
        
        elif st.session_state.lesson_step == 'summary':
            # Wyświetl podsumowanie lekcji w podziale na zakładki, podobnie jak wprowadzenie
            if 'outro' in lesson:
                # Podziel podsumowanie na trzy zakładki - dodana mapa myśli
                summary_tabs = st.tabs(["Podsumowanie", "Case Study", "🗺️ Mapa myśli"])
                
                with summary_tabs[0]:
                    # Wyświetl główne podsumowanie
                    if 'main' in lesson['outro']:
                        st.markdown(lesson['outro']['main'], unsafe_allow_html=True)
                    else:
                        st.warning("Brak głównego podsumowania.")
                
                with summary_tabs[1]:
                    # Wyświetl studium przypadku
                    if 'case_study' in lesson['outro']:
                        st.markdown(lesson['outro']['case_study'], unsafe_allow_html=True)
                    else:
                        st.warning("Brak studium przypadku w podsumowaniu.")
                
                with summary_tabs[2]:
                    # Wyświetl interaktywną mapę myśli
                    st.markdown("### 🗺️ Interaktywna mapa myśli")
                    st.markdown("Poniżej znajdziesz interaktywną mapę myśli podsumowującą kluczowe koncepty z tej lekcji. Możesz klikać na węzły aby je przesuwać i lepiej eksplorować powiązania między różnymi tematami.")
                    
                    try:
                        from utils.mind_map import create_lesson_mind_map
                        mind_map_result = create_lesson_mind_map(lesson)
                        
                        if mind_map_result is None:
                            st.info("💡 **Mapa myśli w przygotowaniu**\n\nDla tej lekcji przygotowujemy interaktywną mapę myśli, która pomoże Ci lepiej zrozumieć powiązania między różnymi konceptami. Wkrótce będzie dostępna!")
                    except Exception as e:
                        st.warning("⚠️ Mapa myśli nie jest obecnie dostępna. Sprawdź, czy wszystkie wymagane biblioteki są zainstalowane.")
                        st.expander("Szczegóły błędu (dla deweloperów)").write(str(e))# Wyświetl całkowitą zdobytą ilość XP
                total_xp = st.session_state.lesson_progress['total_xp_earned']
                # st.success(f"Gratulacje! Ukończyłeś lekcję i zdobyłeś łącznie {total_xp} XP!")
                  # Sprawdź czy lekcja została już zakończona
                lesson_finished = st.session_state.get('lesson_finished', False)
                
                if not lesson_finished:
                    # Pierwszy etap - przycisk "Zakończ lekcję"
                    st.markdown("<div class='next-button'>", unsafe_allow_html=True)
                    if zen_button("🎉 Zakończ lekcję", use_container_width=False):
                        # Przyznaj XP za podsumowanie, jeśli jeszcze nie zostało przyznane
                        if not st.session_state.lesson_progress.get('summary', False):
                            success, xp_awarded = award_fragment_xp(lesson_id, 'summary', step_xp_values['summary'])
                            
                            if success and xp_awarded > 0:
                                # Update session state for UI compatibility
                                st.session_state.lesson_progress['summary'] = True
                                st.session_state.lesson_progress['steps_completed'] += 1
                                st.session_state.lesson_progress['total_xp_earned'] += xp_awarded
                                
                                # Show real-time XP notification
                                show_xp_notification(xp_awarded, f"Zdobyłeś {xp_awarded} XP za ukończenie podsumowania!")
                                
                                # Refresh user data for real-time updates
                                from utils.real_time_updates import refresh_user_data
                                refresh_user_data()
                          # Oznacz lekcję jako zakończoną i zapisz postęp
                        if is_lesson_fully_completed(lesson_id):
                            mark_lesson_as_completed(lesson_id)
                            
                            # Check for achievements after completing lesson
                            from utils.achievements import check_achievements
                            username = st.session_state.get('username')
                            if username:
                                check_achievements(username, 'lesson_completion', lesson_id=lesson_id)
                            
                            # Refresh user data for real-time updates
                            from utils.real_time_updates import refresh_user_data
                            refresh_user_data()
                            
                        # Show completion notification - wyświetl faktyczne całkowite XP
                        final_total_xp = st.session_state.lesson_progress.get('total_xp_earned', 0)
                        show_xp_notification(0, f"🎉 Gratulacje! Ukończyłeś całą lekcję i zdobyłeś {final_total_xp} XP!")
                        
                        # Oznacz lekcję jako zakończoną w sesji
                        st.session_state.lesson_finished = True
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    # Drugi etap - pokaż podsumowanie i przycisk powrotu
                    st.balloons()  # Animacja gratulacji
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                                color: white; padding: 20px; border-radius: 15px; margin: 20px 0;
                                text-align: center; box-shadow: 0 4px 15px rgba(76,175,80,0.3);">
                        <h2 style="margin: 0 0 10px 0;">🎓 Lekcja ukończona!</h2>
                        <p style="margin: 0; font-size: 18px;">Świetna robota! Możesz teraz przejść do kolejnych lekcji.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Przycisk powrotu do wszystkich lekcji
                    st.markdown("<div class='next-button'>", unsafe_allow_html=True)
                    if zen_button("📚 Wróć do wszystkich lekcji", use_container_width=False):
                        # Wyczyść stan zakończenia lekcji
                        st.session_state.lesson_finished = False
                        # Powrót do przeglądu lekcji
                        st.session_state.current_lesson = None
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)
            elif 'summary' in lesson:
                # Obsługa starszego formatu, gdzie podsumowanie było bezpośrednio w lesson['summary']
                st.markdown(lesson['summary'], unsafe_allow_html=True)
            else:
                # Brak podsumowania w danych lekcji
                st.error("Lekcja nie zawiera podsumowania!")
          # Zamknij div .st-bx
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Add live XP indicator
        live_xp_indicator()        # Show lesson progress with current XP system
        # Pobierz aktualne dane fragmentów
        fragment_progress = get_lesson_fragment_progress(lesson_id)
          # Synchronizuj stan sesji z rzeczywistymi danymi fragmentów
        for step in step_order:
            completed_key = f"{step}_completed"
            if completed_key in fragment_progress:
                st.session_state.lesson_progress[step] = fragment_progress[completed_key]
        
        # Oblicz zdobyte XP na podstawie rzeczywistych danych z systemu fragmentów
        current_xp = 0
        for step in step_order:
            step_xp_key = f"{step}_xp"
            if step_xp_key in fragment_progress:
                current_xp += fragment_progress[step_xp_key]
          # Oblicz aktualny postęp na podstawie XP (nie liczby kroków)
        completion_percent = (current_xp / max_xp) * 100 if max_xp > 0 else 0
        
        # Przygotuj dane o kluczowych krokach do wyświetlenia
        key_steps_info = []
        if 'intro' in step_order:
            completed = st.session_state.lesson_progress.get('intro', False)
            key_steps_info.append(f"📖 Intro: {step_xp_values['intro']} XP {'✅' if completed else ''}")
        
        if 'opening_quiz' in step_order:
            completed = st.session_state.lesson_progress.get('opening_quiz', False)
            key_steps_info.append(f"🪞 Samorefleksja: {step_xp_values['opening_quiz']} XP {'✅' if completed else ''}")
        
        if 'content' in step_order:
            completed = st.session_state.lesson_progress.get('content', False)
            key_steps_info.append(f"📚 Treść: {step_xp_values['content']} XP {'✅' if completed else ''}")
        
        if 'practical_exercises' in step_order:
            completed = st.session_state.lesson_progress.get('practical_exercises', False)
            key_steps_info.append(f"🎯 Ćwiczenia praktyczne: {step_xp_values['practical_exercises']} XP {'✅' if completed else ''}")
        
        if 'reflection' in step_order:
            completed = st.session_state.lesson_progress.get('reflection', False)
            key_steps_info.append(f"🤔 Refleksja: {step_xp_values['reflection']} XP {'✅' if completed else ''}")
        
        if 'application' in step_order:
            completed = st.session_state.lesson_progress.get('application', False)
            key_steps_info.append(f"💪 Zadania: {step_xp_values['application']} XP {'✅' if completed else ''}")
        if 'closing_quiz' in step_order:
            completed = st.session_state.lesson_progress.get('closing_quiz', False)
            key_steps_info.append(f"🧠 Quiz: {step_xp_values['closing_quiz']} XP {'✅' if completed else ''}")
        
        if 'summary' in step_order:
            completed = st.session_state.lesson_progress.get('summary', False)
            key_steps_info.append(f"📋 Podsumowanie: {step_xp_values['summary']} XP {'✅' if completed else ''}")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; padding: 20px; margin-bottom: 20px; color: white;">
            <h3 style="margin: 0 0 10px 0;">📚 {lesson.get('title', 'Lekcja')}</h3>
            <div style="background: rgba(255,255,255,0.2); border-radius: 10px; padding: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <span style="font-weight: bold;">Postęp lekcji: {completion_percent:.0f}%</span>
                    <span>💎 {current_xp}/{max_xp} XP</span>
                </div>
                <div style="background: rgba(255,255,255,0.3); border-radius: 5px; height: 12px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #4caf50, #2196f3); 
                                width: {completion_percent}%; height: 100%; transition: width 0.3s ease;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 8px; font-size: 12px; flex-wrap: wrap; gap: 5px;">
                    {' '.join([f'<span>{info}</span>' for info in key_steps_info[:3]])}
                </div>
                {f'<div style="display: flex; justify-content: space-between; margin-top: 5px; font-size: 12px; flex-wrap: wrap; gap: 5px;">{" ".join([f"<span>{info}</span>" for info in key_steps_info[3:]])}</div>' if len(key_steps_info) > 3 else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)


def display_lesson(lesson_data):
    """Wyświetla lekcję z nowymi sekcjami quizów"""
    
    # Wyświetl tytuł lekcji
    st.markdown(f"<h1>{lesson_data['title']}</h1>", unsafe_allow_html=True)
    
    # Wyświetl wprowadzenie
    if 'intro' in lesson_data:
        st.markdown(lesson_data['intro'], unsafe_allow_html=True)
    
    # Przygotuj dane zakładek
    tab_data = []
      # Dodaj zakładki w odpowiedniej kolejności
    if 'opening_quiz' in lesson_data.get('sections', {}):
        tab_data.append(("Samorefleksja", "opening_quiz"))
    
    if 'learning' in lesson_data.get('sections', {}):
        tab_data.append(("Nauka", "learning"))
    
    if 'reflection' in lesson_data.get('sections', {}):
        tab_data.append(("Refleksja", "reflection"))
    
    if 'closing_quiz' in lesson_data.get('sections', {}):
        tab_data.append(("Quiz końcowy", "closing_quiz"))
    
    # Wyodrębnij tytuły zakładek
    tab_titles = [title for title, _ in tab_data]
    
    # Wyświetl zakładki tylko jeśli są jakieś dane do wyświetlenia
    if tab_titles:
        tabs = st.tabs(tab_titles)
          # Dla każdej zakładki wyświetl odpowiednią zawartość
        for i, (_, tab_name) in enumerate(tab_data):
            with tabs[i]:
                if tab_name in ["opening_quiz", "closing_quiz"]:
                    display_quiz(lesson_data['sections'][tab_name])
                elif tab_name == "learning":
                    display_learning_sections(lesson_data['sections'][tab_name])
                elif tab_name == "reflection":
                    display_reflection_sections(lesson_data['sections'][tab_name])
    else:
        st.warning("Ta lekcja nie zawiera żadnych sekcji do wyświetlenia.")


# Dodanie brakujących funkcji
def display_learning_sections(learning_data):
    """Wyświetla sekcje nauki z lekcji"""
    if not learning_data or 'sections' not in learning_data:
        st.warning("Brak treści edukacyjnych w tej lekcji.")
        return
        
    for section in learning_data['sections']:
        content_section(
            section.get("title", "Tytuł sekcji"), 
            section.get("content", "Brak treści"), 
            collapsed=False
        )


def display_reflection_sections(reflection_data):
    """Wyświetla sekcje refleksji z lekcji"""
    if not reflection_data:
        st.warning("Brak zadań refleksyjnych w tej lekcji.")
        return
        
    # Check if there are sections in the data
    if 'sections' not in reflection_data:
        st.warning("Dane refleksji nie zawierają sekcji.")
        return
        
    for section in reflection_data['sections']:
        st.markdown(f"### {section.get('title', 'Zadanie refleksyjne')}")
        st.markdown(section.get("content", "Brak treści"), unsafe_allow_html=True)
        
        # Dodaj pole tekstowe do wprowadzania odpowiedzi
        reflection_key = f"reflection_{section.get('title', '').replace(' ', '_').lower()}"
        user_reflection = st.text_area(
            "Twoja odpowiedź:",
            value=st.session_state.get(reflection_key, ""),
            height=200,
            key=reflection_key
        )
        
        # Dodaj przycisk do zapisywania odpowiedzi
        if st.button("Zapisz odpowiedź", key=f"save_{reflection_key}"):
            st.session_state[reflection_key] = user_reflection
            st.success("Twoja odpowiedź została zapisana!")

def display_quiz(quiz_data, passing_threshold=60):
    """Wyświetla quiz z pytaniami i opcjami odpowiedzi. Zwraca True, gdy quiz jest ukończony."""
    
    # Style CSS TYLKO dla przycisków odpowiedzi quiz - nie wpływa na nawigację
    st.markdown("""
    <style>
    .quiz-question {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 20px;+
        border-radius: 15px;
        margin: 20px 0;
        border-left: 5px solid #4caf50;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .quiz-question h3 {
        color: #2e7d32;
        margin: 0;
        font-size: 1.2em;
    }
    
    /* Kontener dla przycisków odpowiedzi quiz */
    .quiz-answers-section {
        margin: 20px 0;
    }
    
    /* Style TYLKO dla przycisków w kontenerze quiz-answers-section */
    .quiz-answers-section .stButton > button {
        background-color: #f8f9fa !important;
        background-image: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
        border: 2px solid #dee2e6 !important;
        color: #495057 !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        min-height: 48px !important;
        width: auto !important;
        min-width: fit-content !important;
        max-width: fit-content !important;
        white-space: nowrap !important;
    }
    
    .quiz-answers-section .stButton > button:hover {
        background-color: #e9ecef !important;
        background-image: linear-gradient(135deg, #e9ecef 0%, #d1ecf1 100%) !important;
        border-color: #adb5bd !important;
        color: #343a40 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
    }
    
    .quiz-answers-section .stButton > button:active {
        transform: translateY(0px) scale(0.98) !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
    }
    
    /* Dodatkowe selektory dla różnych wersji Streamlit - TYLKO w quiz-answers-section */
    .quiz-answers-section div[data-testid="stButton"] button {
        background-color: #f8f9fa !important;
        background-image: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
        border: 2px solid #dee2e6 !important;
        color: #495057 !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        min-height: 48px !important;
        width: auto !important;
        min-width: fit-content !important;
        max-width: fit-content !important;
        white-space: nowrap !important;
    }
    
    .quiz-answers-section div[data-testid="stButton"] button:hover {
        background-color: #e9ecef !important;
        background-image: linear-gradient(135deg, #e9ecef 0%, #d1ecf1 100%) !important;
        border-color: #adb5bd !important;
        color: #343a40 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
    }
    
    /* Kontrola szerokości kolumn z przyciskami quiz */
    .quiz-answers-section .css-1r6slb0, 
    .quiz-answers-section .css-12oz5g7 {
        max-width: fit-content !important;
        width: auto !important;
        flex: 0 0 auto !important;
    }    </style>
    """, unsafe_allow_html=True)
    
    if not quiz_data or "questions" not in quiz_data:
        st.warning("Ten quiz nie zawiera żadnych pytań.")
        return False, False, 0
        
    st.markdown(f"<h2>{quiz_data.get('title', 'Quiz')}</h2>", unsafe_allow_html=True)
    
    if "description" in quiz_data:
        st.markdown(quiz_data['description'])
      # Sprawdź czy to quiz samodiagnozy (wszystkie correct_answer są null)
    is_self_diagnostic = all(q.get('correct_answer') is None for q in quiz_data['questions'])
    
    # Style CSS z różnymi szerokościami dla różnych typów quizów
    st.markdown(f"""
    <style>
    .quiz-question {{
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        border-left: 5px solid #4caf50;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }}
    
    .quiz-question h3 {{
        color: #2e7d32;
        margin: 0;
        font-size: 1.2em;
    }}
    
    /* Kontener dla przycisków odpowiedzi quiz */
    .quiz-answers-section {{
        margin: 20px 0;
    }}
    
    /* Style dla quizów testowych - przyciski pełnej szerokości */
    .quiz-answers-section.test-quiz .stButton > button {{
        background-color: #f8f9fa !important;
        background-image: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
        border: 2px solid #dee2e6 !important;
        color: #495057 !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        min-height: 48px !important;
        width: 100% !important;
        max-width: 100% !important;
        white-space: normal !important;
        text-align: left !important;
    }}
    
    /* Style dla quizów autorefleksji - przyciski dopasowane do treści */
    .quiz-answers-section.self-reflection-quiz .stButton > button {{
        background-color: #f8f9fa !important;
        background-image: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
        border: 2px solid #dee2e6 !important;
        color: #495057 !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        min-height: 48px !important;
        width: auto !important;
        min-width: fit-content !important;
        max-width: fit-content !important;
        white-space: nowrap !important;
    }}
    
    /* Hover efekty dla obu typów */
    .quiz-answers-section .stButton > button:hover {{
        background-color: #e9ecef !important;
        background-image: linear-gradient(135deg, #e9ecef 0%, #d1ecf1 100%) !important;
        border-color: #adb5bd !important;
        color: #343a40 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
    }}
    
    .quiz-answers-section .stButton > button:active {{
        transform: translateY(0px) scale(0.98) !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
    }}
    
    /* Dodatkowe selektory dla różnych wersji Streamlit */
    .quiz-answers-section.test-quiz div[data-testid="stButton"] button {{
        width: 100% !important;
        max-width: 100% !important;
        white-space: normal !important;
        text-align: left !important;
    }}
    
    .quiz-answers-section.self-reflection-quiz div[data-testid="stButton"] button {{
        width: auto !important;
        min-width: fit-content !important;
        max-width: fit-content !important;
        white-space: nowrap !important;
    }}
    
    /* Kontrola szerokości kolumn dla quizów autorefleksji */
    .quiz-answers-section.self-reflection-quiz .css-1r6slb0, 
    .quiz-answers-section.self-reflection-quiz .css-12oz5g7 {{
        max-width: fit-content !important;
        width: auto !important;
        flex: 0 0 auto !important;
    }}
    </style>
    """, unsafe_allow_html=True)
    quiz_id = f"quiz_{quiz_data.get('title', '').replace(' ', '_').lower()}"
    if quiz_id not in st.session_state:
        st.session_state[quiz_id] = {
            "answered_questions": [],
            "correct_answers": 0,
            "total_questions": len(quiz_data['questions']),
            "completed": False,
            "total_points": 0  # Dla quizów samodiagnozy
        }
    
    # Backward compatibility: ensure total_points exists for existing sessions
    if "total_points" not in st.session_state[quiz_id]:
        st.session_state[quiz_id]["total_points"] = 0
    
    # Wyświetl wszystkie pytania
    for i, question in enumerate(quiz_data['questions']):
        question_id = f"{quiz_id}_q{i}"
        
        # Kontener dla pytania z własnymi stylami
        st.markdown(f"""
        <div class="quiz-question">
            <h3>Pytanie {i+1}: {question['question']}</h3>
        </div>
        """, unsafe_allow_html=True)          # Jeśli pytanie już zostało odpowiedziane, pokaż wynik
        if i in st.session_state[quiz_id]["answered_questions"]:
            selected = st.session_state.get(f"{question_id}_selected")
            question_type = question.get('type', 'single_choice')
            
            # Wyświetl odpowiedzi z oznaczeniem poprawnej
            for j, option in enumerate(question['options']):
                # Dla quizów samodiagnozy - wszystkie opcje równe
                if is_self_diagnostic:
                    if isinstance(selected, list):
                        # Wielokrotny wybór w samodiagnozie (rzadko używane)
                        if j in selected:
                            st.markdown(f"✓ **{option}** _(Twoja odpowiedź)_")
                        else:
                            st.markdown(f"○ {option}")
                    else:
                        # Pojedynczy wybór w samodiagnozie
                        if j == selected:
                            st.markdown(f"✓ **{option}** _(Twoja odpowiedź)_")
                        else:
                            st.markdown(f"○ {option}")
                else:
                    # Dla quizów z poprawnymi odpowiedziami
                    if question_type == 'multiple_choice':
                        # Pytania z wielokrotnym wyborem
                        correct_answers = question.get('correct_answers', [])
                        selected_list = selected if isinstance(selected, list) else []
                        
                        if j in correct_answers and j in selected_list:
                            st.markdown(f"✅ **{option}** _(Poprawna odpowiedź - wybrana)_")
                        elif j in correct_answers and j not in selected_list:
                            st.markdown(f"✅ **{option}** _(Poprawna odpowiedź - nie wybrana)_")
                        elif j not in correct_answers and j in selected_list:
                            st.markdown(f"❌ **{option}** _(Niepoprawna odpowiedź - wybrana)_")
                        else:
                            st.markdown(f"○ {option}")
                    else:
                        # Pytania z pojedynczym wyborem
                        correct_answer = question.get('correct_answer')
                        is_correct = correct_answer is not None and selected == correct_answer
                        
                        if correct_answer is not None:
                            if j == correct_answer:
                                st.markdown(f"✅ **{option}** _(Poprawna odpowiedź)_")
                            elif j == selected and not is_correct:
                                st.markdown(f"❌ **{option}** _(Twoja odpowiedź)_")
                            else:
                                st.markdown(f"○ {option}")
                        else:
                            st.markdown(f"○ {option}")
              # Wyświetl wyjaśnienie
            if "explanation" in question:
                st.info(question['explanation'])
            
            st.markdown("---")
        else:
            # Określ typ quizu i użyj odpowiedniej klasy CSS
            quiz_type_class = "self-reflection-quiz" if is_self_diagnostic else "test-quiz"
            
            # Rozpocznij sekcję przycisków odpowiedzi quiz z odpowiednią klasą
            st.markdown(f'<div class="quiz-answers-section {quiz_type_class}">', unsafe_allow_html=True)
            
            if is_self_diagnostic:
                # Quiz autorefleksji - przyciski krótkie, dopasowane do treści
                for j, option in enumerate(question['options']):
                    # Każdy przycisk w osobnej kolumnie o minimalnej szerokości
                    col1, col2 = st.columns([1, 3])  # Pierwsza kolumna mała, druga większa ale niewykorzystana
                    
                    with col1:
                        if st.button(option, key=f"{question_id}_opt{j}"):
                            # Zapisz wybraną odpowiedź
                            st.session_state[f"{question_id}_selected"] = j
                            st.session_state[quiz_id]["answered_questions"].append(i)
                            # Dla quizów samodiagnozy - zlicz punkty (opcje 1-5 = j+1 punktów)
                            points = j + 1
                            if "total_points" not in st.session_state[quiz_id]:
                                st.session_state[quiz_id]["total_points"] = 0
                            st.session_state[quiz_id]["total_points"] += points
                            if len(st.session_state[quiz_id]["answered_questions"]) == st.session_state[quiz_id]["total_questions"]:
                                st.session_state[quiz_id]["completed"] = True
                                if 'opening_quiz' in quiz_id.lower() or 'startowy' in quiz_id.lower():
                                    st.session_state.lesson_progress['opening_quiz'] = True
                            st.rerun()
                            return False, False, 0
            else:
                # Quiz testowy - przyciski pełnej szerokości
                question_type = question.get('type', 'single_choice')
                if question_type == 'multiple_choice':
                    # Pytanie z wielokrotnym wyborem
                    st.write("**Wybierz wszystkie poprawne odpowiedzi:**")
                    
                    # Zbierz aktualny stan checkboxów
                    for j, option in enumerate(question['options']):
                        checkbox_key = f"{question_id}_opt{j}"
                        st.checkbox(option, key=checkbox_key)
                    
                    # Przycisk do zatwierdzenia odpowiedzi z unikatowym kluczem
                    submit_key = f"{question_id}_submit"
                      # Przycisk do zatwierdzenia odpowiedzi
                    if st.button("Zatwierdź odpowiedzi", key=submit_key):
                        selected_options = []
                        for j, option in enumerate(question['options']):
                            checkbox_key = f"{question_id}_opt{j}"
                            if st.session_state.get(checkbox_key, False):
                                selected_options.append(j)
                        if selected_options:
                            st.session_state[f"{question_id}_selected"] = selected_options
                            st.session_state[quiz_id]["answered_questions"].append(i)
                            correct_answers = question.get('correct_answers', [])
                            if set(selected_options) == set(correct_answers):
                                st.session_state[quiz_id]["correct_answers"] += 1
                                if "quiz_score" in st.session_state:
                                    st.session_state.quiz_score += 5
                            if len(st.session_state[quiz_id]["answered_questions"]) == st.session_state[quiz_id]["total_questions"]:
                                st.session_state[quiz_id]["completed"] = True
                                if 'closing_quiz' in quiz_id.lower() or 'końcowy' in quiz_id.lower():
                                    st.session_state.lesson_progress['closing_quiz'] = True
                            st.rerun()
                            return False, False, 0
                    else:
                        st.warning("Wybierz przynajmniej jedną odpowiedź przed zatwierdzeniem.")
                else:
                    # Pytanie z pojedynczym wyborem (domyślne)
                    for j, option in enumerate(question['options']):
                        if st.button(option, key=f"{question_id}_opt{j}"):
                            st.session_state[f"{question_id}_selected"] = j
                            st.session_state[quiz_id]["answered_questions"].append(i)
                            correct_answer = question.get('correct_answer')
                            if correct_answer is not None and j == correct_answer:
                                st.session_state[quiz_id]["correct_answers"] += 1
                                if "quiz_score" in st.session_state:
                                    st.session_state.quiz_score += 5
                            if len(st.session_state[quiz_id]["answered_questions"]) == st.session_state[quiz_id]["total_questions"]:
                                st.session_state[quiz_id]["completed"] = True
                                if 'closing_quiz' in quiz_id.lower() or 'końcowy' in quiz_id.lower():
                                    st.session_state.lesson_progress['closing_quiz'] = True
                            st.rerun()
                            return False, False, 0
        st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown("---")
    
    # Sprawdź czy quiz jest ukończony i oblicz punkty
    is_completed = st.session_state[quiz_id].get("completed", False)
    
    if is_completed:
        if is_self_diagnostic:
            # Quiz samodiagnozy - wyświetl punkty i interpretację
            total_points = st.session_state[quiz_id].get("total_points", 0)
            
            # Oblicz maksymalne możliwe punkty (liczba pytań × 5)
            max_possible_points = len(quiz_data['questions']) * 5;
            
            st.markdown(f"""
            <div class="quiz-summary">
                <h3>📊 Twój wynik: {total_points}/{max_possible_points} punktów</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Wyświetl interpretację wyników jeśli dostępna
            if 'scoring' in quiz_data and 'interpretation' in quiz_data['scoring']:
                interpretation_found = False
                for score_range, interpretation in quiz_data['scoring']['interpretation'].items():
                    # Parsuj zakres punktów (np. "10-20", "21-35", "36-50")
                    if '-' in score_range:
                        min_score, max_score = map(int, score_range.split('-'))
                        if min_score <= total_points <= max_score:
                            st.success(f"🧮 **Interpretacja wyników:**\n\n{interpretation}")
                            interpretation_found = True
                            break
                
                if not interpretation_found:
                    st.info("🪞 Dziękujemy za szczerą samorefleksję! Twoje odpowiedzi pomogą nam lepiej dopasować materiał do Twojego stylu inwestowania.")
            else:
                st.info("🪞 Dziękujemy za szczerą samorefleksję! Twoje odpowiedzi pomogą nam lepiej dopasować materiał do Twojego stylu inwestowania.")
              # Zawsze "zdany" dla quizu samodiagnozy
            return is_completed, True, total_points
            
        else:            # Standardowy quiz z poprawnymi odpowiedziami
            correct = st.session_state[quiz_id]["correct_answers"]
            total = st.session_state[quiz_id]["total_questions"]
            percentage = (correct / total) * 100
            
            # Oblicz punkty - wartość zależy od procentu odpowiedzi poprawnych
            quiz_xp_value = 15
            earned_points = int(quiz_xp_value * (percentage / 100))
            
            # Czy quiz został zdany (na podstawie passing_threshold)
            is_passed = percentage >= passing_threshold
            
            st.markdown(f"""
            <div class="quiz-summary">
                <h3>Twój wynik: {correct}/{total} ({percentage:.0f}%)</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Wyświetl interpretację wyników jeśli dostępna (nowy system)
            if 'result_interpretation' in quiz_data:
                interpretation_found = False
                interpretations = quiz_data['result_interpretation']
                
                # Sprawdź każdy próg interpretacji od najwyższego do najniższego
                for key in ['excellent', 'good', 'needs_improvement', 'poor']:
                    if key in interpretations:
                        threshold = interpretations[key].get('threshold', 0)
                        if percentage >= threshold:
                            title = interpretations[key].get('title', 'Wynik')
                            message = interpretations[key].get('message', 'Brak opisu')
                            st.success(f"**{title}**\n\n{message}")
                            interpretation_found = True
                            break
                
                if not interpretation_found:
                    # Fallback do standardowych komunikatów
                    if percentage >= 80:
                        st.success("Świetnie! Doskonale rozumiesz ten temat.")
                    elif percentage >= passing_threshold:
                        if passing_threshold > 60:
                            st.success(f"Bardzo dobrze! Osiągnąłeś wymagany próg {passing_threshold}% i możesz kontynuować.")
                        else:
                            st.success("Bardzo dobrze! Możesz kontynuować naukę.")
                    else:
                        if passing_threshold > 60:
                            st.error(f"Aby przejść dalej, musisz uzyskać przynajmniej {passing_threshold}% poprawnych odpowiedzi. Spróbuj ponownie!")
                        else:
                            st.warning("Spróbuj jeszcze raz - możesz to zrobić lepiej!")
            else:
                # Standardowe komunikaty jeśli brak interpretacji
                if percentage >= 80:
                    st.success("Świetnie! Doskonale rozumiesz ten temat.")
                elif percentage >= passing_threshold:
                    if passing_threshold > 60:
                        st.success(f"Bardzo dobrze! Osiągnąłeś wymagany próg {passing_threshold}% i możesz kontynuować.")
                    else:
                        st.success("Bardzo dobrze! Możesz kontynuować naukę.")
                else:
                    if passing_threshold > 60:
                        st.error(f"Aby przejść dalej, musisz uzyskać przynajmniej {passing_threshold}% poprawnych odpowiedzi. Spróbuj ponownie!")
                    else:                        st.warning("Spróbuj jeszcze raz - możesz to zrobić lepiej!")
            
            return is_completed, is_passed, earned_points    # Quiz nie jest jeszcze ukończony
    return is_completed, False, 0
