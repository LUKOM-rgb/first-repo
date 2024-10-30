numero = int(input("Indique um numero: "))

fatorial = numero
total = 1  

while fatorial > 1:
    print(fatorial, end="*")  # Imprime o número atual seguido de "*"
    total *= fatorial  # Multiplica o total pelo valor atual de fatorial
    fatorial -= 1  # reduz o valor de fatorial

# Imprime o último número 1 sem o "*"
print(fatorial)

# Multiplica pelo último valor 1
total *= fatorial

# o resultado final 
print("=", total)