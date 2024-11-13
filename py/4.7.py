listapluvisidade = []

for i in range(1, 12 + 1):
    pluvisidade = int(input("A pluvisidade do mês {:n}º: ".format(i)))  
    listapluvisidade.append(pluvisidade)  

listapluvisidade.sort()  # Ordena a lista
print(listapluvisidade)   # Exibe a lista ordenada
