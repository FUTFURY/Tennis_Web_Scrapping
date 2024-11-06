import requests

url = "https://www.atptour.com/en/rankings/singles"

# Définir les en-têtes pour simuler un navigateur Web
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/"
}

# Envoyer une requête GET pour obtenir le contenu de la page
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi (statut de réponse 200)
if response.status_code == 200:
    # Nom du fichier dans lequel nous allons enregistrer la page HTML
    filename = "page url joueur.html"

    # Écrire le contenu de la réponse dans un fichier
    with open(filename, "w", encoding="utf-8") as file:
        file.write(response.text)

    print("Page HTML enregistrée avec succès sous le nom:", filename)
else:
    print("Erreur lors de la récupération de la page. Statut de réponse:", response.status_code)
