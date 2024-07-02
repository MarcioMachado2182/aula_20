import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("EXERCICIO 3")
root.geometry("400x300")

# Adiciona Frames
frame1 = tk.Frame(root, bg="blue")
frame1.pack( fill="both")
frame2 = tk.Frame(root, bg="silver")
frame2.pack( fill="both")
frame3 = tk.Frame(root, bg="pink")
frame3.pack(fill="both")

#Criando a Label
label1 = tk.Label(frame1, text="Metalica", bg="purple", fg="yellow")
label1.pack(side="right")

#criando area de entrada

entry = tk.Entry(root)
entry.pack(pady=10)

# Adiciona um botão para pegar o texto da entrada
def on_get_text():
    user_input = entry.get()
    print(f"Entrada do usuário: {user_input}")
    label2 = tk.Label(frame2, text=f"Você digitou: {user_input}")
    label2.pack(side="right")

    label2.pack(side="right")




#Criando o Botao
button = tk.Button (frame3, text="Digite alguma Coisa", bg="silver", fg="yellow", anchor="w")
button.pack(pady=10, side="right")






root.mainloop()