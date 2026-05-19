import streamlit as st
# --- HIDE SIDEBAR ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
        [data-testid="stSidebarUserContent"] {
            display: none;
        }
        .block-container {
            padding-top: 0rem;
        }
    </style>
""", unsafe_allow_html=True)


# --- STYLE PREMIUM ---
st.markdown("""
<style>
.hero {
    text-align: center;
    padding-top: 120px;
    padding-bottom: 80px;
}
.hero-title {
    font-size: 60px;
    font-weight: 900;
}
.hero-sub {
    font-size: 22px;
    color: #555;
    margin-bottom: 50px;
}
.big-btn {
    font-size: 30px;
    font-weight: 800;
    padding: 25px 40px;
    border-radius: 14px;
    background: linear-gradient(135deg, #4A6CF7, #6A8BFF);
    color: white;
    text-decoration: none;
    display: inline-block;
    box-shadow: 0px 8px 20px rgba(74,108,247,0.35);
}
.big-btn:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
    <div class="hero-title">🚀 IA Business Suite</div>
    <div class="hero-sub">Crée une boutique complète + un pack publicitaire en un clic.</div>
</div>
""", unsafe_allow_html=True)

# --- GROS BOUTON ---
st.page_link("pages/1_Boutique_Pubs.py", label="✨ Lancer le Générateur IA", icon="🚀")
