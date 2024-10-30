nome = input("indique um nome: ")

comp = len(nome)
print("Numero de caracteres: ",comp)

pos = nome.find(" ")
print("Numero de espaços: ",pos)




a_count = nome.count("a")
e_count = nome.count("e")
i_count = nome.count("i")
o_count = nome.count("o")
u_count = nome.count("u")

# Exibe os resultados
print("A vogal 'a' aparece: {:d} vezes".format(a_count))
print("A vogal 'e' aparece: {:d} vezes".format(e_count))
print("A vogal 'i' aparece: {:d} vezes".format(i_count))
print("A vogal 'o' aparece: {:d} vezes".format(o_count))
print("A vogal 'u' aparece: {:d} vezes".format(u_count))