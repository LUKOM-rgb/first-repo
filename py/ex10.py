#indicar altura e peso

print (" \t\t\tPlanetas\n\t\t 1 - Mercurio\n\t\t 2 - Venus\n\t\t 3 - Marte\n\t\t 4 - Júpiter\n\t\t 5 - Saturno\n\t\t 6 - Urano ")
peso = float(input("Indique o seu peso: "))
planeta= int(input("Indique o código do planeta planeta: "))



if    planeta == 1 :
     gravidade = 0.37
     PlanetaX = peso * gravidade / 0.98
     print("O seu peso de {:.1f} Kg no planeta {:n} seria de {:.2f} Kg" .format(peso,planeta,PlanetaX))

elif planeta == 2 :
     gravidade = 0.90
     PlanetaX = peso * gravidade / 0.98
     print("O seu peso de {:.1f} Kg no planeta {:n} seria de {:.2f} Kg" .format(peso,planeta,PlanetaX))


elif planeta == 3 :
     gravidade = 0.37
     PlanetaX = peso * gravidade / 0.98
     print("O seu peso de {:.1f} Kg no planeta {:n} seria de {:.2f} Kg" .format(peso,planeta,PlanetaX))


elif planeta == 4 :
     gravidade = 2.53
     PlanetaX = peso * gravidade / 0.98
     print("O seu peso de {:.1f} Kg no planeta {:n} seria de {:.2f} Kg" .format(peso,planeta,PlanetaX))

elif planeta == 5 :
     gravidade = 1.06
     PlanetaX = peso * gravidade / 0.98
     print("O seu peso de {:.1f} Kg no planeta {:n} seria de {:.2f} Kg" .format(peso,planeta,PlanetaX))
else: 
    
     gravidade = 0.91
     PlanetaX = peso * gravidade / 0.98
     print("O seu peso de {:.1f} Kg no planeta {:n} seria de {:.2f} Kg" .format(peso,planeta,PlanetaX))
    