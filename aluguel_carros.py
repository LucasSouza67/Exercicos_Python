# leia quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('informe a quantidade de dias alugados '))
km = float(input('informe o numero de kms rodados '))

preco = (dia * 60) + (km * 0.15)

print('O valor a ser pago é de {:.2f} por {} dias e {}Kms rodados'.format(preco, dia, km))