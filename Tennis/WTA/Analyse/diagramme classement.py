import csv
import matplotlib.pyplot as plt

# Fonction pour lire les données du fichier CSV
def lire_donnees_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Fonction pour compter le nombre de joueurs par pays
def compter_joueurs_par_pays(data):
    pays_counts = {}
    for joueur in data:
        origine = joueur['Origine']
        if origine in pays_counts:
            pays_counts[origine] += 1
        else:
            pays_counts[origine] = 1
    return pays_counts

# Fonction pour créer le diagramme circulaire
def diagramme_circulaire(pays_counts):
    sorted_pays_counts = dict(sorted(pays_counts.items(), key=lambda item: item[1], reverse=True))
    top_15_pays_counts = dict(list(sorted_pays_counts.items())[:15])

    labels = list(top_15_pays_counts.keys())
    counts = list(top_15_pays_counts.values())

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Répartition des joueurs par pays dans le top 100 (Top 15)')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# Chemin relatif du fichier CSV contenant les données des joueurs
filename = 'Tennis/WTA/donnees_joueuses.csv'

# Lire les données du fichier CSV
data = lire_donnees_csv(filename)

# Compter le nombre de joueurs par pays
pays_counts = compter_joueurs_par_pays(data)

# Créer le diagramme circulaire
diagramme_circulaire(pays_counts)
