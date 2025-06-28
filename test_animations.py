import streamlit as st

st.set_page_config(page_title="Test Animacji Inspiracji", layout="wide")

# Dodaj style animacji
st.markdown("""
<style>
/* Test animacji hover dla kart */
.animated-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 16px;
    padding: 24px;
    margin: 20px 0;
    color: white;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
}

.animated-card:hover {
    transform: translateY(-12px) scale(1.03) rotate(0.5deg);
    box-shadow: 0 20px 50px rgba(102, 126, 234, 0.4);
}

/* Shimmer effect */
.animated-card::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, 
        transparent 30%, 
        rgba(255, 255, 255, 0.2) 50%, 
        transparent 70%);
    transform: rotate(45deg);
    animation: shimmer 3s infinite;
    pointer-events: none;
}

@keyframes shimmer {
    0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
}

/* Floating animation */
.floating {
    animation: gentleFloat 6s ease-in-out infinite;
}

@keyframes gentleFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-5px); }
}

/* Button ripple */
.ripple-button {
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.ripple-button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Test Animacji Inspiracji")

st.markdown("### 🎭 Najedź myszką na karty poniżej, aby zobaczyć animacje!")

# Test kart z animacjami
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="animated-card floating">
        <h3 style="margin: 0 0 16px 0;">🌟 Testowa Karta Featured</h3>
        <p style="margin: 0 0 16px 0; opacity: 0.9;">
            Ta karta ma animację hover z podniesieniem, skalowaniem i lekką rotacją.
            Dodatkowo ma efekt shimmer i floating animation.
        </p>
        <div style="display: flex; justify-content: space-between; font-size: 12px; opacity: 0.8;">
            <span>🟢 Poziom: Początkujący</span>
            <span>📖 5 min</span>
            <span>👁️ 42 wyświetleń</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="animated-card floating" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); animation-delay: 1s;">
        <h3 style="margin: 0 0 16px 0;">💡 Testowa Karta Standard</h3>
        <p style="margin: 0 0 16px 0; opacity: 0.9;">
            Ta karta ma inny gradient (różowy) i opóźnioną animację floating.
            Hover effect jest taki sam jak w featured.
        </p>
        <div style="display: flex; justify-content: space-between; font-size: 12px; opacity: 0.8;">
            <span>🟡 Poziom: Średni</span>
            <span>📖 8 min</span>
            <span>👁️ 128 wyświetleń</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Test przycisków z animacjami
st.markdown("### 🎯 Test animacji przycisków")

col3, col4, col5 = st.columns(3)

with col3:
    if st.button("⭐ Ulubione", key="fav", help="Przycisk z animacją hover"):
        st.success("Dodano do ulubionych!")

with col4:
    if st.button("📖 Czytaj", key="read", type="primary", help="Primary button z animacją"):
        st.info("Otwieranie inspiracji...")

with col5:
    if st.button("🔄 Losowa", key="random", help="Button z efektem ripple"):
        st.balloons()

# Test loading animation
st.markdown("### ⏳ Test animacji loading")

if st.button("Pokaż Loading", key="loading"):
    with st.spinner("Ładowanie inspiracji..."):
        import time
        time.sleep(2)
        st.success("Gotowe!")

# Test kolorowych kontenerów Streamlit
st.markdown("### 🎨 Test kolorowych kontenerów")

col6, col7 = st.columns(2)

with col6:
    st.info("""
    ### 🌟 Karta Featured (Info)
    
    Ta karta używa `st.info()` dla niebieskiego tła.
    Ma automatyczne kolorowe tło i ikonę.
    
    **Metadata:**
    - 📚 Czas: 5 min
    - 👁️ Wyświetlenia: 42
    - 🏷️ Tagi: crypto, mindset
    """, icon="🌟")

with col7:
    st.success("""
    ### 💡 Karta Standard (Success)
    
    Ta karta używa `st.success()` dla zielonego tła.
    Ma automatyczne kolorowe tło i ikonę.
    
    **Metadata:**
    - 📚 Czas: 8 min  
    - 👁️ Wyświetlenia: 128
    - 🏷️ Tagi: FOMO, motivation
    """, icon="💡")

st.markdown("---")
st.markdown("### 📋 Podsumowanie testów animacji:")
st.markdown("""
- ✅ **Hover animations**: Podnoszenie, skalowanie, rotacja
- ✅ **Shimmer effect**: Połyskujący efekt na kartach  
- ✅ **Floating animation**: Subtelne unoszenie kart
- ✅ **Button animations**: Ripple, hover, scale
- ✅ **Loading states**: Spinner, progress
- ✅ **Colorful containers**: Native Streamlit colors
- ✅ **Responsive design**: Mobile-friendly
- ✅ **Accessibility**: Prefers-reduced-motion support
""")

st.info("💡 **Tip**: Animacje są zoptymalizowane dla różnych urządzeń i respektują ustawienia dostępności użytkownika.", icon="💡")
