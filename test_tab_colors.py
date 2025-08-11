"""
Test do sprawdzenia kolorów zakładek w Streamlit
"""
import streamlit as st

st.set_page_config(
    page_title="Test kolorów zakładek",
    layout="wide"
)

st.title("🎨 Test kolorów zakładek")

st.markdown("Sprawdźmy jak wyglądają domyślne kolory zakładek:")

# Tworzymy przykładowe zakładki
tab1, tab2, tab3 = st.tabs(["📚 Aktywna (czerwona)", "💡 Nieaktywna (czarna)", "🎯 Trzecia zakładka"])

with tab1:
    st.write("To jest zawartość pierwszej zakładki")
    st.write("**Tekst tej zakładki powinien być czerwony (aktywna)**")

with tab2:
    st.write("To jest zawartość drugiej zakładki")
    st.write("**Tekst tej zakładki powinien być czarny (nieaktywna)**")

with tab3:
    st.write("To jest zawartość trzeciej zakładki")
    st.write("**Sprawdź kolory nagłówków zakładek powyżej**")

st.markdown("""
---
## 🔍 Analiza kolorów

**Gdzie są definiowane kolory zakładek?**

1. **Streamlit domyślne kolory** - w pliku konfiguracyjnym `.streamlit/config.toml`
2. **CSS customizations** - w plikach CSS lub inline styles
3. **Material3 styles** - w `utils/material3_components.py`

**Aktualne lokalizacje stylów zakładek:**
- `utils/material3_components.py` - linie 312-324
- `views/lesson.py` - linia 261 (style paneli)
""")

# Dodajmy opcje kolorów do testowania
st.markdown("""
<style>
/* Nowe kolory - jasno-srebrne dla nieaktywnych zakładek */
.stTabs [data-baseweb="tab"] {
    color: #c0c0c0 !important; /* Jasno-srebrny dla nieaktywnych */
    text-shadow: 0 0 2px rgba(192, 192, 192, 0.6) !important;
    opacity: 0.8 !important;
}

.stTabs [aria-selected="true"] {
    color: #ffffff !important; /* Biały dla aktywnej */
    text-shadow: 0 0 3px rgba(255, 255, 255, 0.8) !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #e0e0e0 !important; /* Jaśniejszy srebrny przy hover */
    opacity: 1 !important;
}

.stTabs [data-baseweb="tab"]:hover {
    opacity: 1 !important;
}

/* Debug styles - pokaż ramki */
.debug-info {
    background: #f0f0f0;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
}

/* Opcje kolorów do przetestowania */
.color-option {
    display: inline-block;
    margin: 5px;
    padding: 8px 12px;
    border-radius: 4px;
    border: 1px solid #ddd;
    cursor: pointer;
}
</style>

<div class="debug-info">
<strong>🎨 Nowe kolory zakładek - jasno-srebrne:</strong><br>
- <strong>Nieaktywne zakładki (np. "Ekwipunek"):</strong> <span style="color: #c0c0c0; background: #333; padding: 2px 6px; border-radius: 3px;">Jasno-srebrny #c0c0c0</span><br>
- <strong>Aktywna zakładka:</strong> <span style="color: #ffffff; background: #333; padding: 2px 6px; border-radius: 3px;">Biały #ffffff</span><br>
- <strong>Hover efekt:</strong> <span style="color: #e0e0e0; background: #333; padding: 2px 6px; border-radius: 3px;">Srebrny #e0e0e0</span><br>
- <strong>Dodatki:</strong> Text-shadow i opacity dla lepszej czytelności
</div>

## 🎨 Opcje kolorów - maksymalna widoczność:

<div style="margin: 15px 0; background: #2c3e50; padding: 15px; border-radius: 8px;">
<p style="color: #fff; margin-bottom: 10px;"><strong>Tekst z text-shadow dla lepszej widoczności:</strong></p>
<span style="color: #ffffff; text-shadow: 0 0 3px rgba(255, 255, 255, 0.8); margin: 5px; display: inline-block;">Biały z silnym cieniem (aktywna)</span><br>
<span style="color: #ffffff; text-shadow: 0 0 2px rgba(255, 255, 255, 0.6); opacity: 0.7; margin: 5px; display: inline-block;">Biały z cieniem (nieaktywna)</span><br>
<span style="color: #f8f9fa; text-shadow: 0 0 2px rgba(248, 249, 250, 0.8); margin: 5px; display: inline-block;">Prawie biały z cieniem</span><br>
<span style="color: #ffff00; text-shadow: 0 0 2px rgba(255, 255, 0, 0.8); margin: 5px; display: inline-block;">Żółty z cieniem</span><br>
<span style="color: #00ffff; text-shadow: 0 0 2px rgba(0, 255, 255, 0.8); margin: 5px; display: inline-block;">Cyan z cieniem</span><br>
<span style="color: #ff6b6b; text-shadow: 0 0 2px rgba(255, 107, 107, 0.8); margin: 5px; display: inline-block;">Jasny czerwony z cieniem</span>
</div>

<div style="margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 8px;">
<strong>📝 Przykład treści z nowymi kolorami:</strong><br><br>
To jest przykład tekstu treści lekcji z nowym kolorem #495057. Tekst powinien być teraz bardziej czytelny i mniej męczący dla oczu.<br><br>
<span style="color: #6c757d;">A to jest przykład opisu lekcji z kolorem #6c757d - średni szary.</span>
</div>
""", unsafe_allow_html=True)
