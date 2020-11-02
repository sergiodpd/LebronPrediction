import requests
from bs4 import BeautifulSoup

i = 2004
games = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76, 77, 69, 76, 74, 82, 55, 67]
aux = 0
path = 'https://www.basketball-reference.com/players/j/jamesle01/gamelog/'

gamesLJ =[]
pointsLJ = []

for n in range(17):
    url = path + str(i+n) + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.div.find(id='pgl_basic').tbody
    
    if n > 0:
            aux += games[n-1]
    
    for m in range(1, games[n]+1):
        m = aux + m
        colID = 'pgl_basic.' + str(m)
        #Da error aquí por alguna razón 
        print(table.find(id=colID).findAll('td')[26].text)

        


