listnumeros = []

for i in range(0,11):
    numero = int(input("Insira um numero :"))
    if 0 < numero <= 20:
        listnumeros.append(numero)
    else:
        break

print(listnumeros)

