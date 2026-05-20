import streamlit as st
from groq import Groq
import json
import os

if "boutiques" not in st.session_state:
    st.session_state["boutiques"] = []

# Quand la boutique est générée :
st.session_state["boutiques"].append({
    "nom": nom,
    "description": description,
    "style": style,
    "prix": prix,
    "image": image_url
})

with open("boutiques.json", "w") as f:
    json.dump(st.session_state["boutiques"], f)


# 🔒 Sécurité
if "connecte" not in st.session_state or st.session_state.connecte is False:
    st.error("⛔ Accès refusé. Veuillez activer votre licence.")
    st.stop()

st.title("🛒 Générateur Boutique + Pubs IA (PRO)")
if st.button("Générer la boutique"):
    if not nom or not description:
        st.error("Veuillez remplir au moins le nom et la description.")
    else:
        # Appel à ton IA ici
        st.success("Boutique générée avec succès !")


# 🔑 Clé IA
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- FORMULAIRE ---
nom = st.text_input("Nom du produit")
public = st.text_input("Public cible")
benefices = st.text_area("Bénéfices")
ton = st.selectbox("Ton", ["Professionnel", "Amical", "Luxe", "Fun"])

generate = st.button("✨ Générer Boutique + Pubs IA", use_container_width=True)

if generate:
    if not nom or not public or not benefices:
        st.error("Veuillez remplir tous les champs.")
        st.stop()

    with st.spinner("🧠 IA en cours..."):

        # Boutique
        prompt_boutique = f"""
Crée une boutique complète pour :
Produit : {nom}
Public : {public}
Bénéfices : {benefices}
Ton : {ton}
"""

        boutique = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt_boutique}],
            max_tokens=1500
        ).choices[0].message.content

        # Pubs
        prompt_pubs = f"""
Génère un pack publicitaire complet pour :
Produit : {nom}
Public : {public}
Ton : {ton}
"""

        pubs = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt_pubs}],
            max_tokens=1500
        ).choices[0].message.content

    st.subheader("🛍️ Boutique IA")
    st.write(boutique)

    st.subheader("📣 Publicités IA")
    st.write(pubs)

