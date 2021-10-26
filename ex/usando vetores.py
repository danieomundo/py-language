nomes = []
precos = []

n = input("nome ou fim")
while n != "fim":
  nomes.append(n)
  
  p = float(input("preco?"))
  precos.append(p)

  n = input("nome ou fim")

for i in range (len(nomes)-1,-1,-1): #ordem reversa
  print(nomes[i], precos[i])
