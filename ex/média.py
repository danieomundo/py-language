# Faça um programa que peça as 4 notas bimestrais e mostre a média. 

bim1 = float(input("Insira a nota do 1º bimestre"))
bim2 = float(input("Insira a nota do 2º bimestre"))
bim3 = float(input("Insira a nota do 3º bimestre"))
bim4 = float(input("Insira a nota do 4º bimestre"))

media = float(bim1 + bim2 + bim3 + bim4) / int(4)
print("A média geral foi:", media)
