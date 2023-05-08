from backend.models.postgres_pool_connection import PostgresPool

class AsistenciaModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
    def get_Asistencia(self, id_asistencia):  
        params = {'id_asistencia' : id_asistencia}  
        rv = self.mysql_pool.execute("SELECT * from asistencia where id_asistencia=%(id_asistencia)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_asistencia':result[0],
                    'estado':result[1],
                    'fecha':result[2],
                    'id_horario':result[3],
                    'vector_comparacion':result[4],
                    'foto':result[5],
                    'dni':result[6]
            }
            data.append(content)
            content = {}
        return data
    
    def get_asistencias(self):
        query=self.mysql_pool.execute("SELECT * from asistencia")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_asistencia':row[0],
                'estado':row[1],
                'fecha':row[2],
                'id_horario':row[3],
                'vector_comparacion':row[4],
                'foto':row[5],
                'dni':row[6]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_asistencias(self,estado,fecha,id_horario,vector_comparacion,foto,dni):
        entrada = {
            'estado':estado,
            'fecha':fecha,
            'id_horario':id_horario,
            'vector_comparacion':vector_comparacion,
            'foto':foto,
            'dni':dni
            }

        query ="""insert into asistencia(estado,fecha,id_horario,vector_comparacion,foto,dni)
         values(%(estado)s,%(fecha)s,%(id_horario)s,%(vector_comparacion)s,%(foto)s,%(dni)s);"""
        cursor = self.mysql_pool.execute(query,entrada,commit=True)
        salida = {
            "id_horario":id_horario,
            "message":"Asistencia OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_asistencia(self, id_asistencia, estado, fecha,id_horario,vector_comparacion,foto):    
        data = {
            'id_asistencia' : id_asistencia,
            'estado' : estado,
            'fecha': fecha,
            'id_horario':id_horario,
            'vector_comparacion':vector_comparacion,
            'foto':foto
        }  
        query = """update asistencia set estado = %(estado)s, fecha = %(fecha)s, id_horario =%(id_horario)s,
                    vector_comparacion=%(vector_comparacion)s,foto=%(foto)s
                     where id_asistencia = %(id_asistencia)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_asistencia(self, id_asistencia):    
        params = {'id_asistencia' : id_asistencia}      
        query = """delete from asistencia where id_asistencia = %(id_asistencia)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data