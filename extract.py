import requests
from bs4 import BeautifulSoup

link = "https://www.ojogodobicho.com/deu_no_poste.htm"

requisicao = requests.get(link)
print(requisicao)
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")

# print(site.prettify())


# print(site.title)




titulo = site.find("title")
print(titulo)

pesquisa = site.find_all("table")
print(pesquisa)


pesquisa2 = site.find("td", class_="ylig")
print(pesquisa2)

pesquisa3 = site.find_all("td", class_="ylig")
print(pesquisa2)

