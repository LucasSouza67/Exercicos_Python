# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Informe a temperatura '))

fah = (cel * 9 /5) + 32

print('A temperatura de {}°c é igual a {}°f'.format(cel, fah))