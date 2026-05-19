import streamlit as st

# 🔒 Sécurité licence
if "connecte" not in st.session_state or st.session_state.connecte is False:
    st.error("⛔ Accès refusé. Veuillez activer votre licence.")
    st.stop()

# --- STYLE PREMIUM ---
st.markdown("""
<style>
.hero-title {
    text-align: center;
    font-size: 60px;
    font-weight: 900;
    margin-top: 20px;
}
.hero-sub {
    text-align: center;
    font-size: 22px;
    color: #555;
    margin-bottom: 40px;
}
.big-btn {
    background-color: #4A6CF7;
    color: white;
    padding: 22px 40px;
    border-radius: 12px;
    font-size: 28px;
    font-weight: 700;
    text-align: center;
    display: block;
    margin: auto;
    width: 70%;
    transition: 0.2s;
}
.big-btn:hover {
    background-color: #3a56c9;
    transform: scale(1.03);
}
.pricing-box {
    padding: 25px;
    border-radius: 15px;
    background: #f8f9fc;
    border: 1px solid #e5e7eb;
    text-align: center;
    margin-top: 40px;
}
.price {
    font-size: 48px;
    font-weight: 900;
    color: #4A6CF7;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='hero-title'>🚀 IA Business Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-sub'>Crée des boutiques complètes + publicités IA en un clic.</div>", unsafe_allow_html=True)

# --- GROS BOUTON ---
if st.button("✨ Accéder au Générateur Boutique + Pubs IA", key="go", help="Clique pour ouvrir le module IA"):
    st.switch_page("pages/1_🚀_Boutique_et_Pubs_IA.py")

# --- SECTION ABONNEMENT ---
st.markdown("""
<div class="pricing-box">
    <h2>💳 Abonnement PRO</h2>
    <p class="price">30 $ / mois</p>
    <p>Accès illimité à :</p>
    <ul style="text-align:left; display:inline-block;">
        <li>✔️ Générateur de boutique complet</li>
        <li>✔️ Générateur de publicités IA</li>
        <li>✔️ Analyse IA avancée</li>
        <li>✔️ Export facile</li>
        <li>✔️ Support prioritaire</li>
    </ul>
</div>
""", unsafe_allow_html=True)
