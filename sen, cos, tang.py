#leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan # importa apenas o radiano, seno, cosseno e tangente da biblioteca math 

angulo = float(input('Informe o angulo: ')) # leitura do angulo

seno = sin(radians(angulo))# converte para radiano e calcula o seno 
cosseno = cos(radians(angulo))# converte para radiano e calcula o cosseno 
tangente = tan(radians(angulo))# converte para radiano e calcula a tangente 

print('O seno do angulo de {} graus é {:.2f}'.format(angulo, seno))
print('O cosseno do angulo de {} graus é {:.2f}'.format(angulo, cosseno))
print('A tangente do angulo de {} graus é {:.2f}'.format(angulo, tangente))