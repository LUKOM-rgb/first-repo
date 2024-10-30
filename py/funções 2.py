def maior(numeros:int):

    
    maximo = numeros[0]
    for i in range (0,numeros):
        if numeros[i] > i:
            maximo = numeros[i]
    return maximo

     
    
    












print(maior(10,20,12))
print(maior(5,15,20,14))
