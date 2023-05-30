import sqlite3
from tkinter import ttk
from tkinter import *

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def insert( id, task, time, status):
    conexao = sqlite3.connect("dadosUsuarios.db")
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    Tarefas(itemId TEXT, itemTask TEXT, itemTime TEXT, itemStatus TEXT)""")

    cursor.execute("INSERT INTO Tarefas VALUES ('" + str(id) + "','" + str(task) + "','" + str(time) + "','" + str(status) + "')")
    conexao.commit()


def delete(data):
    conexao = sqlite3.connect("dadosUsuarios.db")
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        Tarefas(itemId TEXT, itemTask TEXT, itemTime TEXT, itemStatus TEXT)""")

    cursor.execute("DELETE FROM Tarefas WHERE itemId = '" + str(data) + "'")
    conexao.commit()


def update(id, task, time, status,  idTask):
    conexao = sqlite3.connect("dadosUsuarios.db")
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        Tarefas(itemId TEXT, itemTask TEXT, itemTime TEXT, itemStatus TEXT)""")

    cursor.execute("UPDATE Tarefas SET itemId = '" + str(id) + "', itemTask = '" + str(task) + "', itemTime = '" + str(time) + "', itemStatus = '" + str(status) + "' WHERE itemId='"+str(idTask)+"'")
    conexao.commit()


def read():
    conexao = sqlite3.connect("dadosUsuarios.db")
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        Tarefas(itemId TEXT, itemTask TEXT, itemTime TEXT, itemStatus TEXT)""")

    cursor.execute("SELECT * FROM Tarefas")
    results = cursor.fetchall()
    conexao.commit()
    return results


def insert_data():
    itemId = str(entryId.get())
    itemTask = str(entryTask.get())
    itemTime = str(entryTime.get())
    itemStatus= str(entryStatus.get())
    if itemId == "" or itemTask == " ":
        print("Error Inserting Id")
    if itemTask == "" or itemTask == " ":
        print("Error Inserting Task")
    if itemTime == "" or itemTime == " ":
        print("Error Inserting Time")
    if itemStatus == "" or itemStatus == " ":
        print("Error Inserting Status")
    else:
        insert(str(itemId), str(itemTask), str(itemTime), str(itemStatus))

    for data in tree.get_children():
        tree.delete(data)

    for result in reverse(read()):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    tree.tag_configure('orow', background='#EEEEEE')
    tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


def delete_data():
    selected_item = tree.selection()[0]
    deleteData = str(tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in tree.get_children():
        tree.delete(data)

    for result in reverse(read()):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    tree.tag_configure('orow', background='#EEEEEE')
    tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def update_data():
    selected_item = tree.selection()[0]
    update_task = tree.item(selected_item)['values'][0]
    update(entryId.get(), entryTask.get(), entryTime.get(), entryStatus.get(), update_task)

    for data in tree.get_children():
        tree.delete(data)

    for result in reverse(read()):
        tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    tree.tag_configure('orow', background='#EEEEEE')
    tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)




window = Tk()
window.title("Agenda")
window.geometry("850x250")
tree = ttk.Treeview(window)

idLabel = Label(window, text="Prioridade")
taskLabel = Label(window,text="Tarefa")
timeLabel = Label(window, text="Horário")
statusLabel = Label(window, text="Status")
idLabel.grid(row=1, column=0, padx=10, pady=10)
taskLabel.grid(row=2, column=0, padx=10, pady=10)
timeLabel.grid(row=3, column=0, padx=10, pady=10)
statusLabel.grid(row=4, column=0, padx=10, pady=10)

entryId = Entry(window, width=25, bd=5)
entryTask = Entry(window, width=25, bd=5)
entryTime = Entry(window, width=25, bd=5)
entryStatus = Entry(window, width=25, bd=5)
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryTask.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryTime.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryStatus.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

buttonInsert = Button(
    window, text="Inserir", padx=5, pady=5, width=5,
    bd=3, bg="lime green", command=insert_data)
buttonInsert.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    window, text="Editar", padx=5, pady=5, width=5,
    bd=3, bg="gold", command=update_data)
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonRemove = Button(
    window, text="Remover", padx=5, pady=5, width=5,
    bd=3, bg="red", command=delete_data)
buttonRemove.grid(row=5, column=3, columnspan=1)

tree['columns'] = ("ID", "Tarefa", "Time", "Status")
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=W, width=100)
tree.column("Tarefa", anchor=W, width=200)
tree.column("Time", anchor=W, width=150)
tree.column("Status", anchor=W, width=150)
tree.heading("ID", text="Prioridade", anchor=W)
tree.heading("Tarefa", text="Tarefa", anchor=W)
tree.heading("Time", text="Horário", anchor=W)
tree.heading("Status", text="Status", anchor=W)

for data in tree.get_children():
    tree.delete(data)

for result in reverse(read()):
    tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

tree.tag_configure('orow', background='#EEEEEE')
tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

window.mainloop()