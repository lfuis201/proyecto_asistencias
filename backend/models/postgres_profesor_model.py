from backend.models.postgres_pool_connection import PostgresPool

class ProfesorModel:
    def __init__(self):        
        self.postgres_pool = PostgresPool()
        
    def get_userid(self, dni):
        params = {'dni' : dni}      
        rv = self.postgres_pool.execute("SELECT id_usuario from usuario where dni="+"\'"+dni+"\';", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0]}
            data.append(content)
            content = {}
        return data
    
    def get_profesor_userid(self, id):
        params = {'id_profesor' : id}      
        rv = self.postgres_pool.execute("SELECT id_usuario from profesor where id_profesor="+"\'"+id+"\';", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0]}
            data.append(content)
            content = {}
        return data
    
    def get_profesor(self, id_profesor):  
        params = {'id_profesor' : id_profesor}  
        rv = self.postgres_pool.execute("SELECT id_profesor,nombre,apellido,departamento,nickname from profesor  join usuario on profesor.id_usuario = usuario.id_usuario  where profesor.id_profesor=%(id_profesor)s;", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_profesor':result[0],
                'nombre':result[1],
                'apellido':result[2],
                'departamento':result[3],
                'nickname':result[4]}
            data.append(content)
            content = {}
        return data
    
    def get_profesores(self):
        query=self.postgres_pool.execute("""select a.id_profesor,a.departamento,u.nombre,u.apellido from profesor a inner join usuario u on a.id_usuario=u.id_usuario""")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_profesor':row[0],
                'departamento':row[1],
                'nombre':row[2],
                'apellido':row[3]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_profesor(self, nickname, password, nombre, apellido, edad, genero,correo_electronico, telefono, direccion,dni,vector,departamento):
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
        cursor1 = self.postgres_pool.execute(query, data, commit=True)
        
        id_usuario = self.get_userid(dni)[0].get("id_usuario")
        
        entrada = {
            'departamento':departamento,
            'id_usuario':id_usuario
            
        }
        
        query ="""insert into profesor(departamento,id_usuario)
         values(%(departamento)s,%(id_usuario)s);"""
        cursor2 = self.postgres_pool.execute(query,entrada,commit=True)
        salida = {
            "id_usuario":id_usuario,
            "message":"Usuario OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_profesors(self,nickname, password, nombre, apellido, edad, genero,correo_electronico, telefono, direccion,vector,id_profesor,departamento,id_usuario):    
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
        cursor = self.postgres_pool.execute(query, data, commit=True)   
        
        data = {
            'id_profesor' : id_profesor,
            'departamento' : departamento
        }  
        query = """update profesor set departamento = %(departamento)s
                     where id_profesor = %(id_profesor)s"""    
        cursor = self.postgres_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_profesors(self, id_profesor):    
        params = {'id_profesor' : id_profesor}      
        query = """delete from profesor where id_profesor = %(id_profesor)s"""    
        self.postgres_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
    
    