#indicar altura genero
genero = input("indique o sexo (M,F):")

altura = int(input("Indique a sua altura (cm): "))

#dpendendo do genero faz o calculo
if    genero == "F":
        K = 2
        pesoideal = (altura-100) - (altura-150)/K
        print("O peso ideal é {:.2f} Kg" .format(pesoideal))
elif genero == "M":
     K = 4
     pesoideal = (altura-100) - (altura-150)/K
print("O peso ideal é {:.2f} Kg" .format(pesoideal))