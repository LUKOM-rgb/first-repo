minimo = int(input("Indique um valor minimo: "))
maximo = int(input("Indique um valor maximo: "))
total = 0
for i in range(minimo,maximo+1) :
    if i % 2 == 0: 
     total +=i
     

print("A soma entre pares do numeros {:n} e {:n} é {:n}".format(minimo,maximo,total))