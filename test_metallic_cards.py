import streamlit as st
from utils.components import lesson_card

st.set_page_config(page_title="Test Metaliczno-Grafitowych Kart", layout="wide")

st.title("🎨 Test Metaliczno-Grafitowych Kart Lekcji")

st.markdown("### Jak wyglądają nowe karty lekcji z metaliczno-grafitowym gradientem:")

# Test różnych typów kart
col1, col2 = st.columns(2)

with col1:
    st.subheader("Karta nieukończona")
    lesson_card(
        title="Strach przed stratą", 
        description="Ta lekcja wprowadza podstawy teorii perspektywy, efektu dyspozycji oraz zarządzania emocjami w inwestowaniu.",
        xp=50,
        duration=15,
        difficulty="Beginner",
        completed=False
    )

with col2:
    st.subheader("Karta ukończona")
    lesson_card(
        title="Emocjonalna zmienność a zmienność rynku", 
        description="Ta lekcja pomoże Ci zrozumieć, jak emocje wpływają na Twoje decyzje inwestycyjne. Dowiesz się, jak unikać pułapek psychologicznych, które mogą prowadź...",
        xp=100,
        duration=20,
        difficulty="Intermediate",
        completed=True
    )

st.markdown("---")

st.subheader("Karta z dłuższym opisem")
lesson_card(
    title="Zaawansowane strategie zarządzania ryzykiem", 
    description="Kompleksowa lekcja obejmująca nowoczesne metody oceny i zarządzania ryzykiem inwestycyjnym. Poznasz narzędzia takie jak VaR, stress testing, oraz metody dywersyfikacji portfela. Lekcja zawiera praktyczne przykłady i case studies z rzeczywistego rynku.",
    xp=150,
    duration=45,
    difficulty="Advanced",
    completed=False
)

st.markdown("---")
st.info("💡 **Nowa animacja**: Karty mają teraz płynne przejście kolorów przy hover z wykorzystaniem pseudo-elementu ::after i cubic-bezier easing (0.4s duration).")

# Dodatkowe informacje o kolorach
with st.expander("🎨 Szczegóły gradientu i animacji"):
    st.markdown("""
    **Gradient kolorów (podstawowy):**
    - Jasny szary: `#f8f9fa` (0%)
    - Średni jasny: `#e9ecef` (20%)  
    - Środkowy: `#dee2e6` (50%)
    - Średni ciemny: `#ced4da` (80%)
    - Grafitowy: `#adb5bd` (100%)
    
    **Gradient kolorów (hover):**
    - Jasny szary: `#f1f3f4` (0%)
    - Średni jasny: `#e1e5e9` (20%)  
    - Środkowy: `#d6dbdf` (50%)
    - Średni ciemny: `#c1c8cd` (80%)
    - Grafitowy: `#9ca3af` (100%)
    
    **Animacja:**
    - Transition: `0.4s cubic-bezier(0.25, 0.8, 0.25, 1)`
    - Metoda: Pseudo-element `::after` z opacity transition
    - Efekty hover: Podniesienie karty + płynna zmiana koloru tła
    - Z-index: Zawartość karty (z-index: 2) nad overlay (z-index: 1)
    """)
