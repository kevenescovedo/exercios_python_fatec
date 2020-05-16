"""### 10. Faça um programa que receba um salário de uma pessoa e mostre o desconto de INSS de acordo com a tabela a seguir

| Valores | Porcentagem |
|---|---|
|Menor ou igual a R$ 600 |	Isento |
| Maior que 600,00 e menor ou igual a 1200,00 | 20% |
|Maior que 1200,00 e menor ou igual a 2000,00 |	30% |
|Maior que 2000,00	|	40% |


 """

salario = float(input("digite o salario de uma pessoa:\n"))
if salario <= 600:
    print ("isento")
elif salario > 600 and salario <= 1200:
  desconto = (salario *(20/100))
  print("deconto do INSS é de:",desconto,"reais")
elif salario > 1200 and salario <= 2000:
  desconto = (salario *(30/100))
  print("deconto do INSS é de:",desconto,"reais")
else:
     desconto =(salario *(40/100))
     print("deconto do INSS é de:",desconto,"reais")
