numeros = int(input("Nº de termos a imprimir :"))

primeiro = 0
segundo  = 1 


total = 0

if numeros >= 1:
    total = "0"
if numeros >= 2:
    total = "1"



for i in range (3,numeros+1):
    total=primeiro + segundo
    print(total)
    segundo = primeiro
    primeiro = total




    
    

