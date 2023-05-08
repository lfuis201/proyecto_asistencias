from backend.models.postgres_pool_connection import PostgresPool

class AlumnoSeccionModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
    def get_AlumnoSeccion(self, id_alumno_seccion):  
        params = {'id_alumno_seccion' : id_alumno_seccion}  
        rv = self.mysql_pool.execute("SELECT * from alumno_seccion where alumno_seccion.id_alumno_seccion=%(id_alumno_seccion)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_alumno_seccion':result[0],
                    'id_alumno':result[1],
                    'id_seccion':result[2]
                    }
            data.append(content)
            content = {}
        return data
    
    def get_AlumnoSecciones(self):
        query=self.mysql_pool.execute("SELECT * from alumno_seccion")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_alumno_seccion':row[0],
                'id_alumno':row[1],
                'id_seccion':row[2]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_alumno_seccion(self,id_alumno,id_seccion):
        entrada = {
            'id_alumno':id_alumno,
            'id_seccion':id_seccion
            }

        query ="""insert into alumno_seccion(id_alumno,id_seccion)
         values(%(id_alumno)s,%(id_seccion)s);"""
        cursor = self.mysql_pool.execute(query,entrada,commit=True)
        salida = {
            "id_alumno":id_alumno,
            "message":"Alumno_Seccion OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_alumno_seccion(self, id_alumno_seccion, id_alumno,id_seccion):    
        data = {
            'id_alumno_seccion' : id_alumno_seccion,
            'id_alumno': id_alumno,
            'id_seccion':id_seccion
        }  
        query = """update alumno_seccion set id_alumno = %(id_alumno)s, id_seccion = %(id_seccion)s
                     where id_alumno_seccion = %(id_alumno_seccion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_alumno_seccion(self, id_alumno_seccion):    
        params = {'id_alumno_seccion' : id_alumno_seccion}      
        query = """delete from alumno_seccion where id_alumno_seccion = %(id_alumno_seccion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data