from backend.models.postgres_pool_connection import PostgresPool

class SeccionProfesorModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
    def get_SeccionProfesor(self, id_seccion_profesor):  
        params = {'id_seccion_profesor' : id_seccion_profesor}  
        rv = self.mysql_pool.execute("SELECT * from seccion_profesor where seccion_profesor.id_seccion_profesor=%(id_seccion_profesor)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_seccion_profesor':result[0],
                    'id_profesor':result[1],
                    'id_seccion':result[2]
                    }
            data.append(content)
            content = {}
        return data
    
    def get_SeccionProfesores(self):
        query=self.mysql_pool.execute("SELECT * from seccion_profesor")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_seccion_profesor':row[0],
                'id_profesor':row[1],
                'id_seccion':row[2]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_SeccionProfesor(self,id_profesor,id_seccion):
        entrada = {
            'id_profesor':id_profesor,
            'id_seccion':id_seccion
            }

        query ="""insert into seccion_profesor(id_profesor,id_seccion)
         values(%(id_profesor)s,%(id_seccion)s);"""
        cursor = self.mysql_pool.execute(query,entrada,commit=True)
        salida = {
            "id_profesor":id_profesor,
            "message":"Profesor_Seccion OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_SeccionProfesor(self, id_seccion_profesor, id_profesor,id_seccion):    
        data = {
            'id_seccion_profesor' : id_seccion_profesor,
            'id_profesor': id_profesor,
            'id_seccion':id_seccion
        }  
        query = """update seccion_profesor set id_profesor = %(id_profesor)s, id_seccion = %(id_seccion)s
                     where id_seccion_profesor = %(id_seccion_profesor)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_SeccionProfesor(self, id_seccion_profesor):    
        params = {'id_seccion_profesor' : id_seccion_profesor}      
        query = """delete from seccion_profesor where id_seccion_profesor = %(id_seccion_profesor)s"""    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data