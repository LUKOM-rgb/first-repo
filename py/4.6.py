import random
listanumeros = [1,10,15,50,90,145,890,76,5,7]

numero = int(input("Qual numero quer da lista: "))

pos1 = listanumeros.index(numero)


print("O numero {:n} está na posição {:n}".format(numero,pos1+1))