
#from backend.models.mysql_pool_connection import MySQLPool
from backend.models.postgres_pool_connection import PostgresPool

class SeccionModel:
    def __init__(self):        
        self.mysql_pool = PostgresPool()

    def get_seccion(self, id_seccion):    
        params = {'id_seccion' : id_seccion}      
        rv = self.mysql_pool.execute("SELECT * from seccion where id_seccion=%(id_seccion)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_seccion': result[0], 'nombre_seccion': result[1], 'aula': result[2], 'id_curso': result[3]}
            data.append(content)
            content = {}
        return data

    def get_seccions(self):  
        rv = self.mysql_pool.execute("SELECT * from seccion")  
        data = []
        content = {}
        for result in rv:
            content = {'id_seccion': result[0], 'nombre_seccion': result[1], 'aula': result[2], 'id_curso': result[3]}
            data.append(content)
            content = {}
        return data

    def create_seccion(self, nombre_seccion, aula, id_curso):    
        data = {
            'nombre_seccion' : nombre_seccion,
            'aula' : aula,
            'id_curso' : id_curso
        }
        
        query = """insert into seccion (nombre_seccion, aula, id_curso) 
            values (%(nombre_seccion)s, %(aula)s, %(id_curso)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        return data

    def update_seccion (self,id_seccion, nombre_seccion, aula, id_curso):    
        data = {
            'id_seccion' : id_seccion,
            'nombre_seccion' : nombre_seccion,
            'aula' : aula,
            'id_curso' : id_curso
        }  
        query = """update seccion set nombre_seccion = %(nombre_seccion)s, aula = %(aula)s,
                    id_curso= %(id_curso)s where id_seccion = %(id_seccion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_seccion(self, id_seccion):    
        params = {'id_seccion' : id_seccion}      
        query = """delete from seccion where id_seccion = %(id_seccion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



if __name__ == "__main__":    
    sm = SeccionModel()

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    print(sm.create_seccion('seccion1', 'aula1', 1))