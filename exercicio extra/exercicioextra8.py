"""
### 8. Faça um programa que receba um nome de capital, verifique se é a capital do Brasil. Se for mostre "Parabéns", caso sontrário, mostre "Estude mais"


"""
from unicodedata import normalize
capital = input("qual  é  capital do Brasil ?: ")
capital =  capital.casefold()
"""REMOVER ACENTO EM PYTHON"""
capital = normalize('NFKD', capital).encode('ASCII','ignore').decode('ASCII')

if capital == "brasilia" :
    print("parabéns você acetou")
else:
    print("estude mais pois você errou !!!")
