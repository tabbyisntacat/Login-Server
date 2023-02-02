import sqlite3
import hashlib



conn = sqlite3.connect("Data/userdata.db")
cur = conn.cursor()



cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
     id INTEGER PRIMARY KEY,
     username VARCHAR(255) NOT NULL,
     password VARCHAR(255) NOT NULL

)
""")


username1,Password1 = "Tabby", hashlib.sha256("TabbyPassword".encode()).hexdigest()
username2,Password2 = "Strikeman", hashlib.sha256("strikemanpass".encode()).hexdigest()
username3,Password3 = "towtap", hashlib.sha256("towtappassword".encode()).hexdigest()
username4,Password4 = "AAAA", hashlib.sha256("AAApassword".encode()).hexdigest()
username5,Password5 = "Tabby3", hashlib.sha256("Tabby3Password".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (? , ?) ",(username1, Password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (? , ?) ",(username2, Password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (? , ?) ",(username3, Password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (? , ?)", (username4, Password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (? , ?) ",(username5, Password5))



conn.commit()