import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Scrollbar Visível")
root.geometry("300x200")

# Adicionar a primeira mensagem
message = tk.Label(root, text="Hello, World!",background="yellow")
message.pack(side="top", expand=True, fill="both")

# Adicionar a segunda mensagem
message2 = tk.Label(root, text="Hello, World!")
message2.pack(side="top", expand=True, fill="both")

root.mainloop()
