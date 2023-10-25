import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find(id='countries')


rows = table.find_all("div", class_='col-md-4 country')[1:]
for row in rows:
    country = row.find("h3", class_='country-name').text.strip()
    capital = row.find("span", class_='country-capital').text.strip()
    print(f'{country}: {capital}')
