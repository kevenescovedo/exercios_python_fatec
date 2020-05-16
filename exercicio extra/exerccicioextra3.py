""" ###3. Faça um programa que receba os lados a, b, c de um paralelepípedo. Calcule e mostre a diagonal. Sabe-se que 
diagonal = raiz(a ** 2 + b ** 2 + c ** 2)

 """
import math
a = float(input("digite o numero de um lado:\n"))
b = float(input("digite o numero do segundo lado:\n"))
c = float(input("digite o numero de terceiro lado:\n"))
diagonal = math.sqrt(a **2 + b ** 2 + c ** 2)
print(" a digonal do paralelipido:",diagonal)
