import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 🔹 Fonction pour récupérer les tendances sur Vinted
def get_vinted_trends(category="hommes"):
    url = f"https://www.vinted.fr/catalog?search_text=&order=relevance&catalog[]={category}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("div", class_="feed-grid__item")
    data = []

    for item in items[:10]:  
        try:
            title = item.find("a", class_="ItemBox_title").text.strip()
            price = item.find("span", class_="ItemBox_price").text.strip()
            link = "https://www.vinted.fr" + item.find("a", class_="ItemBox_title")["href"]
            data.append({"Titre": title, "Prix": price, "Lien": link})
        except AttributeError:
            continue

    return pd.DataFrame(data)

# 🎨 Interface Streamlit
st.title("🔥 Tendances Vinted en Direct")

# Sélecteur de catégorie
category = st.selectbox("Choisis une catégorie :", ["hommes", "femmes", "chaussures", "accessoires"])

# Bouton de mise à jour
if st.button("📊 Voir les tendances"):
    with st.spinner("Chargement..."):
        df = get_vinted_trends(category)
        st.dataframe(df)  # Affiche le tableau avec les tendances

        # 📥 Lien de téléchargement CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Télécharger les tendances", csv, "vinted_trends.csv", "text/csv")
