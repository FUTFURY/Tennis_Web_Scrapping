from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Initialiser le navigateur Chrome
driver = webdriver.Chrome()

url = "https://www.wtatennis.com/rankings/singles"

# Accéder à l'URL
driver.get(url)

# Attendre que les éléments de lien des joueurs soient présents dans le DOM
wait = WebDriverWait(driver, 10)

# Effectuer cinq clics sur le bouton de chargement
for _ in range(5):
    try:
        load_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/section/div[3]/button[1]")))
        load_more_button.click()
        # Attendre 2 secondes après chaque clic pour laisser le temps à la page de charger
        time.sleep(2)
    except:
        break

# Initialiser une liste pour stocker les URLs des joueurs
player_urls = []

# Trouver tous les éléments de lien des joueurs
player_elements = driver.find_elements(By.XPATH, "//td[@class='rankings__cell']/a")

# Ajouter les URLs des joueurs à la liste
for element in player_elements:
    player_url = element.get_attribute('href')
    player_urls.append(player_url)

# Fermer le navigateur
driver.quit()

# Enregistrer les URLs des joueurs dans un fichier CSV
with open('url_wta.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for url in player_urls:
        writer.writerow({'URL': url})

print("Les URLs des joueurs ont été enregistrées dans le fichier 'url_wta.csv'.")
