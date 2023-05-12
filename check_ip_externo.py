import re
import json
from urllib.request import urlopen

menu = input("""O que deseja verificar?
        1) Seu IP Público
        2) IP Público Específico
        >   """
) # removido int(input("")) para ELSE funcionar com ENTER


if menu == "1": # menu = string
    URL = "https://ipinfo.io/json"
elif menu == "2":
    ip_escolha = input("\nDigite o endereço IP: ")
    URL = "https://ipinfo.io/{0}/json".format(ip_escolha)
else:
    URL = "https://ipinfo.io/json"


dados = json.load(urlopen(URL)) ## resposta = urlopen(URL)

ip = dados["ip"]
org = dados["org"]
cidade = dados["city"]
estado = dados["region"]
pais = dados["country"]
timeZone = dados["timezone"]

print("\n\nIP: {0} \nOrg.: {1} \nCidade: {2} \nEstado: {3} \nPaís: {4} \nFuso Horário: {5}".format(ip,org,cidade,estado,pais,timeZone), "\n" )
