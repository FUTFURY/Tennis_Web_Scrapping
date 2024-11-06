import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données depuis le fichier CSV
df = pd.read_csv('Tennis/ATP/players_data.csv')

# Nettoyer les données de victoires/défaites et de prix en argent
df['Victoires/Défaites (Cette année)'] = df['Victoires/Défaites (Cette année)'].str.extract('(\d+)').astype(int)

# Extraire et nettoyer les valeurs numériques de la colonne 'Prix en argent'
df['Prix en argent'] = df['Prix en argent'].replace('[\$,]', '', regex=True)  # Supprimer les symboles de devise
df['Prix en argent'] = df['Prix en argent'].str.extract('(\d+)').astype(float)  # Extraire les valeurs numériques

# Sélectionner les 10 pays les plus importants
top_countries = df['Pays'].value_counts().nlargest(10).index

# Créer une palette de 10 couleurs différentes
palette = sns.color_palette("husl", 10)

# Créer un dictionnaire de correspondance entre les pays et les couleurs
colors = {country: palette[i] for i, country in enumerate(top_countries)}

# Créer le diagramme à bulles
plt.figure(figsize=(12, 8))
for country, group in df.groupby('Pays'):
    if country in top_countries:
        plt.scatter(group['Victoires/Défaites (Cette année)'], group['Prix en argent'], s=group['Victoires/Défaites (Cette année)']*20,
                    c=[colors[country]], label=None, alpha=0.7)
        # Ajouter des annotations pour les pays
        for i, txt in enumerate(group['Nom']):
            plt.annotate(txt, (group['Victoires/Défaites (Cette année)'].iloc[i], group['Prix en argent'].iloc[i]), fontsize=8)

# Ajouter une légende
for country, color in colors.items():
    plt.scatter([], [], color=color, label=country)  # Points factices pour créer une légende
plt.legend(title='Pays')

# Ajouter des labels et un titre
plt.xlabel('Nombre de victoires/défaites cette année')
plt.ylabel('Prix en argent ($)')
plt.title('Performance des joueurs de tennis par pays')

# Afficher le diagramme
plt.grid(True)
plt.tight_layout()
plt.show()
