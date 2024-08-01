#3. Faça um programa que faça a conversão de dólar em euro.
taxa_de_cambio = 0.92 #1 dolar é 0.92 euros
def converter_dolar_para_euro(dolares):
    return dolares * taxa_de_cambio

# Solicita ao usuário o valor em dólares
try:
    valor_dolares = float(input("Digite o valor em dólares: "))
    if valor_dolares < 0:
        print("O valor deve ser positivo.")
    else:
        valor_euros = converter_dolar_para_euro(valor_dolares)
        print(f"{valor_dolares} dólares é igual a {valor_euros:.2f} euros.")
except ValueError:
    print("Por favor, insira um número válido.")