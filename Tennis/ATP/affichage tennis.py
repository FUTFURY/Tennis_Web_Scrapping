import os
import time
import random
import csv
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Définir le chemin du chromedriver
chromedriver_path = "/Users/melvinalgane/Desktop/El Omari_Algane/Tennis/chromedriver"

# Définir le chemin du chromedriver dans la variable PATH
os.environ['PATH'] += ":" + chromedriver_path

# Importer la liste des URL des joueurs depuis scrap_url.py (chemin relatif)
from scrap_url import player_urls

# Fonction pour tester la validité des proxies
def test_proxy(proxy_url):
    url = "https://httpbin.org/ip"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

try:
    # Sélectionnez les proxies valides
    response = requests.get("https://free-proxy-list.net/")
    proxy_list = pd.read_html(response.text)[0]
    proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)
    https_proxies = proxy_list[proxy_list["Https"] == "yes"]
    good_proxies = []
    for proxy_url in https_proxies["url"]:
        if test_proxy(proxy_url):
            good_proxies.append(proxy_url)
            if len(good_proxies) >= 3:
                break

    # Ouvrir le fichier CSV en mode écriture
    with open('players_data.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Écrire les en-têtes
        writer.writerow(['Nom', 'Classement ATP', 'Victoires/Défaites (Carrière)', 'Prix en argent', 'Pays', 'Âge', 'Poids', 'Taille', 'Année de début professionnel', 'Victoires/Défaites (Cette année)'])

        # Initialisation du navigateur avec les options
        options = webdriver.ChromeOptions()

        # Boucle sur chaque URL de joueur
        for index, url in enumerate(player_urls[:100]):
            success = False
            # Rotation de proxy lors du scraping avec Selenium
            for proxy_url in good_proxies:
                proxy = proxy_url.replace("http://", "")

                try:
                    # Initialisation du navigateur avec les options
                    options = webdriver.ChromeOptions()
                    # Ajouter le proxy au navigateur
                    options.add_argument(f'--proxy-server={proxy}')
                    # Initialisation du navigateur avec les options
                    driver = webdriver.Chrome(options=options)

                    # Charger la page de l'URL du joueur
                    driver.get(url)

                    # Attendre 2 secondes entre chaque chargement de page
                    time.sleep(2)

                    # Récupérer les données du joueur
                    player_name_element = driver.find_element(By.CSS_SELECTOR, 'div.player_name > span')
                    player_name = player_name_element.text
                    print(f"Données récupérées pour le joueur {player_name}")

                    ranking_element = driver.find_element(By.CSS_SELECTOR, 'div.atp_player-stats > div.stats-content > div:nth-child(1) > div.stat')
                    ranking = ranking_element.text

                    wins_losses_element = driver.find_element(By.CSS_SELECTOR, 'div.atp_player-stats > div.stats-content > div:nth-child(2) > div.wins')
                    wins_losses = wins_losses_element.text

                    prize_money_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.prize_money'))
                    )
                    prize_money = prize_money_element.text

                    country_element = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_right > li:nth-child(1) > span.flag')
                    country = country_element.text

                    age_element = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_left > li:nth-child(1) > span:nth-child(2)')
                    age = age_element.text

                    weight_element = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_left > li:nth-child(2) > span:nth-child(2)')
                    weight = weight_element.text

                    height_element = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_left > li:nth-child(3) > span:nth-child(2)')
                    height = height_element.text

                    pro_debut_element = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div.atp_layout > div > div.atp_layout-content > div.atp_player-personaldetails > div > div > ul.pd_left > li:nth-child(4) > span:nth-child(2)')
                    pro_debut = pro_debut_element.text

                    current_year_wins_losses_element = driver.find_element(By.CSS_SELECTOR, 'body > div.atp_player-profile-header > div > div > div.player_profile > div.atp_player-stats > div.stats-content > div:nth-child(1) > div.wins')
                    current_year_wins_losses = current_year_wins_losses_element.text

                    # Écrire les données dans le fichier CSV
                    writer.writerow([player_name, ranking, wins_losses, prize_money, country, age, weight, height, pro_debut, current_year_wins_losses])

                    # Fermer le navigateur
                    driver.quit()

                    # Si tout se passe bien sans erreur, marquer le succès
                    success = True
                    break  # Sortir de la boucle de rotation des proxies si une page est correctement traitée

                except Exception as e:
                    print(f"Une erreur s'est produite: {str(e)}")
                    # Fermer le navigateur en cas d'erreur
                    driver.quit()

                if success:
                    break  # Sortir de la boucle principale si une page est correctement traitée

            if not success:
                print("Aucun proxy disponible n'a fonctionné pour cette URL.")

# Si aucun proxy n'a fonctionné
except Exception as e:
    print(f"Une erreur s'est produite: {str(e)}")
finally:
    # Fermer le navigateur
    driver.quit()
