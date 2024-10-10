#indicar altura e peso
genero = input("indique o sexo (M,F):")

idade = int(input("Indique a sua idade: "))

if    genero == "F":
        bpm = 226-idade
        print("FCM= {:n} BPM" .format(bpm))
elif genero == "M":
    bpmF = 220-idade
    print("FCM= {:n} BPM" .format(bpmF))