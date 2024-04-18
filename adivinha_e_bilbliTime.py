# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

from random import randint #importa a rand (int)
from time import sleep

x = randint(0, 100) #escolhe um numero entre 0 e 100

usuario = int(input("informe um numero entre 0 e 100: ")) #entarda de dados 

print("AGUARDE! ESTOU A PENSAR!!")
sleep(5)

# estrutura condicional  
if(x != usuario):
     print("voce ERROU!! Tente novamente")
     print("o numero era {}". format(x))
if(x == usuario):
    print("Parabens!! voce acertou!!")

