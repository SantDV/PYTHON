from tkinter import *

raiz = Tk()
raiz.title("Ventana")
raiz.iconbitmap("login.ico")
raiz.resizable(False, False)

miFrame = Frame()
miFrame.pack()

miFrame.config(width="400", height="400")

raiz.mainloop()
