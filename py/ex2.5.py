import random

while jogarnovamente !="N" :
    num_secreto = random.randint(0, 5)
    maxtentativas = 10  # Definindo o máximo de tentativas

    for tentativas in range(1, maxtentativas + 1):
        palpite = int(input("Indique o seu palpite (entre 0 e 5): "))
        
        if palpite > num_secreto:
            print("O número é menor.")
        elif palpite < num_secreto:
            print("O número é maior.")
        else:
            print("Acertou!")
            print("Acertou em {} tentativas.".format(tentativas))
            break
    else:
        print("Você esgotou suas tentativas.")
        print("O número era {}.".format(num_secreto))

    jogarnovamente = input("quer jogar novamente? (S/N): ").upper()
    if jogarnovamente == "S":
        print("obrigado por jogar")
       







