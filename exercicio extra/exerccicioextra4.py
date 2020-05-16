"""
###5. Faça um programa que receba um número e se ele for maior do 20, mostre a metade do número, caso contrário multiplique por 5 e mostre o resultado.


 """

numero = int(input("digite um numero:\n"))
if numero > 20:
    resultado = numero ** 1/2
    print("a metade de", numero," é:" ,resultado)
else:
    resultado = numero * 5
    print("a multiplicação de", numero,"por 5 é:",resultado)


