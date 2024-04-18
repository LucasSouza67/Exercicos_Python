'''
Faça um programa que leia a largura e a altura de uma parede em metros 
calcule a sua área 
calcule a quantidade de tinta necessária para pintá-la (cada litro pinta 2 metros)
'''

largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))

area = largura * altura 

tinta = area / 2

print('A area da parede de {}x{} é {}m²'.format(largura, altura, area))
print('serao necessarios {} litros de tinta para pinta-la'.format(tinta))