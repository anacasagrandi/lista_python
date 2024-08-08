# 5. Monte um programa que calcule a comissão de vendedor.
print("Insira os valores.")
VProduto = float(input("Insira o valor do Produto: "))
PComissao = float(input("Insira a porcentagem da comissão: "))

# Calculo
Comissão = (VProduto * (PComissao / 100))


print(f"A sua Comissão é de R${Comissão}")