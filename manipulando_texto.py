# manipulação de texto

frase = 'Vasco Da Gama'
frase1 = 'Sexta Tem Aula ?'
frase2  = 'Vasco x Gremio'
frase3 = 'rio de janeiro'

print('Frases antes da mudança: \n')
print(frase)
print(frase1)
print(frase2)
print(frase3)
print('\n')

print('tamanho da primeira frase: {}'.format(len(frase)))# conta o tamanho da primeira string

print('numero de e na segunda frase: {}'.format(frase1.count('e')))# conta a numero de 'e' na segunda string 
print('\n')

print('frases apos as alterações: \n')
frase2 = frase2.replace('Vasco', 'Gremio')# troca Vasco por Gremio
print(frase2)

frase2 = frase2.replace('Gremio', 'Vasco')# troca Gremio por Vasco
print(frase2)

frase = frase.upper()# coloca a primeira frase toda em maiúsculo
print(frase)

frase1 = frase1.lower()# coloca a segunda frase toda em minúsculo
print(frase1)

frase3 = frase3.capitalize()# coloca a primeira letra da quarta frase em maiúsculo 
print(frase3)

frase3 = frase3.title()# colaca todas as primeiras letras da quarta frase em maiúsculo
print(frase3)
