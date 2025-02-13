''' leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome. '''

nome = str(input("Informe seu nome: ")).strip()
print("Nome armazenado: {}".format(nome))
print("Seu nome possui {} letras".format(len(nome) - nome.count(' ')))
print("Nome em minusculo: {}".format(nome.lower()))
print("Nome todo em maiusculo: {}".format(nome.upper()))
# print("Seu primeiro nome posssui {} letras".format(nome.find(' ')))

separa = nome.split() #separa os nomes em uma lista
# print(separa)

print("Seu primeiro nome é {} e tem {} letras".format(separa[0], len(separa[0])))
