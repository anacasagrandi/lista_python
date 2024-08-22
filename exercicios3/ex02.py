# Lista usando laço for
print (" ")
print ("Lista de Estados")
print (" ")

estados = ["Rio de Janeiro", "São Paulo", "Minas Gerais", "Espírito Santo"]

#listar usando laço com índice
for i, estado in enumerate(estados, 1):
    print(f"{i} - {estado}")