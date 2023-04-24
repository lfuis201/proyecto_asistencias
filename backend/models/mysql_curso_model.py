from backend.models.mysql_pool_connection import MySQLPool

class CursoModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_curso(self, id_curso):    
        params = {'id_curso' : id_curso}      
        rv = self.mysql_pool.execute("SELECT * from curso where id_curso=%(id_curso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_curso': result[0], 'nombre_curso': result[1], 'descripcion': result[2]}
            data.append(content)
            content = {}
        return data

    def get_cursos(self):  
        rv = self.mysql_pool.execute("SELECT * from curso")  
        data = []
        content = {}
        for result in rv:
            content = {'id_curso': result[0], 'nombre_curso': result[1], 'descripcion': result[2]}
            data.append(content)
            content = {}
        return data

    def create_curso(self, nombre_curso, descripcion):    
        data = {
            'nombre_curso' : nombre_curso,
            'descripcion' : descripcion
        }
        
        query = """insert into curso (nombre_curso, descripcion) 
            values (%(nombre_curso)s, %(descripcion)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_curso'] = cursor.lastrowid
        return data

    def update_curso (self,id_curso,nombre_curso, descripcion):    
        data = {
            'id_curso' : id_curso,
            'nombre_curso' : nombre_curso,
            'descripcion' : descripcion
        }  
        query = """update curso set nombre_curso = %(nombre_curso)s, descripcion = %(descripcion)s,
                    where id_curso = %(id_curso)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_curso(self, id_curso):    
        params = {'id_curso' : id_curso}      
        query = """delete from curso where id_curso = %(id_curso)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result

if __name__ == "__main__":    
    cm = CursoModel()

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    #print(tm.delete_task(67))
    #print(tm.get_tasks())
    print(cm.create_curso('nombrecurso2', 'descripcion2'))