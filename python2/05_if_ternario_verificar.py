valor = int(input("Informe o valor: "))

# Uso do if ternário
teste = "situação Normal!" if valor < 100 else "situação: Pré-diabetes!" if valor in range (100,125) else "Diabetes"