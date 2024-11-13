numeros = int(input("Quantidade de numeros quer na lista: "))

listanumeros = []
listanumeros2 =[]


for i in range(1,numeros+1):
    numeros2 = int(input("insira o {:n}º numero: ".format(i)))
    listanumeros.append(numeros2)
    

listanumeros2 = list(set(listanumeros))

listanumeros2.sort





print(listanumeros)
print(listanumeros2)