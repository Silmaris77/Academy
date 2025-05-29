"""
Funkcje do generowania interaktywnych map myśli dla lekcji
"""
import streamlit as st

def create_lesson_mind_map(lesson_data):
    """
    Tworzy interaktywną mapę myśli dla danej lekcji
    
    Args:
        lesson_data (dict): Dane lekcji w formacie JSON
    """
    try:
        from streamlit_agraph import agraph, Node, Edge, Config
        import streamlit as st
        
        # Sprawdź czy lekcja ma dedykowane dane do mapy myśli
        if 'mind_map' in lesson_data:
            return create_data_driven_mind_map(lesson_data['mind_map'])
        
        # Fallback dla lekcji B1C1L1 (backward compatibility)
        lesson_id = lesson_data.get('id', '')
        if lesson_id == 'B1C1L1':
            return create_b1c1l1_mind_map()
        
        # Dla innych lekcji bez danych - stwórz automatyczną mapę
        return create_auto_generated_mind_map(lesson_data)
            
    except ImportError:
        # Fallback jeśli streamlit-agraph nie jest dostępne
        import streamlit as st
        st.warning("📋 Mapa myśli nie jest obecnie dostępna. Zainstaluj bibliotekę streamlit-agraph aby włączyć tę funkcję.")
        return None

def create_b1c1l1_mind_map():
    """
    Tworzy mapę myśli specjalnie dla lekcji B1C1L1 - Strach przed stratą
    """
    try:
        from streamlit_agraph import agraph, Node, Edge, Config
        
        # Definiuj węzły
        nodes = []
        edges = []
        
        # Centralny węzeł
        nodes.append(Node(id="central", 
                         label="💸 STRACH PRZED STRATĄ", 
                         size=30,
                         color="#FF6B6B",
                         font={"size": 16, "color": "white"}))
        
        # Główne koncepty
        concepts = [
            {"id": "teoria", "label": "📊 Teoria perspektywy", "color": "#4ECDC4"},
            {"id": "dyspozycja", "label": "🔄 Efekt dyspozycji", "color": "#45B7D1"},
            {"id": "dopamina", "label": "🧠 Dopamina", "color": "#96CEB4"},
            {"id": "framing", "label": "🖼️ Framing", "color": "#FECA57"}
        ]
        
        for concept in concepts:
            nodes.append(Node(id=concept["id"],
                            label=concept["label"],
                            size=20,
                            color=concept["color"],
                            font={"size": 12, "color": "white"}))
            edges.append(Edge(source="central", target=concept["id"]))
        
        # Szczegóły teorii perspektywy
        teoria_details = [
            {"id": "bol_straty", "label": "😢 Ból straty 2-2,5x silniejszy", "parent": "teoria"},
            {"id": "pewnosc", "label": "🛡️ Preferujemy pewność", "parent": "teoria"},
            {"id": "awersja", "label": "⚠️ Awersja do ryzyka", "parent": "teoria"}
        ]
        
        # Szczegóły efektu dyspozycji
        dyspozycja_details = [
            {"id": "sprzedaj_zyski", "label": "💰 Za szybko sprzedajemy zyski", "parent": "dyspozycja"},
            {"id": "trzymaj_straty", "label": "📉 Za długo trzymamy straty", "parent": "dyspozycja"},
            {"id": "get_even", "label": "🎯 Syndrom 'wyjdę na zero'", "parent": "dyspozycja"}
        ]
        
        # Szczegóły dopaminy
        dopamina_details = [
            {"id": "nagroda", "label": "🎉 System nagrody w mózgu", "parent": "dopamina"},
            {"id": "uzaleznienie", "label": "🎰 Uzależnienie od transakcji", "parent": "dopamina"},
            {"id": "euforia", "label": "🚀 Euforia po zyskach", "parent": "dopamina"}
        ]
        
        # Szczegóły framingu
        framing_details = [
            {"id": "prezentacja", "label": "📝 Sposób prezentacji wpływa na decyzje", "parent": "framing"},
            {"id": "pozytywny", "label": "😊 Pozytywne vs negatywne ujęcie", "parent": "framing"},
            {"id": "manipulacja", "label": "🎭 Podatność na manipulację", "parent": "framing"}
        ]
        
        # Dodaj wszystkie szczegóły
        all_details = teoria_details + dyspozycja_details + dopamina_details + framing_details
        
        for detail in all_details:
            nodes.append(Node(id=detail["id"],
                            label=detail["label"],
                            size=12,
                            color="#DDA0DD",
                            font={"size": 10, "color": "black"}))
            edges.append(Edge(source=detail["parent"], target=detail["id"]))
        
        # Rozwiązania praktyczne
        solutions = [
            {"id": "zoom_out", "label": "🔍 Zoom out - szeroka perspektywa"},
            {"id": "limit_strat", "label": "🚧 Wyznacz limit strat"},
            {"id": "stop_checking", "label": "📵 Przestań sprawdzać apki"},
            {"id": "plan", "label": "📋 Trzymaj się planu"}
        ]
        
        for solution in solutions:
            nodes.append(Node(id=solution["id"],
                            label=solution["label"],
                            size=15,
                            color="#90EE90",
                            font={"size": 11, "color": "black"}))
            edges.append(Edge(source="central", target=solution["id"]))
        
        # Case study - Kuba
        nodes.append(Node(id="kuba",
                        label="👨‍💻 Case Study: Kuba i $MOONZ",
                        size=18,
                        color="#FF8C42",
                        font={"size": 12, "color": "white"}))
        edges.append(Edge(source="central", target="kuba"))
        
        kuba_details = [
            {"id": "fomo", "label": "😱 FOMO na $MOONZ", "parent": "kuba"},
            {"id": "spadek", "label": "📉 -20% w 2 dni", "parent": "kuba"},
            {"id": "panika", "label": "😰 Panika i sprawdzanie co 3 min", "parent": "kuba"}
        ]
        
        for detail in kuba_details:
            nodes.append(Node(id=detail["id"],
                            label=detail["label"],
                            size=10,
                            color="#FFB347",
                            font={"size": 9, "color": "black"}))
            edges.append(Edge(source=detail["parent"], target=detail["id"]))
        
        # Konfiguracja wyświetlania
        config = Config(width=800, 
                       height=600,
                       directed=False,
                       physics=True,
                       hierarchical=False,
                       nodeHighlightBehavior=True,
                       highlightColor="#F7A7A6",
                       collapsible=False)
        
        # Wyświetl mapę
        return_value = agraph(nodes=nodes, 
                             edges=edges, 
                             config=config)
        
        return return_value
        
    except ImportError:
        st.error("Nie można załadować biblioteki streamlit-agraph. Zainstaluj ją używając: pip install streamlit-agraph")
        return None
    except Exception as e:
        st.error(f"Błąd podczas tworzenia mapy myśli: {str(e)}")
        return None

def create_data_driven_mind_map(mind_map_data):
    """
    Tworzy mapę myśli na podstawie danych z lesson_data['mind_map']
    
    Args:
        mind_map_data (dict): Dane struktury mapy myśli
    """
    try:
        from streamlit_agraph import agraph, Node, Edge, Config
        import streamlit as st
        
        nodes = []
        edges = []
        
        # Centralny węzeł
        central = mind_map_data['central_node']
        nodes.append(Node(
            id=central['id'],
            label=central['label'],
            size=central.get('size', 25),
            color=central.get('color', '#FF6B6B'),
            font={"size": central.get('font_size', 16), "color": "white"}
        ))
        
        # Kategorie główne
        for category in mind_map_data.get('categories', []):
            nodes.append(Node(
                id=category['id'],
                label=category['label'],
                size=category.get('size', 20),
                color=category.get('color', '#4ECDC4'),
                font={"size": category.get('font_size', 12), "color": "white"}
            ))
            
            # Połącz z centralnym węzłem
            edges.append(Edge(
                source=central['id'],
                target=category['id']
            ))
            
            # Dodaj szczegóły kategorii
            for detail in category.get('details', []):
                nodes.append(Node(
                    id=detail['id'],
                    label=detail['label'],
                    size=detail.get('size', 12),
                    color=detail.get('color', '#DDA0DD'),
                    font={"size": detail.get('font_size', 10), "color": "black"}
                ))
                edges.append(Edge(
                    source=category['id'],
                    target=detail['id']
                ))
        
        # Rozwiązania praktyczne
        for solution in mind_map_data.get('solutions', []):
            nodes.append(Node(
                id=solution['id'],
                label=solution['label'],
                size=solution.get('size', 15),
                color=solution.get('color', '#90EE90'),
                font={"size": solution.get('font_size', 11), "color": "black"}
            ))
            edges.append(Edge(
                source=central['id'],
                target=solution['id']
            ))
        
        # Case study
        if 'case_study' in mind_map_data:
            case = mind_map_data['case_study']
            nodes.append(Node(
                id=case['id'],
                label=case['label'],
                size=case.get('size', 18),
                color=case.get('color', '#FF8C42'),
                font={"size": case.get('font_size', 12), "color": "white"}
            ))
            edges.append(Edge(
                source=central['id'],
                target=case['id']
            ))
            
            # Szczegóły case study
            for detail in case.get('details', []):
                nodes.append(Node(
                    id=detail['id'],
                    label=detail['label'],
                    size=detail.get('size', 10),
                    color=detail.get('color', '#FFB347'),
                    font={"size": detail.get('font_size', 9), "color": "black"}
                ))
                edges.append(Edge(
                    source=case['id'],
                    target=detail['id']
                ))
        
        # Dodatkowe połączenia
        for connection in mind_map_data.get('connections', []):
            edges.append(Edge(
                source=connection['from'],
                target=connection['to']
            ))
        
        # Konfiguracja
        config_data = mind_map_data.get('config', {})
        config = Config(
            width=config_data.get('width', 800), 
            height=config_data.get('height', 600),
            directed=config_data.get('directed', False),
            physics=config_data.get('physics', True),
            hierarchical=config_data.get('hierarchical', False),
            nodeHighlightBehavior=True,
            highlightColor="#F7A7A6",
            collapsible=False
        )
        
        return agraph(nodes=nodes, edges=edges, config=config)
        
    except ImportError:
        import streamlit as st
        st.error("Nie można załadować biblioteki streamlit-agraph. Zainstaluj ją używając: pip install streamlit-agraph")
        return None
    except Exception as e:
        import streamlit as st
        st.error(f"Błąd podczas tworzenia mapy myśli: {str(e)}")
        return None

def create_auto_generated_mind_map(lesson_data):
    """
    Automatycznie generuje mapę myśli na podstawie struktury lekcji
    gdy brak dedykowanych danych mind_map
    """
    try:
        from streamlit_agraph import agraph, Node, Edge, Config
        import streamlit as st
        
        nodes = []
        edges = []
        
        # Centralny węzeł z tytułem lekcji
        title = lesson_data.get('title', 'Lekcja')
        nodes.append(Node(id="central", 
                         label=f"📚 {title}", 
                         size=25,
                         color="#6C5CE7",
                         font={"size": 14, "color": "white"}))
        
        # Dodaj sekcje lekcji jako węzły
        if 'sections' in lesson_data:
            sections = lesson_data['sections']
            
            # Materiał lekcji
            if 'learning' in sections and 'sections' in sections['learning']:
                for i, section in enumerate(sections['learning']['sections'][:4]):  # Max 4 sekcje
                    section_id = f"section_{i}"
                    section_title = section.get('title', f'Sekcja {i+1}')
                    # Skróć tytuł jeśli jest za długi
                    if len(section_title) > 40:
                        section_title = section_title[:37] + "..."
                    
                    nodes.append(Node(id=section_id,
                                    label=f"📖 {section_title}",
                                    size=15,
                                    color="#74B9FF",
                                    font={"size": 10, "color": "white"}))
                    edges.append(Edge(source="central", target=section_id))
        
        # Dodaj elementy strukturalne
        structural_elements = []
        
        if lesson_data.get('sections', {}).get('opening_quiz'):
            structural_elements.append({"id": "quiz_start", "label": "🧠 Quiz startowy", "color": "#FD79A8"})
        
        if lesson_data.get('sections', {}).get('reflection'):
            structural_elements.append({"id": "reflection", "label": "🤔 Refleksja", "color": "#FDCB6E"})
            
        if lesson_data.get('sections', {}).get('application'):
            structural_elements.append({"id": "application", "label": "💪 Zastosowanie", "color": "#A29BFE"})
            
        if lesson_data.get('sections', {}).get('closing_quiz'):
            structural_elements.append({"id": "quiz_end", "label": "🎯 Quiz końcowy", "color": "#E17055"})
        
        for element in structural_elements:
            nodes.append(Node(id=element["id"],
                            label=element["label"],
                            size=12,
                            color=element["color"],
                            font={"size": 10, "color": "white"}))
            edges.append(Edge(source="central", target=element["id"]))
        
        # Dodaj info o XP
        xp_reward = lesson_data.get('xp_reward', 100)
        nodes.append(Node(id="xp_reward",
                        label=f"💎 {xp_reward} XP",
                        size=14,
                        color="#00B894",
                        font={"size": 11, "color": "white"}))
        edges.append(Edge(source="central", target="xp_reward"))
        
        config = Config(width=700, 
                       height=500,
                       directed=False,
                       physics=True,
                       hierarchical=False,
                       nodeHighlightBehavior=True,
                       highlightColor="#F7A7A6")
        
        # Dodaj informację o automatycznym generowaniu
        st.info("🤖 **Automatycznie wygenerowana mapa myśli**\n\nTa mapa została utworzona na podstawie struktury lekcji. Dla lepszego doświadczenia, dedykowana mapa myśli jest w przygotowaniu!")
        
        return agraph(nodes=nodes, edges=edges, config=config)
        
    except ImportError:
        import streamlit as st
        st.error("Nie można załadować biblioteki streamlit-agraph")
        return None
    except Exception as e:
        import streamlit as st
        st.error(f"Błąd podczas tworzenia automatycznej mapy myśli: {str(e)}")
        return None
