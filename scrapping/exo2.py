import requests
from bs4 import BeautifulSoup
import csv

base = "https://www.scrapethissite.com/pages/forms/?page_num="

pages_number = 10

with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Équipe', 'Année', 'Pourcentage'])

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
                    wins = columns[2].text.strip()
                    losses = columns[3].text.strip()
                    percentage = columns[5].text.strip()
                    gf = columns[6].text.strip()
                    ga = columns[7].text.strip()
                    ratio = columns[8].text.strip()

                    if wins > losses:
                        writer.writerow([team, year, wins, losses,percentage, gf, ga, ratio])
        else:
            print("Erreur")



