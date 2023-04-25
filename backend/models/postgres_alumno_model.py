from backend.models.postgres_pool_connection import PostgresPool

class AlumnoModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
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
        query=self.mysql_pool.execute("""select a.id_alumno,a.carrera,u.nombre,u.apellido from alumno a inner join usuario u on a.id_usuario=u.id_usuario""")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_alumno':row[0],
                'carrera':row[1],
                'nombre':row[2],
                'apellido':row[3]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_alumnos(self,carrera,id_usuario):
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


    def update_alumnos(self, id_alumno, carrera):    
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