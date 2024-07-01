import tkinter as tk
from tkinter import ttk ## ttk faz um botao mais bonito que o tk

# root window
root = tk.Tk()
root.geometry('300x200')

texto = tk.Label(root, text="Hello World!")
texto.pack(side="left")

def callback():
    texto.config(text="caraio borracha")
    print("tá frio hoje")
    # do something


botao= ttk.Button(
   root,
   text="Demo Button",
   command=callback
)
botao.pack()
root.mainloop()
