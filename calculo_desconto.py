'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preco = float(input('Valor do produto: '))

npreco = preco * 0.95

print('O preço com desconto é de : {}'.format(npreco))