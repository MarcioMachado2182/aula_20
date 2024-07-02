import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Contador de Cliques")
root.geometry("400x300")
clique = 0
# Adiciona um label
label = tk.Label(root, text="Vamos contar os cliques?", bg="green", fg="white")
label.pack(pady=10)

# Função para contar os cliques
def botao_conta_click():   
    global clique 
    clique = clique +  1 
    label.config(text=f"Você clicou {clique} vezez no botão!")  
   
#Função para limpar os cliques
def botao_limpa_click():
    global clique
    clique  = 0
    label.config(text=f"Você limpou agora voce tem {clique} cliques!")    
    

#Adiciona um botão contador de cliques    
button = tk.Button(root, text="Clique para iniciar a contagem", command=botao_conta_click, bg="silver", fg="yellow")
button.pack(pady=10)

#Adiciona um botão que zera o nº de cliques
button = tk.Button(root, text="Clique Para Zerar", command=botao_limpa_click, bg="purple", fg="white" )
button.pack(pady=10)


root.mainloop()