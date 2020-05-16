"""
### 9. Faça um programa que receba uma sigla do estado de uma pessoa e mostre uma das mensagens:
    carioca
    paulista
    mineiro
    outros estados

"""

sigla = input("digite a sigla do seu estado:\n")
sigla =  sigla.casefold()


if sigla == "rj" :
    print("carioca, fala bolacha")
elif sigla == "sp" :
    print("paulista, fala biscoito, fala o meu")

elif sigla == "mg" :
    print("paulista, fala uai, fala trem")
else:
    print("outros estados")
    

