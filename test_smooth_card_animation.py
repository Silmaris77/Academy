import streamlit as st
from utils.components import lesson_card

st.set_page_config(page_title="Demo Płynnej Animacji Kart", layout="wide")

st.title("🎬 Demo Płynnej Animacji Hover dla Kart Lekcji")

st.markdown("""
### ✨ Co zostało poprawione:

1. **Płynna animacja kolorów** - Wykorzystanie pseudo-elementu `::after` zamiast zmiany `background`
2. **Cubic-bezier easing** - Profesjonalna krzywa animacji (0.25, 0.8, 0.25, 1) 
3. **Dłuższy czas trwania** - 0.4s zamiast 0.3s dla bardziej zauważalnego efektu
4. **Opacity transition** - Nakładka fade-in/out zamiast skokowej zmiany kolorów
5. **Z-index layering** - Poprawna hierarchia warstw (zawartość nad animacją)

**Teraz najedź na karty poniżej, aby zobaczyć płynną animację! 👇**
""")

st.markdown("---")

# Demo różnych stanów kart
col1, col2 = st.columns(2)

with col1:
    st.subheader("🟡 Karta nieukończona")
    st.markdown("<small>Najedź myszką, aby zobaczyć płynną animację</small>", unsafe_allow_html=True)
    lesson_card(
        title="Psychologia Inwestowania", 
        description="Poznaj tajniki psychologii inwestorów i dowiedz się, jak emocje wpływają na decyzje finansowe. Lekcja zawiera praktyczne ćwiczenia i real-world case studies.",
        xp=75,
        duration=25,
        difficulty="Beginner",
        category="Psychologia",
        completed=False
    )

with col2:
    st.subheader("✅ Karta ukończona")
    st.markdown("<small>Animacja działa także dla ukończonych lekcji</small>", unsafe_allow_html=True)
    lesson_card(
        title="Zarządzanie Ryzykiem", 
        description="Zaawansowane techniki zarządzania ryzykiem w portfolio. Dowiedz się jak wykorzystać hedging, dywersyfikację i nowoczesne narzędzia analityczne.",
        xp=120,
        duration=35,
        difficulty="Advanced", 
        category="Risk Management",
        completed=True
    )

st.markdown("---")

st.subheader("🎯 Karta z długim opisem")
st.markdown("<small>Test animacji z większą ilością tekstu</small>", unsafe_allow_html=True)

lesson_card(
    title="Analiza Fundamentalna vs Techniczna", 
    description="Kompleksowe porównanie dwóch głównych szkół analizy rynkowej. Poznasz zalety i wady każdego podejścia, nauczysz się kiedy używać której metody oraz jak łączyć oba podejścia dla maksymalnej skuteczności. Lekcja zawiera konkretne przykłady, narzędzia oraz step-by-step guidance.",
    xp=95,
    duration=40,
    difficulty="Intermediate",
    category="Market Analysis", 
    completed=False
)

st.markdown("---")

# Technical details
with st.expander("⚙️ Szczegóły techniczne animacji"):
    st.markdown("""
    **CSS Transition Details:**
    ```css
    .m3-lesson-card {
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    
    .m3-lesson-card::after {
        opacity: 0;
        transition: opacity 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
        background: linear-gradient(/* darker metallic gradient */);
        z-index: 1;
    }
    
    .m3-lesson-card:hover::after {
        opacity: 1;
    }
    
    .m3-card-content {
        z-index: 2; /* Above the overlay */
    }
    ```
    
    **Dlaczego to działa lepiej:**
    - `background` gradients nie animują się płynnie w CSS
    - `opacity` transition jest bardzo performant
    - Pseudo-element pozwala na niezależną animację tła
    - Cubic-bezier daje profesjonalny efekt "ease-out"
    """)

st.success("🎉 Animacja została poprawiona! Najedź na karty aby zobaczyć płynne przejście kolorów.")
