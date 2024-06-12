import sqlite3 
from pathlib import Path
ROOT_PATH = Path(__file__).parent
con = sqlite3.connect(ROOT_PATH / 'MeuBanco.db')
cur = con.cursor()


def Createtable(con):
    con.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

def InsertRegister(cur, con, data):
    try:
        cur.execute("INSERT INTO clientes ( nome, email) VALUES (?,?);", (data))
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def Updateregister(cur, con, data):
    data = ('hercules herculano', 'josehercules@herculindo.com')
    try:
        cur.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = 1", data)
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def Deleteregister(cur, con, data):
    try:
        cur.execute("DELETE FROM clientes WHERE id = ?", data)
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def InsertMany(cur, con, dados):
    try:
        cur.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', dados)
        con.commit()
    except Exception as e:
        print(f"Current error: {e}")

def Search_Client(cur, data):
    cur.row_factory = sqlite3.Row
    try:
        cur.execute("SELECT * FROM clientes WHERE id=?", (data))
        return cur.fetchone()
    except Exception as e:
        print(f"Current error: {e}")

def List_Clients(cur):
    try:
        return cur.execute("SELECT * FROM clientes")
    except Exception as e:
        print(f"Current error: {e}")

cliente = Search_Client(cur, (2,))
print(dict(cliente))

