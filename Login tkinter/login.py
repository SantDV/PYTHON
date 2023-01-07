from tkinter import *
import sys


def validar():
     if(usuario.get()=="admin" and password.get()=="admin"):
          print("Datos correctos!")
     else:
          print("Datos incorrectos!")


raiz = Tk()
raiz.title("Ventana")
raiz.iconbitmap("login.ico")
raiz.resizable(False, False)
miFrame = Frame()
miFrame.pack()
miFrame.config(width="400", height="400")



usuario = StringVar()
password = StringVar()


Label(miFrame ,text="USUARIO").grid(row=0, column=0, pady=20, padx=20)
txtUser = Entry(miFrame, textvariable= usuario).grid(row=0, column=1, pady=20, padx=20)

Label(miFrame, text="CONTRASEÑA").grid(row=1, column=0, pady=20, padx=20)
txtPass = Entry(miFrame, textvariable = password).grid(row=1, column=1, pady=20, padx=20)




btnIngresar = Button(miFrame, text='INGRESAR',  command= validar).grid(row=2, column=1, pady=20, padx=20)




raiz.mainloop()





   




