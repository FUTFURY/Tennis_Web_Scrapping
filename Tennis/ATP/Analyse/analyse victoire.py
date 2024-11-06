import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv('Tennis/ATP/players_data.csv')

# Nettoyer les données de victoires/défaites cette année
df['Victoires/Défaites (Cette année)'] = df['Victoires/Défaites (Cette année)'].str.extract('(\d+)').astype(float)

# Trier les données par nombre de victoires/défaites cette année
df = df.sort_values(by='Victoires/Défaites (Cette année)', ascending=False)

# Créer le diagramme en lignes
plt.figure(figsize=(12, 6))
plt.plot(df['Nom'], df['Victoires/Défaites (Cette année)'], marker='o', color='skyblue', linestyle='-')
plt.xlabel('Joueur')
plt.ylabel('Nombre de victoires/défaites cette année')
plt.title('Nombre de victoires/défaites des joueurs cette année')
plt.xticks(rotation=90)  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité

# Afficher le diagramme
plt.tight_layout()
plt.show()
