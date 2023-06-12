#from backend.models.mysql_pool_connection import MySQLPool
from backend.models.postgres_pool_connection import PostgresPool


class UserModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()

    def get_user(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        rv = self.mysql_pool.execute("SELECT * from usuario where id_usuario=%(id_usuario)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'nickname': result[1], 'password': result[2]
                       , 'nombre': result[3], 'apellido': result[4], 'edad': result[5]
                       , 'genero': result[6], 'correo': result[7], 'telefono': result[8]
                       , 'direccion': result[9], 'foto': result[10], 'dni': result[11]
                       , 'vector_foto': result[12]}
            data.append(content)
            content = {}
        return data

    def get_users(self):  
        rv = self.mysql_pool.execute("SELECT * from usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'nickname': result[1], 'password': result[2]
                       , 'nombre': result[3], 'apellido': result[4], 'edad': result[5]
                       , 'genero': result[6], 'correo': result[7], 'telefono': result[8]
                       , 'direccion': result[9], 'foto':result[10], 'dni':result[11]
                       , 'vector_foto':result[12]}
            data.append(content)
            content = {}
        return data

    def create_user(self, nickname, password, nombre, apellido, edad, genero,correo_electronico, telefono, direccion,dni,vector):    
        data = {
            'nickname': nickname,
            'password': password,
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad,
            'genero': genero,
            'correo_electronico': correo_electronico,
            'telefono': telefono,
            'direccion': direccion,
            'dni': dni,
            'vector': vector

        }
        
        query = """insert into usuario (nickname, password, nombre, apellido, edad, 
            genero, correo_electronico, telefono, direccion,dni,vector_foto) 
            values (%(nickname)s, %(password)s, %(nombre)s, %(apellido)s, %(edad)s, %(genero)s
            , %(correo_electronico)s, %(telefono)s, %(direccion)s, %(dni)s, %(vector)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        return data
    
    def update_user (self,id_usuario, nickname, password, nombre, apellido, edad, genero,correo_electronico, telefono, direccion,vector):    
        data = {
            'id_usuario' : id_usuario,
            'nickname' : nickname,
            'password' : password,
            'nombre' : nombre,
            'apellido' : apellido,
            'edad' : edad,
            'genero' : genero,
            'correo_electronico' : correo_electronico,
            'telefono' : telefono,
            'direccion' : direccion,
            'vector':vector
        }  
        query = """update usuario set nickname = %(nickname)s, password = %(password)s,
                    nombre= %(nombre)s,apellido= %(apellido)s
                    ,edad= %(edad)s,genero= %(genero)s
                    ,correo_electronico= %(correo_electronico)s
                    ,telefono= %(telefono)s ,direccion= %(direccion)s ,vector_foto= %(vector)s where id_usuario = %(id_usuario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_user(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        query = """delete from usuario where id_usuario = %(id_usuario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

    def get_id(self, dni):
        params = {'dni' : dni}      
        rv = self.mysql_pool.execute("SELECT id_usuario from usuario where dni="+"\'"+dni+"\';", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0]}
            data.append(content)
            content = {}
        return data
        
    def subir_foto(self, foto,dni):
        data = {
            'foto' : foto,
            'dni' : dni
        }
        query = """update usuario set foto= %(foto)s where dni = %(dni)s;"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)
        return data

    def get_photo_by_dni(self,dni):
        params = {'dni' : dni}      
        rv = self.mysql_pool.execute("SELECT foto from usuario where dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'foto': result[0]}
            data.append(content)
            content = {}
        return data


if __name__ == "__main__":    
    um = UserModel()

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    #print(um.get_users())
    #print(um.get_id('patrick')[0].get("id_usuario"))
    foto = um.get_photo_by_dni("75575456")[0].get("foto")
    print(foto)
    print(type(foto))
    #print(um.create_user('nick2', 'password2', 'nomb2','apellido2',20,'M','correo2','tel2','dir2'))
