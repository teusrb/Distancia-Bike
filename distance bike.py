import requests
from geopy.geocoders import Nominatim
import json
import time
import math

#Textos de boas vindas
geolocator = Nominatim(user_agent="maps")
print('Bem-vindo ao Calculador de Tempo e Distância de Bike.\n')
time.sleep(3)
print('Informe o percurso que vai percorrer\n')

#Inputs de endereços
local1 = input('Qual é o ponto A do endereço: ')
location1 = geolocator.geocode("{}".format(local1))

local2 = input('Qual é o ponto B endereço: ')
location2 = geolocator.geocode("{}".format(local2))

#Longitude e Latitude via geopy
long1 = location1.longitude
lat1 = location1.latitude
long2 = location2.longitude
lat2 = location2.latitude

#Requisição dos dados e transformação para json
token = '[TOKEN DA MAPBOX DEVE SER COLOCADO AQUI]' #Token mapbox
requisicao = requests.get('https://api.mapbox.com/directions/v5/mapbox/cycling/{},{};{},{}?access_token={}'.format(long1,lat1,long2,lat2,token))
req = requisicao.json()

#Tempo vem em segundos e transformamos em minutos
temposegundos = (req['routes'][0]['legs'][0]['duration'])
tempoconvertido = temposegundos // 60

#Padrão da unidade de medida do tempo vem em minutos e se o tempo for maior/igual a 60min alteramos essa variavel 
medidatempo = "min"

#Transformar minutos para horas se for maior ou igual a 60 min que equivalem a uma hora
if tempoconvertido >= 60:
    tempoconvertido = math.ceil(tempoconvertido/60)
    medidatempo = "hr"
    

#Distancia vem em metros e transformamos em km
distanciametros = (req['routes'][0]['legs'][0]['distance'])
distanciakm = distanciametros / 1000

#Printando resultados
print("\nCalculando rota...")
time.sleep(3)
print("-------------------------------------------------------------")
print("Trajeto entre {} e {}".format(local1,local2))
print("O tempo de percurso aproximado de bicicleta é de: {:.2f} {}".format(tempoconvertido,medidatempo))
print("A distância aproximada de bicicleta é de: {:.1f} km".format(distanciakm))
print("-------------------------------------------------------------")
