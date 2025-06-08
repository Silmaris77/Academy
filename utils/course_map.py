"""
Moduł do tworzenia interaktywnej mapy struktury kursu z wykorzystaniem streamlit-agraph
"""
import streamlit as st
from data.course_data import get_blocks, get_categories, get_lessons_for_category

def create_course_structure_map():
    """
    Tworzy interaktywną mapę struktury kursu: Moduły → Kategorie → Lekcje
    """
    try:
        from streamlit_agraph import agraph, Node, Edge, Config
    except ImportError:
        st.error("❌ Błąd: Biblioteka streamlit-agraph nie jest zainstalowana")
        st.info("Aby zainstalować, uruchom: `pip install streamlit-agraph`")
        return
        
    try:
        
        nodes = []
        edges = []
        
        # Pobierz dane kursu
        blocks = get_blocks()
        categories = get_categories()        # Centralny węzeł - Cały kurs (kolor z Bloku 2 Skills)
        nodes.append(Node(
            id="course_center",
            label="🎓 BrainVenture Academy",
            size=35,
            color="#43C6AC",
            font={"size": 18, "color": "white"},
            shape="dot"
        ))
        
        # Kolory zsynchronizowane z Skills section blocks
        block_colors = [
            "#FF9950",  # Block 1: Emocje & Mózg (pomarańczowy-czerwony)
            "#43C6AC",  # Block 2: Wewnętrzny Kompas (morski-zielony)
            "#667eea",  # Block 3: Świadomość Działania (niebieski-fioletowy)
            "#f093fb",  # Block 4: Elastyczność & Testowanie (różowy-magenta)
            "#4facfe"   # Block 5: Mistrzostwo & Wspólnota (niebieski-cyan)
        ]
          # Dodaj bloki (moduły)
        for block_id, block_info in blocks.items():
            block_node_id = f"block_{block_id}"
            
            # Skróć nazwę bloku jeśli jest za długa
            block_name = block_info['name']
            if len(block_name) > 60:
                block_name = block_name[:57] + "..."
            
            nodes.append(Node(
                id=block_node_id,
                label=block_name,
                size=25,
                color=block_colors[(block_id - 1) % len(block_colors)],
                font={"size": 14, "color": block_colors[(block_id - 1) % len(block_colors)]},
                shape="dot"
            ))
            
            # Połącz z centrum
            edges.append(Edge(source="course_center", target=block_node_id))
          # Dodaj kategorie - kolory zsynchronizowane z Skills section blocks
        category_colors = [
            "#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe",  # Skills blocks colors
            "#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe",  # Repeat for more categories
            "#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe"   # Repeat for remaining categories
        ]
        
        for category_id, category_info in categories.items():
            category_node_id = f"category_{category_id}"
            block_id = category_info['block']
            
            # Skróć nazwę kategorii
            category_name = f"{category_info['icon']} {category_info['name']}"
            if len(category_name) > 50:
                category_name = category_name[:47] + "..."
            
            nodes.append(Node(
                id=category_node_id,
                label=category_name,
                size=18,
                color=category_colors[(category_id - 1) % len(category_colors)],
                font={"size": 11, "color": category_colors[(category_id - 1) % len(category_colors)]},
                shape="dot"
            ))
              # Połącz z odpowiednim blokiem
            block_node_id = f"block_{block_id}"
            edges.append(Edge(source=block_node_id, target=category_node_id))
            
            # Dodaj przykładowe lekcje (pierwsze 3 z każdej kategorii) - kolory z Skills blocks
            lessons = get_lessons_for_category(category_id)
            lesson_colors = ["#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe"]  # Skills blocks colors
            
            for i, lesson_data in enumerate(lessons):
                if i >= 3:  # Limit do 3 lekcji na kategorię dla czytelności
                    break
                
                lesson_id = lesson_data.get('id', f'lesson_{category_id}_{i}')
                lesson_node_id = f"lesson_{lesson_id}"
                lesson_title = lesson_data.get('title', f'Lekcja {lesson_id}')
                
                # Skróć tytuł lekcji
                if len(lesson_title) > 40:
                    lesson_title = lesson_title[:37] + "..."
                
                lesson_color = lesson_colors[i % len(lesson_colors)]
                nodes.append(Node(
                    id=lesson_node_id,
                    label=f"📚 {lesson_title}",
                    size=12,
                    color=lesson_color,
                    font={"size": 9, "color": lesson_color},
                    shape="dot"
                ))
                  # Połącz z kategorią
                edges.append(Edge(source=category_node_id, target=lesson_node_id))
            
            # Jeśli jest więcej niż 3 lekcje, dodaj węzeł "..." z kolorem Skills
            if len(lessons) > 3:
                more_node_id = f"more_{category_id}"
                nodes.append(Node(
                    id=more_node_id,
                    label=f"... i {len(lessons) - 3} więcej",
                    size=10,
                    color="#43C6AC",  # Skills Block 2 color
                    font={"size": 8, "color": "#43C6AC"},
                    shape="dot"
                ))
                edges.append(Edge(source=category_node_id, target=more_node_id))
        
        # Konfiguracja wizualizacji
        config = Config(
            width="100%",
            height=900,
            directed=True,
            physics=True,
            hierarchical=False,
            nodeHighlightBehavior=True,
            highlightColor="#43C6AC"  # Zsynchronizowany z Skills Block 2
        )
        
        # Wyświetl mapę
        return agraph(nodes=nodes, edges=edges, config=config)
        
    except Exception as e:
        st.error(f"Błąd podczas tworzenia mapy kursu: {str(e)}")
        return None

def create_simplified_course_map():
    """
    Uproszczona wersja mapy kursu - tylko Moduły → Kategorie
    """
    try:
        from streamlit_agraph import agraph, Node, Edge, Config
    except ImportError:
        st.error("❌ Błąd: Biblioteka streamlit-agraph nie jest zainstalowana")
        st.info("Aby zainstalować, uruchom: `pip install streamlit-agraph`")
        return
        
    try:
        
        nodes = []
        edges = []
          # Pobierz dane kursu
        blocks = get_blocks()
        categories = get_categories()
        
        # Centralny węzeł - zsynchronizowany z Skills Block 2
        nodes.append(Node(
            id="course_center",
            label="🎓 BrainVenture Academy\n5 Modułów | 15 Kategorii | 150+ Lekcji",
            size=40,
            color="#43C6AC",  # Skills Block 2 color
            font={"size": 16, "color": "#43C6AC"},
            shape="dot"        ))
        
        # Kolory dla bloków - zsynchronizowane z Skills section blocks
        block_colors = [
            "#FF9950",  # Block 1: Emocje & Mózg
            "#43C6AC",  # Block 2: Wewnętrzny Kompas
            "#667eea",  # Block 3: Świadomość Działania
            "#f093fb",  # Block 4: Elastyczność & Testowanie
            "#4facfe"   # Block 5: Mistrzostwo & Wspólnota
        ]
          # Dodaj bloki
        for block_id, block_info in blocks.items():
            block_node_id = f"block_{block_id}"
            
            # Zlicz kategorie w bloku
            categories_in_block = [cat for cat in categories.values() if cat['block'] == block_id]
            category_count = len(categories_in_block)
            
            block_name = f"MODUŁ {block_id}\n{block_info['name']}\n({category_count} kategorii)"
            
            nodes.append(Node(
                id=block_node_id,
                label=block_name,
                size=30,
                color=block_colors[block_id - 1],
                font={"size": 12, "color": block_colors[block_id - 1]},
                shape="dot"
            ))
            
            edges.append(Edge(source="course_center", target=block_node_id))
          # Dodaj kategorie - kolory zsynchronizowane z Skills section blocks
        category_colors = [
            "#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe",  # Skills blocks colors
            "#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe",  # Repeat for more categories
            "#FF9950", "#43C6AC", "#667eea", "#f093fb", "#4facfe"   # Repeat for remaining categories
        ]
        
        for category_id, category_info in categories.items():
            category_node_id = f"category_{category_id}"
            block_id = category_info['block']
            
            # Zlicz lekcje w kategorii
            lessons = get_lessons_for_category(category_id)
            lesson_count = len(lessons)
            
            category_name = f"{category_info['icon']} {category_info['name']}\n({lesson_count} lekcji)"
            
            nodes.append(Node(
                id=category_node_id,
                label=category_name,
                size=20,
                color=category_colors[category_id - 1],
                font={"size": 10, "color": category_colors[category_id - 1]},
                shape="dot"            ))
            
            block_node_id = f"block_{block_id}"
            edges.append(Edge(source=block_node_id, target=category_node_id))
        
        # Konfiguracja dla uproszczonej mapy
        config = Config(
            width="100%",
            height=850,
            directed=True,
            physics=True,
            hierarchical=True,
            nodeHighlightBehavior=True,
            highlightColor="#43C6AC"  # Zsynchronizowany z Skills Block 2
        )
        
        return agraph(nodes=nodes, edges=edges, config=config)
        
    except Exception as e:
        st.error(f"Błąd podczas tworzenia uproszczonej mapy kursu: {str(e)}")
        return None

def show_course_statistics():
    """
    Wyświetla statystyki kursu w formie kart
    """
    blocks = get_blocks()
    categories = get_categories()
    
    # Oblicz łączną liczbę lekcji
    total_lessons = 0
    for category_id in categories.keys():
        lessons = get_lessons_for_category(category_id)
        total_lessons += len(lessons)
    
    # Wyświetl statystyki w kolumnach
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 15px; text-align: center; color: white;">
            <h2 style="margin: 0; font-size: 2.5rem;">5</h2>
            <p style="margin: 5px 0 0 0; font-size: 1.1rem;">Modułów Tematycznych</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 20px; border-radius: 15px; text-align: center; color: white;">
            <h2 style="margin: 0; font-size: 2.5rem;">15</h2>
            <p style="margin: 5px 0 0 0; font-size: 1.1rem;">Kategorii Umiejętności</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 20px; border-radius: 15px; text-align: center; color: white;">
            <h2 style="margin: 0; font-size: 2.5rem;">{total_lessons}+</h2>
            <p style="margin: 5px 0 0 0; font-size: 1.1rem;">Interaktywnych Lekcji</p>
        </div>
        """, unsafe_allow_html=True)
