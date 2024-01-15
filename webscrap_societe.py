import requests
from bs4 import BeautifulSoup
import time
# URL de la page contenant les informations des entreprises
url = "https://www.gifas.fr/membre/4cad-group"

# Fichier texte dans lequel tu veux enregistrer les liens
fichier_texte = "infos_entreprises.txt"

# Faire la requête HTTP
response = requests.get(url)

if response.status_code == 200:
  
    # Analyser le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Supposons que le montant est dans des balises <div> avec la classe 'page-member__resume__number'
    company_paragraphs = soup.find_all('div', class_='page-member__resume__number')
    
    #On créé un fichier avec le code html de l'url pour pouvoir faire des verifications
    with open("societe.html", "w", encoding="utf-8") as html_file:
        page_html_text = soup.prettify()
        html_file.write(page_html_text)

    #Si on trouve quelque chose:
    if len(company_paragraphs) > 0:
        # Écrire les liens dans le fichier texte
        with open(fichier_texte, 'w') as fichier:#On écrit les trouvailles dans le fichier choisi
            for paragraph in company_paragraphs:
                montant_capital = paragraph.text.strip()  # Supprimer les espaces blancs
                if montant_capital:  # Vérifier si le texte existe
                    fichier.write(montant_capital + '\n')
                    print(f"Écrit dans le fichier : {montant_capital}")
                    break
        print("Opération terminée. Les liens ont été enregistrés dans le fichier texte.")
    else:
        print("Aucun lien trouvé sur la page.")

else:
    print(f"Échec de la requête avec le code d'état {response.status_code}")


