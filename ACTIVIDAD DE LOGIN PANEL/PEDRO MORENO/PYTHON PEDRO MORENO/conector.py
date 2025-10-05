import sqlite3

class Conector:
    def __init__(self):
        # Se crea (o abre) el archivo loginapp.db en tu carpeta del proyecto
        self.conn = sqlite3.connect("loginapp.db")
        self.conn.row_factory = sqlite3.Row  # Para que devuelva diccionarios
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        self.conn.commit()

    def fetchall(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()

    def fetchone(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()
