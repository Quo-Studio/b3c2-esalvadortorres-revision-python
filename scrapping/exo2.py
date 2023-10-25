import requests
from bs4 import BeautifulSoup

base = "https://www.scrapethissite.com/pages/forms/?page_num="

pages_number = 3

for number in range(1, pages_number + 1):
    url = base + str(number)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        rows = soup.find_all('tr')

        for row in rows[1:]: 
            columns = row.find_all('td')
            if len(columns) >= 3:
                team = columns[0].text.strip()
                year = columns[1].text.strip()
                percentage = columns[2].text.strip()

                # Afficher les données
                print(f"Équipe : {team}, Année : {year}, Pourcentage : {percentage}")

    else:
        print(f"Erreur")

