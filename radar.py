'''
leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h é multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
'''
from time import sleep
velocidade = float(input("Informe a velocidade: "))

print("Calculando a velocidade....\n")
sleep(2)

if(velocidade > 80):
    multa = (velocidade - 80) * 7
    print("Calma lá paizão ta indo muito rapido!!\n")
    print("----->" * 5 + "\nSua multa sera de: {:.2f}\n".format(multa) + "<-----" * 5)    
else:
    print("Parabens continue dirigindo dentro do limite!!")

   