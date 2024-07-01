import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Contador de Cliques")
root.geometry("400x300")
clique = 0
# Adiciona um label
label = tk.Label(root, text="Vamos contar os cliques?")
label.pack(pady=10)

# Função para ser chamada quando o botão for clicado
def botao_conta_click():
   
    print("Botão clicado!")
    clique += 1 
    label.config(text=f"Você clicou {clique} vezesno botão!")  
    clique += 1


def botao_limpa_click():
    clique  = 0
    label.config(text=f"Você limpou agora voce clicou {clique} vezesno botão!")    

#Adiciona um botão
    
button = tk.Button(root, text="Clique em mim", command=botao_conta_click)
button.pack(pady=10)

buttton = tk.Button(roottext="ZEROU", command=botao_limpa_click)
button.pack(pady=10)


root.mainloop()