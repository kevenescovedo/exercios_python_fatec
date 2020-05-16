"""
###1. Faça um programa que receba a base e a altura de um retangulo e imprimir as seguintes saídas:
perimetro = 2 * (base + altura)

area = base * altura

diagonal = raiz(base ** 2 + altura ** 2)
perimetro = 2 * (base + altura)

area = base * altura

diagonal = raiz(base ** 2 + altura ** 2)"""
base = float(input("por favor digite a base do retangulo:\n"))
altura = float(input("por favor digite a altura do retangulo:\n"))
area = base * altura

diagonal = sqrt(base **2 + altura ** 2)
perimetro = 2 * (base + altura)

print("area: " area)
print("diagonal: " diagonal)
print("perimetro: " perimetro)

