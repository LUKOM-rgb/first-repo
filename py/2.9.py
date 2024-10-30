numero = int(input("Indique um Numero: "))
resto = " "


for i in range (1,numero):
        resto = numero % 2
        print( resto)
        numero = numero // 2
        if numero == 0 :
            break

      