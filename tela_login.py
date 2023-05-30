import tkinter as tk
from tkinter import *
import bancodedados
from tkinter import messagebox

window = Tk()
window.title("Tela Login")
window.geometry("310x130")


def Login():
    Usuario = user.get()
    senha = password.get()


    bancodedados.cursor.execute("""
            SELECT * FROM Usuarios
            WHERE (user=? and password=?)
    """, (Usuario,senha))
    print("FOI")
    
    verify = bancodedados.cursor.fetchone()
    try:
        if(Usuario in verify and senha in verify):
            messagebox.showinfo(title="AUTH", message="Sucesso")
        else:
            pass
    except:
        messagebox.showinfo(title="AUTH", message="Falhou, dados incorretos")

userLabel = Label(window, text="Usuario")
userLabel.grid(row=0, column=0)

passwordLabel = Label(window,text="Senha")
passwordLabel.grid(row=1, column=0)  


user = tk.Entry(bg="white", fg="black",width=40,bd=5)
user.grid(row=0, column=1)  
password = tk.Entry(bg="white", fg="black",width=40, show="*",bd=5)
password.grid(row=1, column=1)

auth_button = tk.Button(
    text="ENTRAR",
    width=20,
    height=2,
    bg="spring green",
    fg="black",
    command=Login
)
auth_button.grid(row=2,column=1)

window.mainloop()