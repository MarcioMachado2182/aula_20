import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("EXERCICIO 3")
root.geometry("400x300")

# Adiciona um label
frame = tk.Frame(root, bg="blue")
frame.pack( fill="both")
label = tk.Label(frame, text="Metalica", bg="purple", fg="yellow")
label.pack(side="right")

entry = tk.Entry(root)
entry.pack(pady=10)

# Adiciona um botão para pegar o texto da entrada
def on_get_text():

    
    user_input = entry.get()
    print(f"Entrada do usuário: {user_input}")
    label.config(text=f"Você digitou: {user_input}", anchor="w")
    label.pack(side="right")

get_text_button = tk.Button(root, text="Obter texto", command=on_get_text)
get_text_button.pack(pady=10)




root.mainloop()