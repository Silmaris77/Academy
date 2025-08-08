import streamlit as st
from utils.components import lesson_card

st.set_page_config(page_title="Test Nowych Kolorów Czcionek", layout="wide")

st.title("🎨 Test Poprawionych Kolorów Czcionek na Ciemnym Tle")

st.markdown("""
### ✨ Co zostało poprawione:

**Kolorystyka oparta na dark mode z aplikacji:**
- **Główny tekst**: `#1a1a1a` (prawie czarny dla lepszego kontrastu)
- **Nagłówki**: `#0d1421` (bardzo ciemny granat-niebieski)
- **Opis**: `#2c3e50` (ciemny niebieski-szary)
- **Status nieukończony**: `#495057` (średni szary)
- **Status ukończony**: `#155724` (ciemny zielony)

**Kolory wzorowane na dark mode aplikacji gdzie:**
- Nagłówki: `#ffffff` (biały)
- Tekst podstawowy: `#aaaaaa` (jasny szary)
- Tło: `#2d2d2d` (ciemny szary)

**Teraz tekst będzie lepiej widoczny na metaliczno-grafitowym gradiencie! 👇**
""")

st.markdown("---")

# Demo z lepszą czytelności
col1, col2 = st.columns(2)

with col1:
    st.subheader("📖 Lepsza czytelność - nieukończona")
    lesson_card(
        title="Psychologia Masa vs Jednostka", 
        description="Descobrij jak psychologia tłumu wpływa na rynki finansowe i dlaczego masa często popełnia błędy inwestycyjne. Naucz się myśleć niezależnie i podejmować decyzje oparte na analizie, a nie emocjach.",
        xp=85,
        duration=30,
        difficulty="Intermediate",
        category="Psychologia Rynku",
        completed=False
    )

with col2:
    st.subheader("✅ Lepsza czytelność - ukończona")
    lesson_card(
        title="Strategia Dollar Cost Averaging", 
        description="Poznaj jedną z najskuteczniejszych strategii długoterminowego inwestowania. Dowiedz się jak regularnie inwestować bez względu na wahania rynku i dlaczego DCA redukuje ryzyko przy jednoczesnym maksymalizowaniu potencjału wzrostu.",
        xp=95,
        duration=25,
        difficulty="Beginner", 
        category="Strategie Inwestycyjne",
        completed=True
    )

st.markdown("---")

st.subheader("🎯 Długi tekst - test czytelności")
lesson_card(
    title="Zaawansowana Analiza Techniczna: Harmoniczne Wzorce i Fraktale", 
    description="Kompleksowy kurs zaawansowanej analizy technicznej obejmujący wzorce harmoniczne (Gartley, Butterfly, Bat, Crab), teorię fraktali na rynkach finansowych oraz zaawansowane narzędzia analizy cyklicznej. Dowiesz się jak wykorzystać proporcje Fibonacciego w praktyce, rozpoznawać formacje harmoniczne w czasie rzeczywistym oraz budować systemy transakcyjne oparte na analizie wielopoziomowej. Kurs zawiera przykłady z rzeczywistego rynku, backtesty strategii oraz praktyczne ćwiczenia na platformach tradingowych.",
    xp=150,
    duration=60,
    difficulty="Advanced",
    category="Analiza Techniczna", 
    completed=False
)

st.markdown("---")

# Porównanie kolorów
with st.expander("🎨 Porównanie starych vs nowych kolorów"):
    st.markdown("""
    **Stare kolory** (słabo czytelne na ciemnym tle):
    - Główny tekst: `#212529` (ciemny szary)
    - Nagłówek: `#1A237E` (ciemny niebieski)
    - Opis: `#555` (średni szary)
    - Status: `#757575` (jasny szary)
    
    **Nowe kolory** (lepiej czytelne):
    - Główny tekst: `#1a1a1a` (prawie czarny - większy kontrast)
    - Nagłówek: `#0d1421` (bardzo ciemny granat-niebieski)
    - Opis: `#2c3e50` (ciemny niebieski-szary)
    - Status nieukończony: `#495057` (średni szary z lepszym kontrastem)
    - Status ukończony: `#155724` (ciemny zielony zamiast jasnego)
    
    **Zalety nowych kolorów:**
    - ✅ Lepszy kontrast z metaliczno-grafitowym tłem
    - ✅ Wzorowane na kolorystyce dark mode aplikacji
    - ✅ Zachowana hierarchia typograficzna
    - ✅ Lepsze UX - czytelność bez męczenia oczu
    """)

st.success("🎉 Kolory zostały poprawione dla lepszej czytelności na ciemnym metaliczno-grafitowym tle!")
