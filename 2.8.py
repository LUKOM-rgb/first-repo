numero = int(input("Indique um Numero: "))
soma = 0

for i in range (1,numero):
        resto = numero % i
        if resto == 0:
            soma += i
            print(i, end="+")
        if resto != 0:
         continue
    
if soma == numero:
    print("O numero {:n} é perfeito".format(numero))
else:
    print("O numero {:n} não é perfeito".format(numero))
    





    
    