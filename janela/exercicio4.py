import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Dados Pessoais")
root.geometry("600x600")

# Adiciona Frames
frame1 = tk.Frame(root, bg="blue")
frame1.pack( fill="both")
frame2 = tk.Frame(root, bg="silver")
frame2.pack( fill="both")
frame3 = tk.Frame(root, bg="pink")
frame3.pack(fill="both")

#Criando a Label
label1 = tk.Label(frame1, text="Qual o Seu nome", bg="purple", fg="yellow")
label1.pack()

label2 = tk.Label()
label2.pack()

#criando area de entrada
entry = tk.Entry(frame2)
entry.pack(side="right")

# Adiciona um botão para pegar o texto da entrada
def on_get_text():
    global entry
    user_input = entry.get()
    print(f"Seu Nome é: {user_input}")
    label2.config(text=f"Voce digitou: {user_input}")
   
#Criando o Botao
button = tk.Button (frame3, text="Confirme Aqui!", command=on_get_text, bg="silver", fg="yellow")
button.pack(pady=10, side="right")


root.mainloop()