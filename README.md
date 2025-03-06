# 🎾 Tennis Data Scraper – Analyse des joueurs ATP & WTA  

Ce projet permet de scraper et analyser les données des joueurs ATP et WTA en utilisant **Python et Selenium**. Il collecte des informations sur les joueurs, telles que leur classement, statistiques et caractéristiques physiques, et génère des visualisations pour mieux comprendre les tendances du tennis professionnel.

## 📂 Structure du projet  

```
📂 Tennis
 ├── 📂 ATP                # Données et scripts liés à l'ATP
 │   ├── __pycache__       
 │   ├── affichage_tennis.py  # Affichage des résultats et graphiques
 │   ├── Analyse             # Dossier pour l'analyse des données
 │   ├── collect_url_joueur.py  # Collecte des URLs des joueurs
 │   ├── page_url_joueur.html   # Exemple de page collectée
 │   ├── players_data.csv       # Données des joueurs collectées
 │   ├── scrap_url.py           # Script principal de scraping
 │
 ├── 📂 WTA                # Dossier similaire pour les joueuses WTA
 ├── chromedriver          # Exécutable pour Selenium
```

## 🚀 Installation et exécution  

### Prérequis  
- Python 3.12  
- Google Chrome + **ChromeDriver** (placé dans le dossier principal)  
- Bibliothèques Python nécessaires (voir `requirements.txt`)  

### Installation  
```bash
git clone https://github.com/FUTFURY/Tennis_Web_Scrapping.git
cd Tennis_Web_Scrapping
pip install -r requirements.txt
```

### Exécution du scraping  
```bash
python ATP/scrap_url.py
```

### Visualisation des données  
```bash
python ATP/affichage_tennis.py
```

## 🔧 Fonctionnalités  
- 🏆 **Scraping** des joueurs ATP et WTA  
- 📊 **Analyse des données collectées** (classement, âge, taille, poids...)  
- 📈 **Génération de graphiques** pour explorer les tendances  

## 📄 Licence  
Ce projet est sous licence MIT.
