#indicar altura e peso
numero = int(input("Indique um numero: "))

#formula para o imc
numerofinal = numero % 2

if numerofinal == 1:
   print("O numero {:n} é impar" .format (numero))
else:
   print("O numero {:n} é par" .format (numero))