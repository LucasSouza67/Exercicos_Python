#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle #importa do random a função shuffle(embaralhar)

#leitura dos nomes 
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]#coloca os nomes em uma lista 

shuffle(lista)#embaralha a ordem da lista 

print('A ordem de apresentação é: ')
print(lista)#exibe a lista 

