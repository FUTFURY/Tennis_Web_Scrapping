import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv('Tennis/ATP/players_data.csv')

# Extraire l'année de début professionnel
df['Année de début professionnel'] = df['Année de début professionnel'].astype(str).str[:4]

# Compter le nombre de joueurs pour chaque année de début professionnel
career_start_counts = df['Année de début professionnel'].value_counts().sort_index()

# Créer le graphique à barres
plt.figure(figsize=(10, 6))
plt.bar(career_start_counts.index, career_start_counts.values, color='skyblue')
plt.xlabel('Année de début professionnel')
plt.ylabel('Nombre de joueurs')
plt.title('Nombre de joueurs ayant commencé leur carrière professionnelle chaque année')
plt.xticks(rotation=45)  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité
plt.grid(axis='y')  # Afficher une grille horizontale pour faciliter la lecture

# Afficher le graphique
plt.tight_layout()
plt.show()
