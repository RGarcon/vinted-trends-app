import streamlit as st
from pyVinted import Vinted
import pandas as pd

# Initialisation de l'API
vinted = Vinted()

# Mapping simple pour associer un mot-clé à une URL Vinted
URLS = {
"hommes": "https://www.vinted.fr/vetements?catalog[]=5", # Vêtements hommes
"femmes": "https://www.vinted.fr/vetements?catalog[]=1904", # Vêtements femmes
"chaussures": "https://www.vinted.fr/chaussures", # Toutes chaussures
"accessoires": "https://www.vinted.fr/accessoires" # Accessoires mode
}

# Interface
st.title("🔥 Tendances Vinted en Direct")

category = st.selectbox("Choisis une catégorie :", list(URLS.keys()))

if st.button("📊 Voir les tendances"):
with st.spinner("Chargement des articles..."):
articles = vinted.items.search(URLS[category], 20, 1) # max 20 articles
if not articles:
st.warning("Aucun article trouvé. Essaie une autre catégorie.")
else:
# Mise en forme DataFrame
df = pd.DataFrame([{
"Titre": a.title,
"Prix": f"{a.price} €",
"Marque": a.brand_title or "N/A",
"Lien": a.url
} for a in articles])

st.dataframe(df)

# Bouton pour téléchargement CSV
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Télécharger les résultats", csv, f"{category}_vinted.csv", "text/csv")
