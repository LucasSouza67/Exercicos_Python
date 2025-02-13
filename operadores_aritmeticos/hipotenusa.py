# leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

import math 

adj = float(input('Tamanho do cateto adjacente ')) #leitura do cateto 1
op = float(input('Tamanho do cateto oposto ')) #leitura do cateto 2

cat1 = math.pow(adj, 2) #cateto adjacente ao quadrado
cat2 = math.pow(op, 2) #cateto oposto ao quadrado
hip = math.sqrt(cat1 + cat2) #calcula a raiz das duas potencias somadas 

hp = math.hypot(adj, op) # calcula a hipotenusa usando a biblioteca math 

print('De maneira matematica é: {:.2f}'.format(hip))
print('Usando apenas a biblioteca - math - : {:.2f}'.format(hp))