def primo (x):
  cont = 0
  for i in range(1, x+1):
    if x % i == 0:
      cont += 1
  if cont == 2:
    return True
  else:
    return False

def invers (num):
  niv = 0
  while num > 0:
    resto = num % 10
    num = num // 10
    niv = niv * 10 + resto
  return niv
vet = []
vet2 = []

for i in range (300, 751):
  if primo(i):
    vet.append(i)

for k in vet:
  var = invers(k)
  if primo(var):
    vet2.append(var)

print(f'Os números primos entre 300 e 750 são: {vet}')
print('-------------------------------------------------------------')
print(f'Os números primos do inverso de cada número do vetor anterior são: {vet2}')



'''
# num primo

num = int(input('Digite um número:'))
tot = 0

for c in range(1, num+1):
  if num % c == 0:
    print(f'{c} ')
    tot += 1
print(f"O número {num} foi divisivel {tot} vezes.")

if tot == 2:
  print("Por isso ele É primo.")
else:
  print("Por isso ele NÃO é primo.")


'''
