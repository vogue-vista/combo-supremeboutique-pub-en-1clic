import streamlit as st
from groq import Groq

# 🔒 Sécurité licence
if "connecte" not in st.session_state or st.session_state.connecte is False:
    st.error("⛔ Accès refusé. Veuillez activer votre licence.")
    st.stop()

st.title("🛒 Générateur Boutique + Pubs IA (PRO)")

# 🔑 Clé IA sécurisée
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except:
    st.error("❌ Clé GROQ_API_KEY manquante dans les secrets Streamlit.")
    st.stop()

# --- FORMULAIRE ---
st.subheader("🧩 Informations sur le produit")

nom_produit = st.text_input("Nom du produit")
public_cible = st.text_input("Public cible")
benefices = st.text_area("Bénéfices du produit")
ton = st.selectbox("Ton de la marque", ["Professionnel", "Amical", "Luxe", "Fun", "Émotionnel"])

st.markdown("---")

# --- GROS BOUTON ---
generate = st.button("✨ Générer Boutique + Pubs IA", use_container_width=True)

if generate:
    if not nom_produit or not public_cible or not benefices:
        st.error("Veuillez remplir tous les champs obligatoires.")
        st.stop()

    with st.spinner("🧠 Génération IA en cours..."):

        # --- PROMPT BOUTIQUE ---
        prompt_boutique = f"""
Crée une boutique complète pour le produit suivant :

Nom : {nom_produit}
Public cible : {public_cible}
Bénéfices : {benefices}
Ton : {ton}

Structure demandée :
- Page d'accueil
- Page produit
- À propos
- FAQ
- Politique de retour
"""

        boutique = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt_boutique}],
            temperature=0.6,
            max_tokens=1500
        ).choices[0].message.content

        # --- PROMPT PUBS ---
        prompt_pubs = f"""
Génère un pack publicitaire complet pour :

Produit : {nom_produit}
Public cible : {public_cible}
Ton : {ton}

Inclure :
- Hooks TikTok
- Scripts UGC
- Textes Facebook Ads
- Titres Google Ads
- Descriptions Google Ads
"""

        pubs = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt_pubs}],
            temperature=0.7,
            max_tokens=1500
        ).choices[0].message.content

    # --- AFFICHAGE ---
    st.subheader("🛍️ Boutique IA générée")
    st.write(boutique)

    st.markdown("---")

    st.subheader("📣 Pack Publicitaire IA généré")
    st.write(pubs)
