from pyVinted import Vinted
import pandas as pd

vinted = Vinted()

URLS = {
    "hommes": "https://www.vinted.fr/vetements?catalog[]=5",
    "femmes": "https://www.vinted.fr/vetements?catalog[]=1904",
    "chaussures": "https://www.vinted.fr/chaussures",
    "accessoires": "https://www.vinted.fr/accessoires"
}

for category, url in URLS.items():
    print(f"Récupération pour {category}...")
    articles = vinted.items.search(url, 50, 1)  # récupère 50 articles max
    data = [{
        "Titre": a.title,
        "Prix": f"{a.price} €",
        "Marque": a.brand_title or "N/A",
        "Lien": a.url
    } for a in articles]

    df = pd.DataFrame(data)
    df.to_csv(f"trends_{category}.csv", index=False)
    print(f"{category} → {len(df)} articles enregistrés.")
