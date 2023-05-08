from backend.models.postgres_pool_connection import PostgresPool

class HorarioModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
        
    def get_horario(self, id_horario):  
        params = {'id_horario' : id_horario}  
        rv = self.mysql_pool.execute("SELECT h.id_horario,h.num_horas,h.descripcion,h.hora_inicio,h.hora_fin,h.dia_semana,s.nombre_seccion,s.aula  from horario h inner join seccion s on h.id_seccion = s.id_seccion  where h.id_horario=%(id_horario)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_horario':result[0],
                    'num_horas':result[1],
                    'descripcion':result[2],
                    'hora_inicio':str(result[3]),
                    'hora_fin':str(result[4]),
                    'dia_semana':result[5],
                    'nombre_seccion':result[6],
                    'aula':result[7],
                    }
            data.append(content)
            content = {}
        return data
    
    def get_horarios(self):
        query=self.mysql_pool.execute("SELECT * from horario")
        data = []
        contenido={}
        for row in query:
            contenido={
                'id_horario':row[0],
                'num_horas':row[1],
                'descripcion':row[2],
                'hora_inicio':str(row[3]),
                'hora_fin':str(row[4]),
                'dia_semana':row[5],
                'id_seccion':row[6]
            }
            data.append(contenido)
            contenido={}
        return data    

    def insert_horarios(self,num_horas,descripcion,hora_inicio,hora_fin,dia_semana,id_seccion):
        entrada = {
            'num_horas':num_horas,
            'descripcion':descripcion,
            'hora_inicio':hora_inicio,
            'hora_fin':hora_fin,
            'dia_semana':dia_semana,
            'id_seccion':id_seccion
            }

        query ="""insert into horario(num_horas,descripcion,hora_inicio,hora_fin,dia_semana,id_seccion)
         values(%(num_horas)s,%(descripcion)s,%(hora_inicio)s,%(hora_fin)s,%(dia_semana)s,%(id_seccion)s)"""
        cursor = self.mysql_pool.execute(query,entrada,commit=True)
        salida = {
            "id_seccion":id_seccion,
            "message":"Horario OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_horarios(self, id_horario, num_horas, descripcion,hora_inicio,hora_fin,dia_semana,id_seccion):    
        data = {
            'id_horario' : id_horario,
            'num_horas' : num_horas,
            'descripcion': descripcion,
            'hora_inicio':hora_inicio,
            'hora_fin':hora_fin,
            'dia_semana':dia_semana,
            'id_seccion':id_seccion
        }  
        query = """update horario set num_horas = %(num_horas)s, descripcion = %(descripcion)s, hora_inicio =%(hora_inicio)s,
                    hora_fin=%(hora_fin)s,dia_semana=%(dia_semana)s, id_seccion=%(id_seccion)s
                     where id_horario = %(id_horario)s """    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result


    def delete_horarios(self, id_horario):    
        params = {'id_horario' : id_horario}      
        query = """delete from horario where id_horario = %(id_horario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data