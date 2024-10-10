#indicar altura e peso
altura = float(input("Indique a sua altura em metros: "))
peso = float(input("Indique o seu peso em kilos: "))

#formula para o imc
imc = peso/altura**2

print(altura)

print(peso)

print(" imc: {:.2f} " .format(imc))
