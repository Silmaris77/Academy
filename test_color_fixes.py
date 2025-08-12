import streamlit as st
from utils.material3_components import apply_material3_theme
from utils.components import lesson_card

st.set_page_config(page_title="Test poprawek kolorów", layout="wide")

def test_color_improvements():
    """Test poprawionych kolorów tekstu i nagłówków"""
    
    # Zastosuj nasze poprawki kolorów
    apply_material3_theme()
    
    st.title("🎨 Test poprawionych kolorów")
    st.header("Nagłówek h2 z poprawionym kontrastem")
    st.subheader("Nagłówek h3 z poprawionym kontrastem")
    
    st.markdown("## Markdown nagłówek h2")
    st.markdown("### Markdown nagłówek h3")
    
    st.write("**Zwykły tekst** - powinien być teraz bardziej czytelny z poprawionym kontrastem!")
    
    st.info("🔧 **Poprawki kolorów wykonane:**")
    st.markdown("""
    - ✅ Nagłówki h1, h2, h3: biały kolor z text-shadow
    - ✅ Ogólny tekst: jasny kolor z text-shadow
    - ✅ Tekst w kartach lekcji: biały z text-shadow
    - ✅ Tekst w kontenerach: lepszy kontrast
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 Test karty lekcji z poprawionymi kolorami:")
    
    # Test karty lekcji
    lesson_card(
        title="Przykładowa lekcja z poprawionymi kolorami",
        description="Ta lekcja demonstruje poprawiony kontrast tekstu. Czy tekst jest teraz bardziej czytelny?",
        xp=100,
        difficulty="beginner",
        category="Test",
        completed=False,
        button_text="Sprawdź czytelność",
        button_key="test_lesson"
    )
    
    st.success("✅ Jeśli widzisz ten tekst wyraźnie, poprawki kolorów działają!")
    
    st.markdown("---")
    st.markdown("**Sprawdź czy wszystkie elementy są teraz bardziej czytelne:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Kolumna 1")
        st.write("Tekst w pierwszej kolumnie")
        
    with col2:
        st.markdown("#### Kolumna 2") 
        st.write("Tekst w drugiej kolumnie")
        
    with col3:
        st.markdown("#### Kolumna 3")
        st.write("Tekst w trzeciej kolumnie")

if __name__ == "__main__":
    test_color_improvements()
