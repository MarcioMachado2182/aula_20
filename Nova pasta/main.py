import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

message = tk.Label(root, text='Hello, Word!', font=("Arial", 16), fg="blue",background="yellow")
#message. pack()
#message. pack(fill="both")
message. pack(ipadx=200, ipady=50)
root.mainloop()

