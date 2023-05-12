import requests
import operator

from bs4 import BeautifulSoup  
from collections import Counter




def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")

    # procura por DIV com CLASSE com qualquer conteúdo
    # for each_text in soup.findAll("div", {"class": "entry-content"}): ## NÃO ENTRA NISSO AQUI
        # content = each_text.text

    # Modificação para ler toda a pagina, removido primeiro FOR
    content = soup.text

    # letras minusculas + cada palavra em uma linha
    words = content.lower().split()
    for each_word in words:
        wordlist.append(each_word)
    
    clean_wordlist(wordlist)
    

def clean_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        symbols = "!@#$%&*()_-=+`'\[{]}~^;:.>,</?|"

        for i in range(0, len(symbols)): ## remove do Array os simbolos acima
            word = word.replace(symbols[i], "")

        if len(word) > 0: ### se numero de caracteres for maior que Zero
            clean_list.append(word) # limpa a lista adicionando "word" acima no lugar
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    for key, value in sorted(word_count.items(),
                            key = operator.itemgetter(1) ):
        print ("% s : % s" % (key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)

if __name__ == "__main__":
    start("https://pt.wikipedia.org/wiki/Python")