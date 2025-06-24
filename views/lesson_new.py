import streamlit as st
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
from views.skills_new import show_skill_tree


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
        try:
            difficulty_level = int(difficulty)
        except (ValueError, TypeError):
            difficulty_level = 1
    
    return '⭐' * difficulty_level


def show_lesson():
    """Show lesson view with tabs for lessons and course structure"""
    
    # Zastosuj style Material 3
    apply_material3_theme()
    
    # Opcja wyboru urządzenia w trybie deweloperskim
    if st.session_state.get('dev_mode', False):
        toggle_device_view()
    
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
    zen_header("Kurs Zen Degen Academy")
    
    # Create main tabs
    tab1, tab2 = st.tabs(["📚 Dostępne Lekcje", "🌳 Struktura Kursu"])
    
    with tab1:
        show_lessons_content()
    
    with tab2:
        show_skill_tree()


def show_lessons_content():
    """Show the lessons content (original show_lesson content)"""
    # Pobierz aktualny typ urządzenia
    device_type = get_device_type()
    
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
                            st.rerun()
                        )
                    )
    
    else:
        # Kod wyświetlania pojedynczej lekcji z nową strukturą 4 zakładek
        lesson_id = st.session_state.current_lesson
        if lesson_id not in lessons:
            st.error("Nie znaleziono wybranej lekcji.")
            return
            
        lesson = lessons[lesson_id]
        
        # Wyświetl nagłówek lekcji
        st.markdown(f"<h1>📚 {lesson.get('title', 'Lekcja')}</h1>", unsafe_allow_html=True)
        
        # Utwórz 4 główne zakładki zgodnie z nowym schematem
        tab1, tab2, tab3, tab4 = st.tabs([
            "🚀 Wprowadzenie", 
            "📖 Materiał", 
            "🎯 Zadania praktyczne", 
            "📋 Podsumowanie"
        ])
        
        # ZAKŁADKA 1: WPROWADZENIE (z pod-zakładkami)
        with tab1:
            show_introduction_tab(lesson, lesson_id)
        
        # ZAKŁADKA 2: MATERIAŁ (bez zmian)
        with tab2:
            show_material_tab(lesson, lesson_id)
        
        # ZAKŁADKA 3: ZADANIA PRAKTYCZNE (z pod-zakładkami)
        with tab3:
            show_practical_tasks_tab(lesson, lesson_id)
        
        # ZAKŁADKA 4: PODSUMOWANIE (z pod-zakładkami)
        with tab4:
            show_summary_tab(lesson, lesson_id)


def show_introduction_tab(lesson, lesson_id):
    """Wyświetla zakładkę Wprowadzenie z pod-zakładkami"""
    intro_sub_tabs = st.tabs(["📖 Wprowadzenie", "📚 Case Study", "🪞 Samorefleksja"])
    
    with intro_sub_tabs[0]:
        # Wyświetl główne wprowadzenie
        if isinstance(lesson.get("intro"), dict) and "main" in lesson["intro"]:
            st.markdown(lesson["intro"]["main"], unsafe_allow_html=True)
        elif isinstance(lesson.get("intro"), str):
            st.markdown(lesson["intro"], unsafe_allow_html=True)
        else:
            st.warning("Brak treści wprowadzenia.")
    
    with intro_sub_tabs[1]:
        # Wyświetl studium przypadku
        if isinstance(lesson.get("intro"), dict) and "case_study" in lesson["intro"]:
            st.markdown(lesson["intro"]["case_study"], unsafe_allow_html=True)
        else:
            st.warning("Brak studium przypadku w tej lekcji.")
    
    with intro_sub_tabs[2]:
        # Wyświetl quiz startowy (samorefleksja)
        if 'sections' in lesson and 'opening_quiz' in lesson.get('sections', {}):
            st.info("🪞 **Narzędzie Samorefleksji** - Ten quiz pomaga Ci lepiej poznać siebie jako inwestora. Nie ma tu dobrych ani złych odpowiedzi - chodzi o szczerą autorefleksję.")
            
            quiz_data = lesson['sections']['opening_quiz']
            quiz_complete, _, earned_points = display_quiz(quiz_data)
        else:
            st.info("Dla tej lekcji nie przewidziano kwestionariusza samorefleksji.")


def show_material_tab(lesson, lesson_id):
    """Wyświetla zakładkę Materiał - główna treść lekcji"""
    if 'sections' not in lesson:
        st.error("Lekcja nie zawiera klucza 'sections'!")
    elif 'learning' not in lesson.get('sections', {}):
        st.error("Lekcja nie zawiera sekcji 'learning'!")
    elif 'sections' not in lesson['sections'].get('learning', {}):
        st.error("Sekcja 'learning' nie zawiera klucza 'sections'!")
    else:
        # Wyświetl sekcje materiału lekcji
        for i, section in enumerate(lesson["sections"]["learning"]["sections"]):
            with st.expander(section.get("title", f"Sekcja {i+1}"), expanded=False):
                st.markdown(section.get("content", "Brak treści"), unsafe_allow_html=True)


def show_practical_tasks_tab(lesson, lesson_id):
    """Wyświetla zakładkę Zadania praktyczne z pod-zakładkami"""
    practical_sub_tabs = st.tabs(["🎯 Ćwiczenia+autorefleksja", "🧠 Quiz końcowy"])
    
    with practical_sub_tabs[0]:
        # Wyświetl ćwiczenia praktyczne i refleksje
        show_exercises_and_reflection(lesson, lesson_id)
    
    with practical_sub_tabs[1]:
        # Wyświetl quiz końcowy
        if 'sections' in lesson and 'closing_quiz' in lesson.get('sections', {}):
            st.info("🧠 **Quiz końcowy** - Sprawdź swoją wiedzę z tej lekcji. Aby przejść dalej, musisz uzyskać co najmniej 75% poprawnych odpowiedzi.")
            
            quiz_data = lesson['sections']['closing_quiz']
            quiz_completed, quiz_passed, earned_points = display_quiz(quiz_data, passing_threshold=75)
            
            if quiz_completed and not quiz_passed:
                st.error("Aby przejść dalej, musisz uzyskać przynajmniej 75% poprawnych odpowiedzi w quizie końcowym. Spróbuj ponownie!")
                
                if st.button("🔄 Spróbuj ponownie", key="retry_quiz"):
                    # Resetuj stan quizu końcowego
                    quiz_session_key = f"quiz_{quiz_data.get('title', '').replace(' ', '_').lower()}"
                    if quiz_session_key in st.session_state:
                        del st.session_state[quiz_session_key]
                    st.rerun()
        else:
            st.info("Ta lekcja nie zawiera quizu końcowego.")


def show_exercises_and_reflection(lesson, lesson_id):
    """Wyświetla ćwiczenia praktyczne i zadania refleksyjne"""
    
    # Sprawdź czy są nowe ćwiczenia praktyczne
    if 'sections' in lesson and 'practical_exercises' in lesson.get('sections', {}):
        practical_data = lesson['sections']['practical_exercises']
        
        if 'tabs' in practical_data:
            # Nowy format z pod-zakładkami
            sub_tabs_data = practical_data['tabs']
            available_tabs = []
            tab_keys = []
            
            # Sprawdź które zakładki są dostępne
            if 'autotest' in sub_tabs_data:
                available_tabs.append("🧠 Autotest")
                tab_keys.append('autotest')
            
            if 'reflection' in sub_tabs_data:
                available_tabs.append("📝 Refleksja")
                tab_keys.append('reflection')
            
            if 'analysis' in sub_tabs_data:
                available_tabs.append("📊 Analiza")
                tab_keys.append('analysis')
            
            if 'implementation' in sub_tabs_data:
                available_tabs.append("🎯 Wdrożenie")
                tab_keys.append('implementation')
            
            if available_tabs:
                exercise_tabs = st.tabs(available_tabs)
                
                for i, (tab_key, tab_title) in enumerate(zip(tab_keys, available_tabs)):
                    with exercise_tabs[i]:
                        tab_data = sub_tabs_data[tab_key]
                        
                        if 'description' in tab_data:
                            st.info(tab_data['description'])
                        
                        if 'sections' in tab_data:
                            for section in tab_data['sections']:
                                st.markdown(f"### {section.get('title', 'Sekcja')}")
                                st.markdown(section.get('content', 'Brak treści'), unsafe_allow_html=True)
                                
                                if section.get('interactive', False):
                                    section_key = f"practical_{tab_key}_{section.get('title', '').replace(' ', '_').lower()}"
                                    
                                    with st.form(key=f"form_{section_key}"):
                                        existing_response = st.session_state.get(section_key, "")
                                        user_response = st.text_area(
                                            "Twoja odpowiedź:",
                                            value=existing_response,
                                            height=200,
                                            key=f"input_{section_key}"
                                        )
                                        
                                        submitted = st.form_submit_button("Zapisz odpowiedź")
                                        
                                        if submitted:
                                            st.session_state[section_key] = user_response
                                            st.success("Twoja odpowiedź została zapisana!")
            else:
                st.warning("Nie znaleziono dostępnych ćwiczeń praktycznych.")
        else:
            st.warning("Ćwiczenia praktyczne nie są jeszcze dostępne w tej lekcji.")
    
    # Sprawdź czy są starsze sekcje refleksji i zadań praktycznych (backward compatibility)
    elif 'sections' in lesson:
        has_reflection = 'reflection' in lesson.get('sections', {})
        has_application = 'application' in lesson.get('sections', {})
        
        if has_reflection or has_application:
            if has_reflection and has_application:
                legacy_tabs = st.tabs(["🤔 Refleksja", "💪 Zadania praktyczne"])
                
                with legacy_tabs[0]:
                    show_legacy_reflection_section(lesson)
                
                with legacy_tabs[1]:
                    show_legacy_application_section(lesson)
            
            elif has_reflection:
                show_legacy_reflection_section(lesson)
            
            elif has_application:
                show_legacy_application_section(lesson)
        else:
            st.info("Ta lekcja nie zawiera ćwiczeń praktycznych.")
    else:
        st.info("Ta lekcja nie zawiera ćwiczeń praktycznych.")


def show_legacy_reflection_section(lesson):
    """Wyświetla starą sekcję refleksji (backward compatibility)"""
    if 'sections' in lesson['sections'].get('reflection', {}):
        for section in lesson["sections"]["reflection"]["sections"]:
            st.markdown(f"### {section.get('title', 'Zadanie refleksyjne')}")
            st.markdown(section.get("content", "Brak treści"), unsafe_allow_html=True)
            
            reflection_key = f"reflection_{section.get('title', '').replace(' ', '_').lower()}"
            
            with st.form(key=f"form_{reflection_key}"):
                existing_response = st.session_state.get(reflection_key, "")
                user_reflection = st.text_area(
                    "Twoja odpowiedź:",
                    value=existing_response,
                    height=200,
                    key=f"input_{reflection_key}"
                )
                
                submitted = st.form_submit_button("Zapisz odpowiedź")
                
                if submitted:
                    st.session_state[reflection_key] = user_reflection
                    st.success("Twoja odpowiedź została zapisana!")


def show_legacy_application_section(lesson):
    """Wyświetla starą sekcję zadań praktycznych (backward compatibility)"""
    if 'sections' in lesson['sections'].get('application', {}):
        for section in lesson["sections"]["application"]["sections"]:
            st.markdown(f"### {section.get('title', 'Zadanie praktyczne')}")
            st.markdown(section.get("content", "Brak treści"), unsafe_allow_html=True)
            
            task_key = f"application_{section.get('title', '').replace(' ', '_').lower()}"
            
            with st.form(key=f"form_{task_key}"):
                existing_solution = st.session_state.get(task_key, "")
                user_solution = st.text_area(
                    "Twoje rozwiązanie:",
                    value=existing_solution,
                    height=200,
                    key=f"input_{task_key}"
                )
                
                submitted = st.form_submit_button("Zapisz rozwiązanie")
                
                if submitted:
                    st.session_state[task_key] = user_solution
                    st.success("Twoje rozwiązanie zostało zapisane!")


def show_summary_tab(lesson, lesson_id):
    """Wyświetla zakładkę Podsumowanie z pod-zakładkami"""
    summary_sub_tabs = st.tabs(["📋 Podsumowanie", "📚 Case Study", "🗺️ Mapa myśli"])
    
    with summary_sub_tabs[0]:
        # Wyświetl główne podsumowanie
        if 'outro' in lesson and 'main' in lesson['outro']:
            st.markdown(lesson['outro']['main'], unsafe_allow_html=True)
        elif 'summary' in lesson:
            st.markdown(lesson['summary'], unsafe_allow_html=True)
        else:
            st.warning("Brak podsumowania w tej lekcji.")
        
        # Przycisk zakończenia lekcji
        lesson_finished = st.session_state.get('lesson_finished', False)
        
        if not lesson_finished:
            st.markdown("<div style='text-align: center; margin-top: 30px;'>", unsafe_allow_html=True)
            if st.button("🎉 Zakończ lekcję", key="complete_lesson", use_container_width=False):
                # Oznacz lekcję jako zakończoną
                mark_lesson_as_completed(lesson_id)
                
                # Check for achievements
                from utils.achievements import check_achievements
                username = st.session_state.get('username')
                if username:
                    check_achievements(username, 'lesson_completion', lesson_id=lesson_id)
                
                st.session_state.lesson_finished = True
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.balloons()
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                        color: white; padding: 20px; border-radius: 15px; margin: 20px 0;
                        text-align: center; box-shadow: 0 4px 15px rgba(76,175,80,0.3);">
                <h2 style="margin: 0 0 10px 0;">🎓 Lekcja ukończona!</h2>
                <p style="margin: 0; font-size: 18px;">Świetna robota! Możesz teraz przejść do kolejnych lekcji.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            if st.button("📚 Wróć do wszystkich lekcji", key="back_to_lessons"):
                st.session_state.lesson_finished = False
                st.session_state.current_lesson = None
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
    
    with summary_sub_tabs[1]:
        # Wyświetl studium przypadku z podsumowania
        if 'outro' in lesson and 'case_study' in lesson['outro']:
            st.markdown(lesson['outro']['case_study'], unsafe_allow_html=True)
        else:
            st.warning("Brak studium przypadku w podsumowaniu.")
    
    with summary_sub_tabs[2]:
        # Wyświetl interaktywną mapę myśli
        st.markdown("### 🗺️ Interaktywna mapa myśli")
        st.markdown("Poniżej znajdziesz interaktywną mapę myśli podsumowującą kluczowe koncepty z tej lekcji.")
        
        try:
            from utils.mind_map import create_lesson_mind_map
            mind_map_result = create_lesson_mind_map(lesson)
            
            if mind_map_result is None:
                st.info("💡 **Mapa myśli w przygotowaniu**\n\nDla tej lekcji przygotowujemy interaktywną mapę myśli, która pomoże Ci lepiej zrozumieć powiązania między różnymi konceptami. Wkrótce będzie dostępna!")
        except Exception as e:
            st.warning("⚠️ Mapa myśli nie jest obecnie dostępna. Sprawdź, czy wszystkie wymagane biblioteki są zainstalowane.")
            st.expander("Szczegóły błędu (dla deweloperów)").write(str(e))


def display_quiz(quiz_data, passing_threshold=60):
    """Wyświetla quiz z pytaniami i opcjami odpowiedzi. Zwraca True, gdy quiz jest ukończony."""
    
    if not quiz_data or "questions" not in quiz_data:
        st.warning("Ten quiz nie zawiera żadnych pytań.")
        return False, False, 0
        
    st.markdown(f"<h2>{quiz_data.get('title', 'Quiz')}</h2>", unsafe_allow_html=True)
    
    if "description" in quiz_data:
        st.markdown(quiz_data['description'])
    
    # Sprawdź czy to quiz samodiagnozy (wszystkie correct_answer są null)
    is_self_diagnostic = all(q.get('correct_answer') is None for q in quiz_data['questions'])
    
    quiz_id = f"quiz_{quiz_data.get('title', '').replace(' ', '_').lower()}"
    if quiz_id not in st.session_state:
        st.session_state[quiz_id] = {
            "answered_questions": [],
            "correct_answers": 0,
            "total_questions": len(quiz_data['questions']),
            "completed": False,
            "total_points": 0  # Dla quizów samodiagnozy
        }
    
    # Wyświetl wszystkie pytania
    for i, question in enumerate(quiz_data['questions']):
        question_id = f"{quiz_id}_q{i}"
        
        st.markdown(f"**Pytanie {i+1}: {question['question']}**")
        
        # Jeśli pytanie już zostało odpowiedziane, pokaż wynik
        if i in st.session_state[quiz_id]["answered_questions"]:
            selected = st.session_state.get(f"{question_id}_selected")
            
            # Wyświetl odpowiedzi z oznaczeniem poprawnej
            for j, option in enumerate(question['options']):
                if is_self_diagnostic:
                    if j == selected:
                        st.markdown(f"✓ **{option}** _(Twoja odpowiedź)_")
                    else:
                        st.markdown(f"○ {option}")
                else:
                    correct_answer = question.get('correct_answer')
                    is_correct = correct_answer is not None and selected == correct_answer
                    
                    if correct_answer is not None:
                        if j == correct_answer:
                            st.markdown(f"✅ **{option}** _(Poprawna odpowiedź)_")
                        elif j == selected and not is_correct:
                            st.markdown(f"❌ **{option}** _(Twoja odpowiedź)_")
                        else:
                            st.markdown(f"○ {option}")
            
            # Wyświetl wyjaśnienie
            if "explanation" in question:
                st.info(question['explanation'])
            
            st.markdown("---")
        else:
            # Wyświetl opcje odpowiedzi jako przyciski
            for j, option in enumerate(question['options']):
                if st.button(option, key=f"{question_id}_opt{j}"):
                    st.session_state[f"{question_id}_selected"] = j
                    st.session_state[quiz_id]["answered_questions"].append(i)
                    
                    if is_self_diagnostic:
                        # Dla quizów samodiagnozy - zlicz punkty (opcje 1-5 = j+1 punktów)
                        points = j + 1
                        st.session_state[quiz_id]["total_points"] += points
                    else:
                        # Dla standardowych quizów - sprawdź poprawność
                        correct_answer = question.get('correct_answer')
                        if correct_answer is not None and j == correct_answer:
                            st.session_state[quiz_id]["correct_answers"] += 1
                    
                    if len(st.session_state[quiz_id]["answered_questions"]) == st.session_state[quiz_id]["total_questions"]:
                        st.session_state[quiz_id]["completed"] = True
                    
                    st.rerun()
                    return False, False, 0
            
            st.markdown("---")
    
    # Sprawdź czy quiz jest ukończony i oblicz punkty
    is_completed = st.session_state[quiz_id].get("completed", False)
    
    if is_completed:
        if is_self_diagnostic:
            # Quiz samodiagnozy - wyświetl punkty i interpretację
            total_points = st.session_state[quiz_id].get("total_points", 0)
            max_possible_points = len(quiz_data['questions']) * 5
            
            st.success(f"📊 **Twój wynik: {total_points}/{max_possible_points} punktów**")
            st.info("🪞 Dziękujemy za szczerą samorefleksję! Twoje odpowiedzi pomogą nam lepiej dopasować materiał do Twojego stylu inwestowania.")
            
            return is_completed, True, total_points
        else:
            # Standardowy quiz z poprawnymi odpowiedziami
            correct = st.session_state[quiz_id]["correct_answers"]
            total = st.session_state[quiz_id]["total_questions"]
            percentage = (correct / total) * 100
            
            # Czy quiz został zdany (na podstawie passing_threshold)
            is_passed = percentage >= passing_threshold
            
            st.markdown(f"**Twój wynik: {correct}/{total} ({percentage:.0f}%)**")
            
            if percentage >= 80:
                st.success("Świetnie! Doskonale rozumiesz ten temat.")
            elif percentage >= passing_threshold:
                st.success(f"Bardzo dobrze! Osiągnąłeś wymagany próg {passing_threshold}% i możesz kontynuować.")
            else:
                st.error(f"Aby przejść dalej, musisz uzyskać przynajmniej {passing_threshold}% poprawnych odpowiedzi. Spróbuj ponownie!")
            
            return is_completed, is_passed, correct
    
    # Quiz nie jest jeszcze ukończony
    return is_completed, False, 0
