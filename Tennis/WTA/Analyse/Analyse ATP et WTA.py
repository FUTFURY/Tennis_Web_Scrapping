import pandas as pd
import matplotlib.pyplot as plt

def extract_age(age_str):
    # Si la valeur est une chaîne de caractères, extraire le premier nombre
    if isinstance(age_str, str):
        # Séparer la chaîne par des espaces et récupérer le premier nombre
        age = int(age_str.split()[0])
        return age
    else:
        # Sinon, la valeur est déjà un entier, laisser inchangée
        return age_str

def analyse_players_data(atp_file, wta_file):
    # Lecture des fichiers CSV
    atp_df = pd.read_csv(atp_file)
    wta_df = pd.read_csv(wta_file)

    # Extraction de l'âge
    atp_df["Âge"] = atp_df["Âge"].apply(extract_age)
    wta_df["Age"] = wta_df["Age"].apply(extract_age)

    # Calcul des statistiques
    atp_mean_age = atp_df["Âge"].mean()
    wta_mean_age = wta_df["Age"].mean()

    # Nettoyage de la colonne "Classement ATP" pour ATP
    atp_df["Classement ATP"] = atp_df["Classement ATP"].str.extract(r'(\d+)').astype(float)
    atp_mean_ranking = atp_df["Classement ATP"].mean()

    # Nettoyage de la colonne "Classement" pour WTA
    wta_df["Classement"] = wta_df["Classement"].astype(str).str.extract(r'(\d+)').astype(float)

    # Répartition des nationalités (limiter aux 15 premières)
    atp_country_counts = atp_df["Pays"].value_counts().head(15)
    wta_country_counts = wta_df["Origine"].value_counts().head(15)

    # Création des graphiques
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Graphique 1 : Comparaison des âges moyens
    axs[0, 0].bar(["ATP", "WTA"], [atp_mean_age, wta_mean_age])
    axs[0, 0].set_title("Âge moyen des joueurs/joueuses")
    axs[0, 0].set_ylabel("Âge moyen")

    # Graphique 2 : Répartition des nationalités (ATP)
    axs[0, 1].pie(atp_country_counts, labels=atp_country_counts.index, autopct='%1.1f%%')
    axs[0, 1].set_title("Répartition des nationalités (ATP)")

    # Graphique 3 : Répartition des nationalités (WTA)
    axs[1, 0].pie(wta_country_counts, labels=wta_country_counts.index, autopct='%1.1f%%')
    axs[1, 0].set_title("Répartition des nationalités (WTA)")

    plt.tight_layout()
    plt.show()

# Chemins vers les fichiers CSV
atp_file_path = "Tennis/ATP/players_data.csv"
wta_file_path = "Tennis/WTA/donnees_joueuses.csv"

# Appel de la fonction d'analyse
analyse_players_data(atp_file_path, wta_file_path)
