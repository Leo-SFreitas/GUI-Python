import sqlite3

conexao = sqlite3.connect('dadosUsuarios.db')

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
      id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      user TEXT NOT NULL,
      password TEXT NOT NULL
    );
""")

print("\nconectado ao banco de dados\n")
conexao.commit()