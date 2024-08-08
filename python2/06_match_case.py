opcao = int(input("indique a opção desejada:"))

# seleção de opçoes
match opcao:
    case 1:
        print("suporte técnico.")
    case 2:
        print("financeiro.")
    case 3:
        print("nossos produtos.")
    case 4:
        print("outros assuntos.")
    case _:
        print("opção invalida!")