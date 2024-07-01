import tkinter as tk
from tkinter import ttk
from casa import Casa

#Criando a Janela Principal
root = tk.Tk()
root.title("Casa")
root.geometry('300x400')


# Adicionar a primeira mensagem
casa = Casa(n_comodos="10",n_portas="3",n_janelas="4",cor_externa="Azul",numero="2182",endereco="Acesso, H(Sq 3 - 2ª Unidade Vicinal - Restinga)",proprietario="Márcio")
message = tk.Label(root, text="numero de comodos: ", background="yellow", anchor="w")
message.pack(side="top", fill="both")
message = tk.Label(root, text="10", anchor="w", background="silver")
message.pack(side="top", fill="both")


# Adicionar a segunda mensagem
casa = Casa(n_comodos="10",n_portas="3",n_janelas="4",cor_externa="Azul",numero="2182",endereco="Acesso, H(Sq 3 - 2ª Unidade Vicinal - Restinga)",proprietario="Márcio")
message = tk.Label(root, text="numero de portas: ", background="yellow", anchor="w")
message.pack(side="top", fill="both")
message = tk.Label(root, text="3", anchor="w", background="silver" )
message.pack(side="top", fill="both")


# Adicionar a terceira mensagem
casa = Casa(n_comodos="10",n_portas="3",n_janelas="4",cor_externa="Azul",numero="2182",endereco="Acesso, H(Sq 3 - 2ª Unidade Vicinal - Restinga)",proprietario="Márcio")
message = tk.Label(root, text="numero de janelas: ", background="yellow", anchor="w")
message.pack(side="top", fill="both")
message = tk.Label(root, text="4", anchor="w", background="silver" )
message.pack(side="top", fill="both")


# Adicionar a quarta mensagem
casa = Casa(n_comodos="10",n_portas="3",n_janelas="4",cor_externa="Azul",numero="2182",endereco="Acesso, H(Sq 3 - 2ª Unidade Vicinal - Restinga)",proprietario="Márcio")
message = tk.Label(root, text="cor externa: ", background="yellow", anchor="w")
message.pack(side="top", fill="both")
message = tk.Label(root, text="Azul", anchor="w", background="silver" )
message.pack(side="top", fill="both")


# Adicionar a quinta mensagem
casa = Casa(n_comodos="10",n_portas="3",n_janelas="4",cor_externa="Azul",numero="2182",endereco="Acesso, H(Sq 3 - 2ª Unidade Vicinal - Restinga)",proprietario="Márcio")
message = tk.Label(root, text="numero: ", background="yellow", anchor="w")
message.pack(side="top", fill="both")
message = tk.Label(root, text="2182", anchor="w", background="silver" )
message.pack(side="top", fill="both")


# Adicionar a sexta mensagem
casa = Casa(n_comodos="10",n_portas="3",n_janelas="4",cor_externa="Azul",numero="2182",endereco="Acesso, H(Sq 3 - 2ª Unidade Vicinal - Restinga)",proprietario="Márcio")
message = tk.Label(root, text="endereco: ", background="yellow", anchor="w")
message.pack(side="top", fill="both")
message = tk.Label(root, text="Acesso, H (Sq 3 - 2ª Unidade Vicinal - Restinga)", anchor="w", background="silver" )
message.pack(side="top", fill="both")


# Adicionar a setima mensagem
casa = Casa(n_comodos="10",n_portas="3",n_janelas="4",cor_externa="Azul",numero="2182",endereco="Acesso, H(Sq 3 - 2ª Unidade Vicinal - Restinga)",proprietario="Márcio")
message = tk.Label(root, text="proprietario: ", background="yellow", anchor="w")
message.pack(side="top", fill="both")
message = tk.Label(root, text="Marcio", anchor="w", background="silver" )
message.pack(side="top", fill="both")


root.mainloop()