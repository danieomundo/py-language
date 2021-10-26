# em construção!

'''
Programa que leia e valide as seguintes informações:
nome: maior que 3 caracteres;
idade: entre 0 a 150;
salario: maior que zero;
sexo: 'f' ou 'm';
estado civil: 's', 'c', 'v', 'd'.
'''

nome = str(input("Nome:"))
idade = int(input("Idade:"))
salario = float(input("Salário:"))
sexo = str(input("[f/m]:"))
estcivil = str(input("Estado civil s/c/v/d:"))

while len(nome) < 3:
  nome = str(input("Digite um nome válido!"))

while idade > 150:
  idade = int(input("Digite uma idade válida"))

if salario < 0:
  salario = float(input("Salário precisa ser maior que 0!"))
  
  
  
