from conector import Conector

class Usuario:
    def __init__(self):
        self.db = Conector()

    def validarUsuario(self, nickname, clave):
        sql = "SELECT * FROM usuarios WHERE nickname=? AND contrasena=?"
        row = self.db.fetchone(sql, (nickname, clave))
        return row

    def registrarUsuario(self, nombres, apellidos, nickname, correo, clave):
        sql = "INSERT INTO usuarios (nombres, apellidos, nickname, correo, contrasena) VALUES (?, ?, ?, ?, ?)"
        self.db.execute(sql, (nombres, apellidos, nickname, correo, clave))

    def listarUsuarios(self):
        sql = "SELECT * FROM usuarios"
        return self.db.fetchall(sql)
