#indicar altura e peso
peso = float(input("Indique o seu peso em kilos: "))
altura = float(input("Indique a sua altura em metros: "))

#formula para o imc
imc = peso/altura**2

print(altura)

print(peso)

print(" imc: {:.2f} " .format(imc))

if    imc < 18.5 :
    print("Baixo peso")

elif 18.5 <= imc < 24.9 :
    print("Peso normal")

elif 25<= imc < 29.9 :
    print("Excesso de peso")

elif 30 <= imc < 34.9 :
    print("Obesidade grau I")

elif 35 <= imc < 39.9 :
    print("Obesiadade grau II")

else: 
    print("Obesiadade grau III")
    