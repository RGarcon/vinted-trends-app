import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tendances Vinted", layout="wide")

st.title("🔥 Tendances du moment sur Vinted")
st.markdown("Voici les articles les plus populaires cette semaine par catégorie. Parfait pour l'achat-revente ou vider son dressing !")

categories = {
    "hommes": "trends_hommes.csv",
    "femmes": "trends_femmes.csv",
    "chaussures": "trends_chaussures.csv",
    "accessoires": "trends_accessoires.csv"
}

choix = st.selectbox("Choisis une catégorie :", list(categories.keys()))

try:
    df = pd.read_csv(categories[choix])
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Télécharger les données", csv, f"{choix}_vinted.csv", "text/csv")
except FileNotFoundError:
    st.warning("Pas encore de données dispo. Lance le script en local pour récupérer les tendances.")
