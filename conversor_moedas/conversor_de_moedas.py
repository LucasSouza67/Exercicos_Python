real = float(input("Tem quantos reias aí meu parceiro ? "))

#valores em 12/5/2023
dolar = real/4.92
euro = real/5.38
libra = real/6.13

print("Você pode comprar {:.2f} Dolares com {:.2f} Reais".format(dolar, real))
print("Você pode comprar {:.2f} Euros com {:.2f} Reais".format(euro, real))
print("Você pode comprar {:.2f} Libras com {:.2f} Reais".format(libra,real))