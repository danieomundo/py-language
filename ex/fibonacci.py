#sequência de fibonacci

n = int(input("Digite quantos termos da sequência deseja:"))

t1 = 0
t2 = 1

print (t1)
print (t2)

for i in range (2, n):
  t3 = t2 + t1
  print (t3)
  t1 = t2 #transformar o termo 1 em termo 2
  t2 = t3 #transformar o termo 2 em termo 3
