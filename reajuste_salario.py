'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Informe o salario '))

nsalario = salario * 1.15

print('O salario com aumento de 15% é de {:.2f}'.format(nsalario))