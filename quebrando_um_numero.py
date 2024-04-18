'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
import math #importa a biblioteca matematica 

num = float(input('Foneca um numero: ')) #leitura do numero

num_int = math.trunc(num) #quebra o numero na parte inteira

n = math.floor(num) #arrendonda a numero para baixo e exibe a parte inteira

print('O inteiro de {} é {}'.format(num, n))#arredondada para baixo
print('O inteiro de {} é {}'.format(num, num_int))#quebra o numero