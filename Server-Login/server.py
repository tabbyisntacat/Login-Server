import sqlite3
import hashlib
import socket
import threading

print("Server starting")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("Localhost", 9999))



server.listen()
print("server started")

def Handle_Connection(c):
    username = c.recv(1024).decode()
    password  = c.recv(1024)
    print(f'Recived username {username}')
    print(f"Recicved password {password}")
    password = hashlib.sha256(password).hexdigest()
    print(f"Hashed password {password}")

    conn = sqlite3.connect("Data/userdata.db")
    cur = conn.cursor()

    cur.execute("SELECT  * FROM userdata WHERE USERNAME = ? AND PASSWORD = ?", (username, password  ))

    if cur.fetchall():
        c.send("logged in".encode())
    else:
        c.send("login failed".encode())



while True:
    client,addr = server.accept()
    threading.Thread(target=Handle_Connection,args=(client,)).start()
