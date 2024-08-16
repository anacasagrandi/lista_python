#tabuada
while True:
    print("")
    num = int(input("Informe um número: "))
    print("")
    print("Tabuada do {num}")
    print("")

    #Gerar tabuada usando Laço for
    for i in range(1,11):
       result = num * i
       print(f"{num} * {i} = {result}")
       i += 1

    #pergunta se quer continuar
    continuar = input("\nDeseja calcular outra tabuada(s/n): ?")
    if continuar.lower() != 's':
      print("Encerrando o programa.")
      break