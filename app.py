import streamlit as st

# -------------------------
# SIMULATION DU PAIEMENT
# -------------------------
# Mets True pour tester l'accès premium
if "premium" not in st.session_state:
    st.session_state["premium"] = False

# -------------------------
# HIDE SIDEBAR
# -------------------------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="stSidebarNav"] {display: none;}
[data-testid="stSidebarUserContent"] {display: none;}
.block-container {padding-top: 0rem;}
</style>
""", unsafe_allow_html=True)

# -------------------------
# POLICE PREMIUM
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap');

html, body, div, span, p, h1, h2, h3, h4, h5, h6, button, label {
    font-family: 'Poppins', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# STYLE GLOBAL
# -------------------------
st.markdown("""
<style>

.hero {
    text-align: center;
    padding-top: 120px;
    padding-bottom: 40px;
}

.hero-title {
    font-size: 60px;
    font-weight: 900;
    color: #111;
}

.hero-sub {
    font-size: 22px;
    color: #555;
    margin-bottom: 50px;
}

.big-btn {
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
    margin-bottom: 40px;
}

.big-btn:hover {
    transform: scale(1.07);
    box-shadow: 0px 12px 28px rgba(74,108,247,0.55);
}

.pricing-box {
    padding: 25px;
    border-radius: 15px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    text-align: center;
    width: 60%;
    margin: auto;
    margin-top: 20px;
}

.price-big {
    font-size: 48px;
    font-weight: 900;
    color: #4A6CF7;
    margin-bottom: 10px;
}

.price-small {
    font-size: 22px;
    font-weight: 600;
    color: #333;
    margin-top: -10px;
}

.footer {
    text-align: center;
    margin-top: 80px;
    color: #999;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------
st.markdown("""
<div class="hero">
    <div class="hero-title">🚀 IA Business Suite</div>
    <div class="hero-sub">Crée une boutique complète + un pack publicitaire en un clic.</div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# BOUTON AVEC VERROU SI NON PAYÉ
# -------------------------
if st.session_state["premium"]:
    st.page_link("pages/1_Boutique_Pubs.py", label="✨ Lancer le Générateur IA", icon="🚀")
else:
    st.button("🔒 Lancer le Générateur IA (Premium requis)", disabled=True)
    st.info("Pour générer une boutique, vous devez activer l'abonnement PRO.")

# -------------------------
# SECTION ABONNEMENT
# -------------------------
st.markdown("""
<div class="pricing-box">
    <h2>💳 Abonnement PRO</h2>

    <div class="price-big">40 $ / mois</div>
    <div class="price-small">+ 10 $ par boutique générée</div>

    <p style="margin-top:20px;">Accès illimité à :</p>
    <ul style="text-align:left; display:inline-block; font-size:18px;">
        <li>✔️ Générateur de boutique complet</li>
        <li>✔️ Générateur de publicités IA</li>
        <li>✔️ Analyse IA avancée</li>
        <li>✔️ Export facile</li>
        <li>✔️ Support prioritaire</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# -------------------------
# FOOTER
# -------------------------
st.markdown("""
<div class="footer">
    © 2026 – IA Business Suite • Propulsé par l’IA
</div>
""", unsafe_allow_html=True)
