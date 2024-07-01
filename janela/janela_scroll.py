import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
#root.title("Minha Primeira GUI")
root.geometry("70x21")

# Adiciona um label
message = tk.Label(root, text="Label 2 ", background="green", anchor="w", fg="white")
message.pack(side="left")

message = tk.Label(root, text="Label 3 ", background="blue", anchor="w", fg="white")
message.pack(side="left")

message = tk.Label(root, text="Label 1 ", background="red", anchor="w", fg="white")
message.pack(side="left")



root.mainloop()