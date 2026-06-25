nome = input("qual é seu nome? ") 
print("Olá,", nome + "!")
idade = input("qual é sua idade? ")
print("Você tem", idade, "anos.")
if int(idade) < 18:
    print("cade a sua mãe? ")
else:
    print("Você é maior de idade porfavor seja responsável com suas ações.")