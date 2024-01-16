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
    #On créé un fichier avec le code html de l'url pour pouvoir faire des verifications
    with open("societe.html", "w", encoding="utf-8") as html_file:
        page_html_text = soup.prettify()
        html_file.write(page_html_text)
    # Supposons que le montant est dans des balises <div> avec la classe 'page-member__resume__number'
    company_capital = soup.find_all('div', class_='page-member__resume__number')
       
    company_activity = soup.find_all('div', class_='wysiwyg mt-16')



    #Si on trouve quelque chose:
    with open(fichier_texte, 'w') as fichier:
        if len(company_capital) > 0:
            # Écrire les liens dans le fichier texte
            #On écrit les trouvailles dans le fichier choisi
            for paragraph in company_capital:
                montant_capital = paragraph.text.strip()  # Supprimer les espaces blancs
                if montant_capital:  # Vérifier si le texte existe
                    fichier.write(montant_capital + '\n')
                    print(f"Écrit dans le fichier : {montant_capital}")
                    break
        if len(company_activity) > 0:
            # Écrire les liens dans le fichier texte
            #On écrit les trouvailles dans le fichier choisi
            for paragraph in company_activity:
                activity = paragraph.text.strip()  # Supprimer les espaces blancs
                if activity:  # Vérifier si le texte existe
                    fichier.write(activity + '\n')
                    print(f"Écrit dans le fichier : {activity}")
                    break
else:
    print(f"Échec de la requête avec le code d'état {response.status_code}")


