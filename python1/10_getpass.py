#importação de biblioteca getpass
import getpass  as gtp
usuario = input("Nome do usuário:")
senha = gtp.getpass("Digite sua senha:")
#Verificação do numero de caracteres da senha
if len(senha) >= 6:
    print(f"Usuário cadastrado com sucesso!")
else: 
    print("Senha deve ter pelo menos 6 caracteres!")
