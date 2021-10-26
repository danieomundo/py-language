x = str(input('Please, insert a word: '))
y = x[::-1] #inverte a palavra

if x == y:
  print('It's a palindrome.')
else:
  print('It's NOT a palindrome.')
        

'''def result(palavra):
    palavra_min = palavra.lower()
    palavra_invertida = palavra_min[::-1]
    if palavra_min == palavra_invertida:
        print("A palavra é palíndroma.")
    else:
        print("A palavra não é palíndroma.")
    print()
    print('Sua palavra: ', end='')
    print(palavra)
    print('Inversão: ', end='')
    print(palavra_invertida)

word=input('Digite uma palavra: ')
print(result(word))'''
