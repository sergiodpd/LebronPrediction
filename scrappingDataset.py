import requests
from bs4 import BeautifulSoup
import csv

i = 2004
games = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76, 77, 69, 76, 74, 82, 55, 67]
aux = 0
points = 0
path = 'https://www.basketball-reference.com/players/j/jamesle01/gamelog/'

gamesLJ =[]
gamesLJ.append('Games Played')
pointsLJ = []
pointsLJ.append("Points scored")

#Miro cada una de sus temporadas para recoger sus partidos
for n in range(17):
    url = path + str(i+n) + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.div.find(id='pgl_basic').tbody
    
    if n > 0:
            aux += games[n-1]
    
    #Mirar cada uno de sus partidos para coger el número de puntos
    for m in range(1, games[n]+1):
        m = aux + m
        colID = 'pgl_basic.' + str(m)
        gamesLJ.append(m)
        points += int(table.find(id=colID).findAll('td')[26].text)
        pointsLJ.append(points)
    
        #Aquí he sacado ya los datos y solo me queda meterlo en el csv y probar los regresores
        #print("Game", m, "Points", points)


dataset =  r'C:\Users\Sergio\Documents\LebronPrediction\dataset'

newFile = open(dataset + "\\LJPredictionNew.csv", 'w')

data = []
rows = []

for n in range(0, len(gamesLJ)):
    print(n)
    rows.append(gamesLJ[n])
    rows.append(pointsLJ[n])

    data.append(rows)
    rows  = []

with newFile:
    writer = csv.writer(newFile)
    writer.writerows(data)


        


