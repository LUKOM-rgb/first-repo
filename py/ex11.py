#indicar altura e peso
idade = int(input("Indique a sua idade: "))


if    idade <=2 :
     print("Infância - Primeira infancia" )

elif idade <= 6 :
     print("Infância - Intermédia" )

elif idade <= 12 :
     print("Infância - Adoloscencia" )

elif idade <= 14 :
     print("Adoloscencia -  puberdade " )

elif idade <= 19 :
     print(" Adoloscencia - Tardia" )

elif idade <= 39 :
     print(" Adultez - Jovem adulto" )

elif idade <= 59 :
     print(" Adultez - Meia idade" )

elif idade <= 74 :
     print(" idosos- idosos jovens" )

else: print("Idosos - Idosos Velhos")