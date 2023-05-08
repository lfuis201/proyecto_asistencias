from backend.models.postgres_pool_connection import PostgresPool

class ParticipacionModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
    def get_Participacion(self, id_participacion):  
        params = {'id_participacion' : id_participacion}  
        rv = self.mysql_pool.execute("SELECT * from participacion where id_participacion=%(id_participacion)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_participacion':result[0],
                    'fecha':result[1],
                    'participacion':result[2],
                    'id_horario':result[3]
                    }
            data.append(content)
            content = {}
        return data
    
    def get_Partipaciones(self):
        query=self.mysql_pool.execute("SELECT * from participacion")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_participacion':row[0],
                'fecha':row[1],
                'participacion':row[2],
                'id_horario':row[3]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_participacion(self,fecha,participacion,id_horario):
        entrada = {
            'fecha':fecha,
            'participacion':participacion,
            'id_horario':id_horario
            }

        query ="""insert into participacion(fecha,participacion,id_horario)
         values(%(fecha)s,%(participacion)s,%(id_horario)s);"""
        cursor = self.mysql_pool.execute(query,entrada,commit=True)
        salida = {
            "id_horario":id_horario,
            "message":"Participacion OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_participacion(self, id_participacion, fecha, participacion,id_horario):    
        data = {
            'id_participacion' : id_participacion,
            'fecha': fecha,
            'participacion':participacion,
            'id_horario':id_horario
        }  
        query = """update participacion set fecha = %(fecha)s, participacion = %(participacion)s, id_horario =%(id_horario)s
                     where id_participacion = %(id_participacion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_participacion(self, id_participacion):    
        params = {'id_participacion' : id_participacion}      
        query = """delete from participacion where id_participacion = %(id_participacion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data