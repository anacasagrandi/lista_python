import tkinter as tk
#funçao p transferir texto do input p label
def mostrar_mensagem():
    texto = caixa_texto.get() #obter i texto da caixa d texto
    label_resultado.config(text=texto) #mostrar o texto na label

#Janelaprincipal
janela = tk.Tk()
janela.title("Exemplo de interface")
janela.geometry("400x150")

#cria caixa de texto
caixa_texto = tk.Entry(janela, width=60)
caixa_texto.pack(pady=10)

#cria botao
botao = tk.Button(janela, text= "Mostrar texto", command= mostrar_mensagem)
botao.pack(pady=5)

#cris rotulo p mostra resdultadi label
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=5)


#executar a jabela principal
janela.mainloop()