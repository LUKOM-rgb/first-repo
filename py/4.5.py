listafaturacao = []

for i in range(1, 12 + 1):
    faturacao = int(input("Faturação do mês {:n}º: ".format(i)))  
    listafaturacao.append(faturacao)  


media = sum(listafaturacao) / 12


print(f"O Mês com maior faturação foi: {max(listafaturacao)}")
print(f"O Mês com menor faturação foi: {min(listafaturacao)}")
print("Valor médio de faturação {:.3f}".format(media))
