import requests
from bs4 import BeautifulSoup  


# URL = requests.get("https://www.climatempo.com.br/").content
soup = BeautifulSoup(URL.text, "html.parser")

resposta = soup.find("div", {"class": "modal-content"}).get_text(strip=True)


# print(soup.prettify()) ## resultado em String
print(resposta)
print(soup.h1)
