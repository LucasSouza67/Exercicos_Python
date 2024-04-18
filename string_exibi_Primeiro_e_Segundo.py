""" 
verifica se um um nome tem silva ou não
Conta a numero de 'A'
E exibe o primero e ultimo nome da pessoa 

"""

nome = str(input("informe o seu nome: ")).strip()

nome.lower()
nome = nome.split()
#print(nome)

print("Seu primeiro nome é {}".format(nome[0]))
print("seu ultimo nome é {}".format(nome[len(nome)-1]))
print("seu nome tem {} letras 'A' ".format(nome.count('a')))
    
if('silva' in nome):
    print("Seu nome TEM silva")
else:
    print("Seu nome NÃO tem silva")
