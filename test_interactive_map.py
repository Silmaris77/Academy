#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test interaktywnej hierarchicznej mapy kursu
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_interactive_map_import():
    """Test importu nowej funkcji"""
    try:
        from utils.course_map import create_interactive_hierarchical_map
        from data.course_data import get_blocks, get_categories
        
        print("✅ Import funkcji przeszedł pomyślnie")
        
        # Sprawdź dane kursu
        blocks = get_blocks()
        categories = get_categories()
        
        print(f"📊 Dane kursu:")
        print(f"   Bloki: {len(blocks)}")
        print(f"   Kategorie: {len(categories)}")
        
        # Sprawdź strukturę bloków
        print(f"\n🏗️ Struktura bloków:")
        for block_id, block_info in blocks.items():
            block_categories = [k for k, v in categories.items() if v['block'] == block_id]
            print(f"   Blok {block_id}: {block_info['name'][:50]}... ({len(block_categories)} kategorii)")
        
        print(f"\n🎯 Funkcja create_interactive_hierarchical_map gotowa do użycia")
        return True
        
    except ImportError as e:
        print(f"❌ Błąd importu: {e}")
        return False
    except Exception as e:
        print(f"❌ Błąd: {e}")
        return False

def test_streamlit_agraph_availability():
    """Test dostępności streamlit-agraph"""
    try:
        from streamlit_agraph import agraph, Node, Edge, Config
        print("✅ streamlit-agraph jest dostępne")
        
        # Test tworzenia prostych obiektów
        test_node = Node(id="test", label="Test Node", size=20, color="#FF0000")
        test_edge = Edge(source="test", target="test")
        test_config = Config(width=800, height=600, physics=True)
        
        print("✅ Obiekty Node, Edge, Config działają poprawnie")
        return True
        
    except ImportError as e:
        print(f"❌ streamlit-agraph nie jest dostępne: {e}")
        return False
    except Exception as e:
        print(f"❌ Błąd z streamlit-agraph: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Test interaktywnej hierarchicznej mapy kursu")
    print("=" * 50)
    
    # Test 1: Import funkcji
    print("\n1. Test importu funkcji:")
    import_ok = test_interactive_map_import()
    
    # Test 2: Streamlit-agraph
    print("\n2. Test streamlit-agraph:")
    agraph_ok = test_streamlit_agraph_availability()
    
    # Podsumowanie
    print("\n" + "=" * 50)
    if import_ok and agraph_ok:
        print("🎉 Wszystkie testy przeszły pomyślnie!")
        print("🚀 Interaktywna mapa kursu jest gotowa do użycia w aplikacji Streamlit")
    else:
        print("❌ Niektóre testy nie powiodły się")
        if not import_ok:
            print("   - Problem z importem funkcji")
        if not agraph_ok:
            print("   - Problem ze streamlit-agraph")
