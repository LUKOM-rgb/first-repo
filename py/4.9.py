semanas = ["domingo","segunda","terça","quarta","quinta","sexta","sabado"]
visitantes = []

for i in range(len(semanas)):
    visitas = int(input(f"{semanas[i]}        :"))
    visitantes.append(visitas)


visitantes.sort()
visitantes.reverse()



for i in range(len(semanas)):
    print(f"{semanas[i]}    :{visitantes[i]}")