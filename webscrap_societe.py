import requests
from bs4 import BeautifulSoup
import time

#LIRE LE README Avant de lancer !

#On récupère la liste des entreprises
url_list = []
fichier_lien="liens_annuaire.txt"
with open(fichier_lien,'r', encoding="utf-8") as liens:
    for ligne in liens:
        # Ajouter la ligne à la liste (en retirant le saut de ligne avec .strip())
        url_list.append(ligne.strip())

#pour pas tout afficher
url_test_list=url_list[:50]


# On stocke dans ce fichier les infos : N°,lien,nom,Tel,activité, capital, email
fichier_texte = "infos_entreprises.txt"
numero_entreprise=0
with open(fichier_texte, 'w',encoding="utf-8") as fichier:
    #on parcoure les pages une à une 
    for url in url_test_list:
        numero_entreprise+=1
        num=str(numero_entreprise)
        fichier.write('\n___________________________________________________________________________\n\n')
        fichier.write(f"Entreprise numéro {num} : ")
        # Faire la requête HTTP
        response = requests.get(url)

        if response.status_code == 200:
            # Analyser le HTML avec BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # #On créé un fichier avec le code html de l'url pour pouvoir faire des verifications
            # with open("societe.html", "w", encoding="utf-8") as html_file:
            #     page_html_text = soup.prettify()
            #     html_file.write(page_html_text)
            # #Supposons que le montant est dans des balises <div> avec la classe 'page-member__resume__number'
            company_name = soup.find_all('h1', class_='title-main title-main--white uppercase')

            company_resume=soup.find_all('div', class_='page-member__resume__pres wysiwyg')
           
            company_capital = soup.find_all('div', class_='page-member__resume__number')

            company_activity = soup.find_all('div', class_='wysiwyg mt-16')

            company_email=soup.find_all('a', class_='gen-text gen-text--L gen-text--blue-dark')

            company_number=soup.find_all('span', class_='gen-text gen-text--L gen-text--blue-dark')

            #Si on trouve quelque chose:
            if len(company_name) > 0:
                # Écrire les liens dans le fichier texte
                #On écrit les trouvailles dans le fichier choisi
                for paragraph in company_name:
                    name = paragraph.text.strip()  # Supprimer les espaces blancs
                    if name:  # Vérifier si le texte existe
                        fichier.write(name + '\n')
                        print(f"Écriture des données de : {name}")
                        break
                    else:
                        fichier.write(url + '\n')
                    print(f"Écrit dans le fichier : {url}")
            if len(company_resume) > 0:
                for paragraph in company_resume:
                    resume = paragraph.text.strip()
                    if resume:
                        fichier.write(f"Présentation : {resume}\n")
                        break
            if len(company_capital) > 0:
                for paragraph in company_capital:
                    montant_capital = paragraph.text.strip()
                    if montant_capital:
                        fichier.write(f"Capital : {montant_capital}\n")
                        break
            if len(company_activity) > 0:
                for paragraph in company_activity:
                    activity = paragraph.text.strip()
                    if activity:
                        fichier.write(f"Activité : {activity}\n\n")
                        break

            if len(company_email) > 0:
                for balise_a in company_email:
                    href = balise_a.get('href')
                    fichier.write(f"E{href}\n")

            if len(company_number) > 0:
                for paragraph in company_number:
                    number = paragraph.text.strip() 
                    if number:
                        fichier.write(f"Tel : {number}\n")
                        break
        else:
            print(f"Échec de la requête avec le code d'état {response.status_code}")
        time.sleep(0.001)
    fichier.write('\n___________________________________________________________________________\n\n')
fichier.close()

