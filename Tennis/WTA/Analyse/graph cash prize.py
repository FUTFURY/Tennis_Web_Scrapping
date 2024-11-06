import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données depuis le fichier CSV
data = pd.read_csv("Tennis/WTA/donnees_joueuses.csv")

# Nettoyer la colonne 'Cash prize' en enlevant les virgules et le signe dollar
data['Cash prize'] = data['Cash prize'].replace('[\$,]', '', regex=True).astype(float)

# Calculer le total de matchs (titres + victoires)
data['Total Match'] = data['Titres en simple cette année'] + data['Victoires cette année']

# Calculer le total de matchs par nation
total_matches_per_nation = data.groupby('Origine')['Total Match'].sum().sort_values(ascending=False)

# Sélectionner les 20 premières nations
top_20_nations = total_matches_per_nation.head(20).index

# Filtrer les données pour inclure uniquement les 20 premières nations
data_filtered = data[data['Origine'].isin(top_20_nations)]

# Déterminer la taille des bulles en fonction du nombre de victoires/titres ou du prix en argent
bubble_size = data_filtered['Total Match']  # Modifier en fonction de vos besoins

# Définir une palette de couleurs pour chaque pays
palette = sns.color_palette("tab10", len(top_20_nations))

# Créer le diagramme à bulles
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Cash prize', y='Total Match', size=bubble_size, hue='Origine', palette=palette, sizes=(50, 500), data=data_filtered)
plt.xscale('log')  # Utiliser une échelle logarithmique pour l'axe des abscisses
plt.xlabel('Prix en argent (log)')
plt.ylabel('Total de matchs')
plt.title('Victoires/Titres et prix en argent des joueuses (Top 20 nations)')
plt.legend(title='Origine', bbox_to_anchor=(1.05, 1), loc='upper left')

# Définir les valeurs à afficher sur l'axe des abscisses en dollars
x_ticks = [1000, 3000, 10000, 30000, 100000, 300000, 1000000, 3000000]
x_tick_labels = ['$1k', '', '$10k', '', '$100k', '', '$1M', '$3M']
plt.xticks(x_ticks, x_tick_labels)

plt.tight_layout()
plt.show()
