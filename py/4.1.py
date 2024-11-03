
def aboveAverage(listnumeros):
    media = sum(listnumeros)/ len(listnumeros)
    for numero in listnumeros:
            if numero > media:
                 cont+= 1
    return cont



listnumeros = []
for i in range(0,11):
    numero = int(input("Insira um numero :"))
    listnumeros.append(numero)

cont = aboveAverage(listnumeros)

print("Existem {:n} numeros acima da media " .format(cont))
