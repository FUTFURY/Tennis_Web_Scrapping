import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
df = pd.read_csv('Tennis/ATP/players_data.csv')

# Compter le nombre de joueurs par pays
player_counts = df['Pays'].value_counts()

# Sélectionner les 15 plus grandes nations
top_15_countries = player_counts.head(15)

# Créer le diagramme circulaire
plt.figure(figsize=(8, 8))
plt.pie(top_15_countries, labels=top_15_countries.index, autopct='%1.1f%%', startangle=140)
plt.title('Répartition des joueurs par pays dans le top 100 mondial de tennis (Top 15 nations)')

# Afficher le diagramme
plt.axis('equal')  # Assurer que le diagramme est un cercle
plt.show()
