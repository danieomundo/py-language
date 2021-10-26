# Fazer um programa que leia um nome de usuário e a sua senha e não aceite a senha 
# igual ao nome de usuario, mostrando uma mensagem de erro e voltando a pedir as 
# informações.

user = str(input("digite um nome de usuário"))
senha = str(input("digite uma senha:"))

while user == senha:
  senha = str(input("erro! usuário e senha não podem ser iguais."))

if user != senha:
  print("cadastro realizado com sucesso.")

