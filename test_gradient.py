import streamlit as st

st.set_page_config(page_title="Test Gradientu", layout="wide")

st.title("Test Gradientowych Kart")

# Test 1: Karta z pełnym HTML
st.subheader("Test 1: Pełne HTML")

card_html = """
<div style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    min-height: 200px;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
">
    <h3 style="margin: 0 0 16px 0; color: white; font-weight: bold;">Testowa karta z gradientem</h3>
    <p style="margin: 0 0 16px 0; color: rgba(255,255,255,0.9); line-height: 1.5;">
        To jest testowa karta z gradientowym tłem. Sprawdzamy czy gradient jest widoczny.
    </p>
    <div style="display: flex; justify-content: space-between; margin: 16px 0; font-size: 12px; color: rgba(255,255,255,0.8);">
        <span>🟢 Poziom podstawowy</span>
        <span>📖 5 min</span>
        <span>👁️ 42 wyświetleń</span>
    </div>
</div>
"""

st.markdown(card_html, unsafe_allow_html=True)

# Test 2: Druga karta z innym gradientem
st.subheader("Test 2: Różowy gradient")

card_html2 = """
<div style="
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px rgba(240, 147, 251, 0.3);
    border: 1px solid rgba(255,255,255,0.2);
    min-height: 200px;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
">
    <h3 style="margin: 0 0 16px 0; color: white; font-weight: bold;">Druga testowa karta</h3>
    <p style="margin: 0 0 16px 0; color: rgba(255,255,255,0.9); line-height: 1.5;">
        To jest druga testowa karta z różowym gradientem. Ten gradient powinien być widoczny na różowo-pomarańczowo.
    </p>
    <div style="display: flex; justify-content: space-between; margin: 16px 0; font-size: 12px; color: rgba(255,255,255,0.8);">
        <span>🟡 Poziom średni</span>
        <span>📖 8 min</span>
        <span>👁️ 128 wyświetleń</span>
    </div>
</div>
"""

st.markdown(card_html2, unsafe_allow_html=True)

# Test 3: Karty w kolumnach
st.subheader("Test 3: Karty w dwóch kolumnach")

col1, col2 = st.columns(2)

with col1:
    st.markdown(card_html, unsafe_allow_html=True)

with col2:
    st.markdown(card_html2, unsafe_allow_html=True)

st.markdown("---")
st.write("Jeśli widzisz kolorowe gradienty powyżej, to znaczy, że CSS działa poprawnie!")
