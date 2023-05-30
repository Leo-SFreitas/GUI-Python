from tkinter import *
import bancodedados
from tkinter import messagebox

window = Tk()
window.title("Tela de cadastro")
window.geometry("310x150")


nameLabel = Label(window,text="Nome")
nameLabel.grid(row=0, column=0)
name = Entry(bg="white", fg="black",width=40,bd=3)
name.grid(row=0, column=1)

emailLabel = Label(window,text="Email")
emailLabel.grid(row=1, column=0)
email = Entry(bg="white", fg="black",width=40,bd=3)
email.grid(row=1, column=1)

userLabel = Label(window, text="Usuario")
userLabel.grid(row=2, column=0)
user = Entry(bg="white", fg="black",width=40,bd=3)
user.grid(row=2, column=1)

passwordLabel = Label(window,text="Senha")
passwordLabel.grid(row=3, column=0)
password = Entry(bg="white", fg="black",width=40, show="*",bd=3)
password.grid(row=3, column=1)

def registerDB():
    Nome = name.get()
    
    Email = email.get()
    Usuario = user.get()
    senha = password.get()

    bancodedados.cursor.execute("""
        INSERT INTO Usuarios(name, email, user, password) VALUES(?,?,?,?)
    """, (Nome,Email,Usuario,senha))
    bancodedados.conexao.commit()
    messagebox.showinfo(title="Info Cadastro", message="Cadastrado")


register_button = Button(
    text="CADASTRAR",
    width=25,
    height=2,
    bg="dodger blue",
    fg="black",
    command=registerDB
)
register_button.grid(row=4,column=1)

window.mainloop()