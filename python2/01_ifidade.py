#variaveis
nome = input("informe o seu nome:")
idade = int(input("Informe a sua idade:"))

#verifica idADE
if idade >=18:
    print(f"Olá, {nome}! Você tem {idade} anos. Então você é maior de idade.")
else:
    print(f"Olá, {nome}! Você tem {idade} anos. Então você é menor de idade.")