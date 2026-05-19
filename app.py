import streamlit as st

# 🔒 Sécurité licence
if "connecte" not in st.session_state or st.session_state.connecte is False:
    st.error("⛔ Accès refusé. Veuillez activer votre licence.")
    st.stop()

# --- STYLE PREMIUM ---
st.markdown("""
<style>

body {
    background-color: #ffffff;
}

.hero-container {
    text-align: center;
    padding-top: 120px;
    padding-bottom: 80px;
}

.hero-title {
    font-size: 64px;
    font-weight: 900;
    color: #111;
    margin-bottom: 10px;
}

.hero-sub {
    font-size: 22px;
    color: #555;
    margin-bottom: 50px;
}

.big-button {
    background: linear-gradient(135deg, #4A6CF7, #6A8BFF);
    color: white;
    padding: 28px 50px;
    border-radius: 14px;
    font-size: 30px;
    font-weight: 800;
    text-decoration: none;
    display: inline-block;
    transition: 0.25s;
    box-shadow: 0px 8px 20px rgba(74,108,247,0.35);
}

.big-button:hover {
    transform: scale(1.05);
    box-shadow: 0px 12px 28px rgba(74,108,247,0.55);
}

.footer {
    text-align: center;
    margin-top: 120px;
    color: #999;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🚀 IA Business Suite</div>
    <div class="hero-sub">Génère une boutique complète + un pack publicitaire en un seul clic.</div>
</div>
""", unsafe_allow_html=True)

# --- GROS BOUTON ---
clicked = st.button("✨ Lancer le Générateur IA", key="cta", use_container_width=False)

if clicked:
    st.switch_page("pages/1_🚀_Boutique_et_Pubs_IA.py")

# --- FOOTER ---
st.markdown("""
<div class="footer">
    © 2026 – IA Business Suite • Propulsé par l’IA
</div>
""", unsafe_allow_html=True)

