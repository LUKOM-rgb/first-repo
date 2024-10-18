

soma = 0

maior = 0

i = 0
while i<10 :
    numero = int(input("indique um numero 10 vezes (está na {:n} vez): ".format(i+1)))
    
    # se o numero for maior que 20 vai pedir para voltar a por o numero 
    if numero > 20:
        continue
    soma += numero                            #soma todos os numeros do input
    i+=1
    
    # para registar o maior numero 
    if numero > maior:
        maior = numero 

media = soma/10                              


print("maior é {:n}".format(maior))

print("A média é {:n}".format(media))

