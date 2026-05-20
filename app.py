import streamlit as st
# Détection du code secret dans l'URL
params = st.query_params
if "code" in params and params["code"] == "ABONNE2024":
    st.session_state["premium"] = True


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

# Bouton IA
if st.session_state["premium"]:
    st.page_link("pages/1_Boutique_Pubs.py", label="✨ Lancer le Générateur IA", icon="🚀")
else:
    st.button("🔒 Lancer le Générateur IA (Premium requis)", disabled=True)

st.write("")

# Bouton S'abonner (PayPal)
paypal_url = "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TON_ID_PAYPAL_ICI"

st.markdown(f"### 👉 [💳 S’abonner maintenant]({paypal_url})")

st.write("---")

# Section abonnement
st.header("💳 Abonnement PRO")

st.write("### **50 $ / mois**")

st.write("""
Avec l’abonnement PRO, vous obtenez :

- Générateur de boutique complet  
- Générateur de publicités IA  
- Analyse IA avancée  
- Export facile  
- Support prioritaire  
""")


