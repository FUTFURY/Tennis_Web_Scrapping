import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv('Tennis/ATP/players_data.csv')

# Nettoyer et extraire les données d'âge, poids et taille
df['Âge'] = df['Âge'].str.extract('(\d+)').astype(float)
df['Poids'] = df['Poids'].str.extract('(\d+)').astype(float)

# Convertir lbs en kg pour la colonne de poids
df['Poids'] = df['Poids'] * 0.453592  # 1 lbs = 0.453592 kg

# Convertir la taille de pieds et pouces en mètres
height_inches = df['Taille'].str.extract(r"(\d+)'(\d+)").astype(float)  # Extraire les pieds et pouces
df['Taille'] = (height_inches[0] * 12 + height_inches[1]) * 0.0254  # Convertir en mètres

# Créer les graphiques en boîte
plt.figure(figsize=(12, 6))

# Graphique en boîte pour l'âge
plt.subplot(1, 3, 1)
plt.boxplot(df['Âge'].dropna())
plt.title('Distribution de l\'âge des joueurs')
plt.xlabel('Âge')

# Graphique en boîte pour le poids
plt.subplot(1, 3, 2)
plt.boxplot(df['Poids'].dropna())
plt.title('Distribution du poids des joueurs')
plt.xlabel('Poids (kg)')

# Graphique en boîte pour la taille
plt.subplot(1, 3, 3)
plt.boxplot(df['Taille'].dropna())
plt.title('Distribution de la taille des joueurs')
plt.xlabel('Taille (m)')

# Afficher les graphiques
plt.tight_layout()
plt.show()
