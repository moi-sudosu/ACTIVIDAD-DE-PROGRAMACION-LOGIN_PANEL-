import sqlite3

conn = sqlite3.connect("loginapp.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombres TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    nickname TEXT NOT NULL UNIQUE,
    correo TEXT NOT NULL,
    contrasena TEXT NOT NULL
)
""")

# Usuario de prueba
cursor.execute("INSERT INTO usuarios (nombres, apellidos, nickname, correo, contrasena) VALUES (?, ?, ?, ?, ?)",
               ("Pedro", "Louis", "pedro123", "pedro@example.com", "1234"))

conn.commit()
conn.close()

print("Base de datos creada con usuario de prueba.")
