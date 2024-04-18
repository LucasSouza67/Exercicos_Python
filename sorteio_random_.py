#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random # importa a biblioteca random

#leitura dos nomes 
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1, n2, n3, n4] #adiciona os nomes em uma lista 

sorteado = random.choice(lista)#escolhe um nome da lista 

print('O aluno sorteado foi {}'.format(sorteado))