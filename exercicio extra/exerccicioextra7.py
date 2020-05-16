"""
###6. Faça um programa que receba um número, se ele for positivo, mostre seu inverso, caso contrário, mostrar o seu valor absoluto.



 """

numero = int(input("digite um numero:\n"))
if numero > 0:
    resultado =  "1/" + str(numero)
    valor_decimal = 1/numero
    print("o inverso de", numero,"é:" ,resultado)
    print("decimal:", valor_decimal)
elif numero == 0:
    print (" o valor obsoluto de 0 é 0")
else:
   resultado = -(numero)
   print (" o valor obsoluto de", numero, "é:",resultado)


