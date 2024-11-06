import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv("Tennis/WTA/donnees_joueuses.csv")

# Compter le nombre de redondance pour chaque préférence de main
counts = data["Préférence de main"].value_counts()

# Créer un histogramme
plt.bar(counts.index, counts.values)

# Ajouter des étiquettes et un titre
plt.xlabel("Préférence de main")
plt.ylabel("Nombre de joueuses")
plt.title("Répartition des préférences de main des joueuses")

# Afficher l'histogramme
plt.show()
