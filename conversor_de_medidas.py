medida = float(input("Forneça uma medida em metros: "))

cm = medida * 100
mm = medida * 1000

print("A medida de {} metros em  centimetros é de {:.0f} e em milimetros é {:.0f}".format(medida, cm, mm))
