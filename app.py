import streamlit as st

# -------------------------
# SIMULATION DU PAIEMENT
# -------------------------
if "premium" not in st.session_state:
    st.session_state["premium"] = False

# -------------------------
# SUPPRIMER LA SIDEBAR
# -------------------------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="stSidebarNav"] {display: none;}
[data-testid="stSidebarUserContent"] {display: none;}
</style>
""", unsafe_allow_html=True)

# -------------------------
# POLICE PRO
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
html, body, div, p, h1, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# CONTENU
# -------------------------

st.title("🚀 IA Business Suite")
st.subheader("Crée une boutique complète + un pack publicitaire en un clic.")

st.write("")
st.write("")

# Bouton IA
if st.session_state["premium"]:
    st.page_link("pages/1_Boutique_Pubs.py", label="✨ Lancer le Générateur IA", icon="🚀")
else:
    st.button("🔒 Lancer le Générateur IA (Premium requis)", disabled=True)

st.write("")
st.write("")

# Bouton S'abonner (PayPal)
paypal_url = "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TON_ID_PAYPAL_ICI"

