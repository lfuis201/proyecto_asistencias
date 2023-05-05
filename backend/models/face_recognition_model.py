from backend.models.postgres_pool_connection import PostgresPool

from flask import jsonify

class Face_Recognition_Model:
    def __init__(self):        
        self.mysql_pool = PostgresPool()
    
    def get_photo_user(self,id_usuario):
        params = {'id_usuario' : id_usuario}      
        rv = self.mysql_pool.execute("SELECT foto from usuario where id_usuario=%(id_usuario)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'foto': result[0]}
            data.append(content)
            content = {}
        return data
        