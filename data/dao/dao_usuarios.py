from data.modelo.usuario import Usuario

class DaoUsuarios:
    
    def get_all(self,db) -> list[Usuario]:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        equipos_en_db = cursor.fetchall()
        equipos : list[Usuario] = list()
        for equipo in equipos_en_db:
            usuario = Usuario(equipo[0],equipo[1])
            print(usuario.nombre)
            equipos.append(usuario)
            print(len(equipos))
        
        cursor.close()
        return equipos
    
    def insert(self, db, id: int, nombre: str):
        cursor = db.cursor()
        sql = "INSERT INTO Usuarios (id, nombre) VALUES (%s, %s)"
        data = (id, nombre)  # Se asegura de incluir tanto ID como Nombre
        cursor.execute(sql, data)
        db.commit()
        cursor.close()

    def delete(self, db, id: str):
        cursor = db.cursor()
        sql = ("DELETE FROM  Usuarios where id = (%s) ")
        data = (id,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO alumnos (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()