import random

# Lê o username
username = input("Username: ")

# Verifica se o username contém espaços
if " " in username:
    print("username é inválido")
else:
    # Inicializa a password como uma lista
    password = []
    
    # Calcula o número total de letras no username
    num_letras = len(username)
    
    # Intercala letras nas posições pares com números aleatórios
    for i in range(num_letras):
        if i % 2 == 0:  # Se a posição for par
            password.append(username[i])  # Adiciona a letra
        else:  # Se a posição for ímpar
            password.append(str(random.randint(0, 9)))  # Adiciona um número aleatório
    
    # Adiciona o número total de caracteres no final da password
    password.append(str(num_letras))
    
    # Junta a lista em uma string
    senha_final = ''.join(password)
    
    print("A password gerada é:", senha_final)
