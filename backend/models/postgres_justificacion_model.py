from backend.models.postgres_pool_connection import PostgresPool

class JustificacionModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
    def get_Justificacion(self, id_justificacion):  
        params = {'id_justificacion' : id_justificacion}  
        rv = self.mysql_pool.execute("SELECT j.*, a.fecha FROM justificacion j INNER JOIN asistencia a ON j.id_asistencia = a.id_asistencia WHERE j.id_justificacion = %(id_justificacion)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_justificacion':result[0],
                    'fechar':result[1],
                    'id_asistencia':result[2],
                    'fecha:':result[2]
                    }
            data.append(content)
            content = {}
        return data
    
    def get_Justificaciones(self):
        query=self.mysql_pool.execute("SELECT * from justificacion")
        data = list()
        contenido=dict()
        for row in query:
            contenido={
                'id_justificacion':row[0],
                'fechar':row[1],
                'id_asistencia':row[2]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_justificacion(self,fechar,id_asistencia):
        entrada = {
            'fechar':fechar,
            'id_asistencia':id_asistencia
            }

        query ="""insert into justificacion(fechar,id_asistencia)
         values(%(fechar)s,%(id_asistencia)s);"""
        cursor = self.mysql_pool.execute(query,entrada,commit=True)
        salida = {
            "id_asistencia":id_asistencia,
            "message":"Asistencia OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_justificacion(self, id_justificacion, fechar, id_asistencia):    
        data = {
            'id_justificacion' : id_justificacion,
            'fechar': fechar,
            'id_asistencia':id_asistencia
        }  
        query = """update justificacion set fechar= %(fechar)s, id_asistencia = %(id_asistencia)s
                     where id_justificacion = %(id_justificacion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_justificacion(self, id_justificacion):    
        params = {'id_justificacion' : id_justificacion}      
        query = """delete from justificacion where id_justificacion = %(id_justificacion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   
        data = {'result': 1}
        return data