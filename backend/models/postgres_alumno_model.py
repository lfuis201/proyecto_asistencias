from backend.models.postgres_pool_connection import PostgresPool

class AlumnoModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
        
    def get_id_alumno_por_dni(self, dni):
        params = {'dni': dni}
        rv = self.mysql_pool.execute("SELECT id_alumno FROM alumno WHERE id_usuario IN (SELECT id_usuario FROM usuario WHERE dni = %(dni)s)", params)
        data = []
        content = {}
        for result in rv:
            content = {'id_alumno': result[0]}
            data.append(content)
            content = {}
        return data
            
    def get_userid(self, dni):
        params = {'dni' : dni}      
        rv = self.mysql_pool.execute("SELECT id_usuario from usuario where dni="+"\'"+dni+"\';", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0]}
            data.append(content)
            content = {}
        return data
    
    def get_alumno_userid(self, id):
        params = {'id_alumno' : id}      
        rv = self.mysql_pool.execute("SELECT id_usuario from alumno where id_alumno="+"\'"+id+"\';", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0]}
            data.append(content)
            content = {}
        return data
    
    def get_alumno(self, id_alumno):  
        params = {'id_alumno' : id_alumno}  
        rv = self.mysql_pool.execute("SELECT id_alumno,nombre,apellido,carrera,nickname from alumno  join usuario on alumno.id_usuario = usuario.id_usuario  where alumno.id_alumno=%(id_alumno)s;", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_alumno':result[0],
                'nombre':result[1],
                'apellido':result[2],
                'carrera':result[3],
                'nickname':result[4]}
            data.append(content)
            content = {}
        return data
    
    def get_alumnos(self):
        query=self.mysql_pool.execute("""select a.id_alumno,a.carrera,u.nombre,u.apellido,u.id_usuario from alumno a inner join usuario u on a.id_usuario=u.id_usuario""")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_alumno':row[0],
                'carrera':row[1],
                'nombre':row[2],
                'apellido':row[3],
                'id_usuario':row[4],
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_alumnos(self,nickname, password, nombre, apellido, edad, genero,correo_electronico, telefono, direccion,dni,vector,carrera):
        
        data = {
            'nickname' : nickname,
            'password' : password,
            'nombre' : nombre,
            'apellido' : apellido,
            'edad' : edad,
            'genero' : genero,
            'correo_electronico' : correo_electronico,
            'telefono' : telefono,
            'direccion' : direccion,
            'dni':dni,
            'vector':vector

        }
        
        
        query = """insert into usuario (nickname, password, nombre, apellido, edad, 
            genero, correo_electronico, telefono, direccion,dni,vector_foto) 
            values (%(nickname)s, %(password)s, %(nombre)s, %(apellido)s, %(edad)s, %(genero)s
            , %(correo_electronico)s, %(telefono)s, %(direccion)s, %(dni)s, %(vector)s)"""    
        cursor1 = self.mysql_pool.execute(query, data, commit=True)
        
        id_usuario = self.get_userid(dni)[0].get("id_usuario")
        
        entrada = {
            'carrera':carrera,
            'id_usuario':id_usuario
            }

        query ="""insert into alumno(carrera,id_usuario)
         values(%(carrera)s,%(id_usuario)s);"""
        cursor = self.mysql_pool.execute(query,entrada,commit=True)
        salida = {
            "id_usuario":id_usuario,
            "message":"Usuario OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_alumnos(self,nickname, password, nombre, apellido, edad, genero,correo_electronico, telefono, direccion,vector,id_alumno, carrera,id_usuario):    
        data = {
            
            'nickname' : nickname,
            'password' : password,
            'nombre' : nombre,
            'apellido' : apellido,
            'edad' : edad,
            'genero' : genero,
            'correo_electronico' : correo_electronico,
            'telefono' : telefono,
            'direccion' : direccion,
            'vector':vector,
            'id_usuario':id_usuario
        }
        
        
        query = """update usuario set nickname = %(nickname)s, password = %(password)s,
                    nombre= %(nombre)s,apellido= %(apellido)s
                    ,edad= %(edad)s,genero= %(genero)s
                    ,correo_electronico= %(correo_electronico)s
                    ,telefono= %(telefono)s ,direccion= %(direccion)s ,vector_foto= %(vector)s where id_usuario = %(id_usuario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   
        
        
        data = {
            'id_alumno' : id_alumno,
            'carrera' : carrera
        }  
        query = """update alumno set carrera = %(carrera)s
                     where id_alumno = %(id_alumno)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_alumnos(self, id_alumno):    
        params = {'id_alumno' : id_alumno}      
        query = """delete from alumno where id_alumno = %(id_alumno)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data