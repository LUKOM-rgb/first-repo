#indicar altura e peso
segundos = int(input("Indique os segundos: "))

#formula para o imc
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundosrestantes = segundos % 60 


print("{:n} horas, {:n} minutos, {:n} segundos"   .format (horas,minutos,segundosrestantes ))



