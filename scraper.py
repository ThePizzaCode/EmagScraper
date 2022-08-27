from time import sleep
import requests
import re
from bs4 import BeautifulSoup
import csv

#Initializari
produs = 'bicicleta'
baseLink = 'https://www.emag.ro/search/'
numar = 0

#Deschide fisierul csv
file = open('result.csv', 'w')
writer = csv.writer(file)
headerLista = ['Nr. Ord.', 'Nume Produs', 'Link', 'Pret', 'Status Genius']
writer.writerow(headerLista)

#Compune link si fa o cerere pentru sursa
URL = baseLink + produs+'/' +'p'+ '1'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

#Extrage numarul de pagini
maxPages = str((soup.find('ul', attrs={'id':'listing-paginator'})).find('span').text)
maxPages=re.findall(r'\d+', maxPages)[-1]
maxPage = int(maxPages)
print('Am gasit ' + maxPages + ' pagini pentru produsul ' + produs + '\n')

#Extrage produsele din pagina
for pag in range (1, maxPage):
    print('Procesez pagina ' + str(pag) + ' din ' + str(maxPage) + '....' + '\n')
    #sleep(5) #sleep pentru a nu prinde ban-uri
    URL = baseLink + produs+'/' +'p'+ str(pag)
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('div', attrs={'class':'js-product-data'})

    for i in range (0, 60):
        currentResult = results[i]
        numar += 1
        numeProdus = currentResult.find('a', attrs={'class' : 'card-v2-title'}).text
        linkProdus = currentResult.find('a', attrs={'class' : 'card-v2-title'})['href']
        pretProdus = currentResult.find('p', attrs={'class' : 'product-new-price'}).text
        if(currentResult.find('div', attrs={'class' : 'badge-genius'}) != None):
            status = 'Da'
        else:
            status = 'Nu'
        data = [numar, numeProdus, linkProdus, pretProdus, status]
        writer.writerow(data)

file.close()
print('Am terminat de procesat toate paginile')
