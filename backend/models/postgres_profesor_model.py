from backend.models.postgres_pool_connection import PostgresPool

class ProfesorModel:
    def __init__(self):        
        self.postgres_pool = PostgresPool()
        
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
        query=self.postgres_pool.execute("""select a.id_profesor,a.departamento,u.nombre,u.apellido from profesor a inner join usuario u on a.id_profesor=u.id_usuario""")
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

    def insert_profesor(self,departamento,id_usuario):
        entrada = {
            'departamento':departamento,
            'id_usuario':id_usuario
            }

        query ="""insert into profesor(departamento,id_usuario)
         values(%(departamento)s,%(id_usuario)s);"""
        cursor = self.postgres_pool.execute(query,entrada,commit=True)
        salida = {
            "id_profesor":cursor.lastrowid,
            "message":"Usuario OK"
        }
#        global llave_usuario
#        llave_usuario = cursor.lastrowid
        return salida


    def update_profesors(self, id_profesor, departamento):    
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