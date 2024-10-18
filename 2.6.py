primo = True
numero = int(input("Indique um Numero: "))
for  i in range(2,numero):
    resto = numero % i
    if resto == 0:
        primo = False
        break

if primo == True:
    print("O numero {:n} é primo".format(numero))
else:
    print("O numero {:n} não é primo".format(numero))
    
        


