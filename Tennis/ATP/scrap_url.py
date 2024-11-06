from bs4 import BeautifulSoup

# Chemin relatif du fichier HTML contenant la page
file_path = "Tennis/page url joueur.html"

# Ouvrir le fichier HTML contenant la page
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Analyser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Sélectionner toutes les balises <a> contenant les URL des joueurs
player_links = soup.select('table.mega-table.desktop-table.non-live tbody tr td.player.bold.heavy.large-cell ul li.name.center a')

# Liste pour stocker les URL des joueurs
player_urls = []

# Extraire les URL des joueurs et les stocker dans la liste
for link in player_links:
    player_urls.append("https://www.atptour.com" + link.get('href'))

# Afficher les URL des joueurs
for url in player_urls:
    print(url)
