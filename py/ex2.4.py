import random

num_secreto = random.randint(0,5)

tentativas = 1

maxtenativas = 50

for i in range(tentativas,maxtenativas+1) :
    palpite = int(input("Indique o seu Palpite: "))
    if palpite > num_secreto : 
        print("O numero é menor")
        tentativas+= 1 
    
    elif palpite< num_secreto:
        print("O numero é maior")
        tentativas+= 1 
    
    elif tentativas == 10:
        print("Não consegiu")
    else :
        print("Acertou")
        print ("Acertou em {:n} Tentativas".format(tentativas))
        break
else:
    print("voce esgotou em {:n}".format(maxtenativas))
    print("O numero é {:n}".format(num_secreto))








