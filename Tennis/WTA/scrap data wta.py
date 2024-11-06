import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Fonction pour ouvrir les liens des joueurs avec Selenium et scraper les informations
def scraper_informations_joueuses(player_urls):
    # Initialiser le navigateur Chrome
    driver = webdriver.Chrome()

    # Ouvrir le fichier CSV pour enregistrer les données
    with open('donnees_joueuses.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Nom', 'Date de naissance', 'Age', 'Taille', 'Préférence de main', 'Origine', 'Classement', 'Cash prize', 'Titres en simple cette année', 'Victoires cette année'] 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Boucle à travers les trois premiers liens et scraper les informations
        for url in player_urls[:100]:
            driver.get(url)

            # Attendre 2 secondes entre chaque chargement de page
            time.sleep(2)
            
            # Attendre que la page se charge
            driver.implicitly_wait(10)

            # Initialiser un dictionnaire pour stocker les données de la joueuse
            player_data = {}

            # Scraper le nom de la joueuse
            try:
                nom_joueuse_element = driver.find_element(By.CLASS_NAME, "profile-header__name")
                player_data['Nom'] = nom_joueuse_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping du nom de la joueuse:", e)

            # Scraper l'âge et la date de naissance
            try:
                age_element = driver.find_element(By.CSS_SELECTOR, ".js-profile-header-info__age")
                player_data['Date de naissance'] = age_element.get_attribute("data-dob")
                player_data['Age'] = age_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping de l'âge et de la date de naissance:", e)

            # Scraper la taille
            try:
                taille_element = driver.find_element(By.CSS_SELECTOR, ".profile-header-info__detail-stat--small")
                player_data['Taille'] = taille_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping de la taille:", e)

            # Scraper la préférence de main
            try:
                main_element = driver.find_element(By.XPATH, "//div[contains(text(),'Right-Handed') or contains(text(),'Left-Handed')]")
                player_data['Préférence de main'] = main_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping de la préférence de main:", e)

            # Scraper l'origine
            try:
                origine_element = driver.find_element(By.XPATH, "//div[contains(@class,'profile-header-info__detail') and div[contains(text(),'Birthplace')]]/div[@class='profile-header-info__detail-stat--small']")
                player_data['Origine'] = origine_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping de l'origine:", e)
            
            # Scraper le classement
            try:
                ranking_element = driver.find_element(By.CSS_SELECTOR, ".profile-header-image-col__rank-pos")
                player_data['Classement'] = ranking_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping du classement:", e)

            # Scraper le cash prize
            try:
                cash_prize_element = driver.find_element(By.CSS_SELECTOR, ".profile-header-stats__value[data-single][data-prefix]")
                player_data['Cash prize'] = cash_prize_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping du cash prize:", e)
            
            
            # Scraper les titre en simple cette année
            try:
                xpath = "/html/body/div/main/div/div/div/div[1]/div[1]/div[1]/div[2]/div[2]"
                singles_wins_this_year_element = driver.find_element(By.XPATH, xpath)
                player_data['Titres en simple cette année'] = singles_wins_this_year_element.text.strip()
            except Exception as e:
                print("Une erreur s'est produite lors du scraping des victoires en simple cette année:", e)
                
            # Scraper les victoires cette année
            try:
                losses_element = driver.find_element(By.CSS_SELECTOR, "span.js-profile-header-stat-count-up")
                losses_count = losses_element.get_attribute("data-single")
                player_data['Victoires cette année'] = losses_count
            except Exception as e:
                print("Une erreur s'est produite lors du scraping des victoires:", e)
            
            # Écrire les données dans le fichier CSV
            writer.writerow(player_data)

            # Afficher un message indiquant que les données de la joueuse ont été enregistrées
            print(f"Les données de la joueuse {player_data['Nom']} ont été enregistrées avec succès.")

    # Fermer le navigateur
    driver.quit()

# Lire les URLs des joueurs à partir du fichier CSV
def lire_urls_de_csv(filename):
    player_urls = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_urls.append(row['URL'])
    return player_urls

# Nom du fichier CSV contenant les URLs des joueurs
filename = 'Tennis/WTA/url_wta.csv'

# Obtenir la liste des URLs des joueuses à partir du fichier CSV
player_urls = lire_urls_de_csv(filename)

# Appeler la fonction pour ouvrir les liens des joueurs et scraper les informations
scraper_informations_joueuses(player_urls)
