import random

numero = int(input("Quantos números deseja ler: "))

maior = 0
segundo_maior = 0

for i in range(1, numero + 1):
    num_secreto = random.randint(0, 50)
    print(num_secreto)
    
    if num_secreto > maior:
        segundo_maior = maior  # O maior se torna o segundo maior
        maior = num_secreto  # O novo número se torna o maior
    elif num_secreto > segundo_maior and num_secreto != maior:
        segundo_maior = num_secreto  # Atualiza o segundo maior se for menor que o maior

print("O segundo maior valor da lista de números lidos é {:n}".format(segundo_maior))



        