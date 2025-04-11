
# Web Scrapper

# Importando as bibliotecas
import requests
import argparse
from bs4 import BeautifulSoup

# Definindo Argumentos
parser = argparse.ArgumentParser(description="Web Scapper")
parser.add_argument("-s", "--site", help="Site alvo", required=True)
args = parser.parse_args()
site = args.site


# Filtragem do href
def scrapper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    urls = [a["href"] for a in soup.find_all("a", href=True)]
    return urls


# Print do conteúdo
urls = scrapper(site)
for url in urls:
    print(url)
