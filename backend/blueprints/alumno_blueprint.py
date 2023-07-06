from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_alumno_model import AlumnoModel

from backend.models.mysql_user_model import UserModel

import requests
import json
model = UserModel()
model_alumno = AlumnoModel()
alumno_blueprint = Blueprint('alumno_blueprint',__name__)

@alumno_blueprint.route('/get_alumnos',methods=['GET'])
@cross_origin()
def get_alumns():
    content = model_alumno.get_alumnos()
    return jsonify(content) 

@alumno_blueprint.route('/get_alumno',methods=['GET'])
@cross_origin()
def get_alumn():
    return jsonify(model_alumno.get_alumno(int(request.json['id_alumno'])))


@alumno_blueprint.route('/create_alumnos',methods=['POST'])
@cross_origin()
def insert_alumn():
    f = request.files['foto']
    filename = f.filename
    f.save("/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos/" +request.form['dni']+ filename)
    
    f_save = ("/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos/" +request.form['dni']+ filename)
    
    url = 'http://0.0.0.0:81/recibir_foto'
    
    img1 = open(f_save, 'rb')
    files = {'file': img1}
    
    response = requests.post(url, files=files)
    json_response=json.loads(response.text)
    vector = json_response["result"]
    
    content = model_alumno.insert_alumnos(request.form['nickname']
                                , request.form['password'], request.form['nombre']
                                , request.form['apellido'], request.form['edad']
                                , request.form['genero'], request.form['correo_electronico']
                                , request.form['telefono'],request.form['direccion'],request.form['dni']
                                ,vector,request.form['carrera'])
    
    dni = request.form['dni']
    
    model.subir_foto(f_save,dni)
    
    return jsonify(content)

@alumno_blueprint.route('/update_alumnos',methods=['PATCH'])
@cross_origin()
def update_alumn():
    id_alumno = request.form['id_alumno']
    
    id_user = model_alumno.get_alumno_userid(id_alumno)[0].get("id_usuario")

    data = model.get_user(id_user)
    
 
    dni = data[0].get("dni")

    f = request.files['foto']
    filename = f.filename
    f.save("/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos/" +dni+ filename)
    
    f_save = ("/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos/" +dni+ filename)
    
    url = 'http://0.0.0.0:81/recibir_foto'
    
    img1 = open(f_save, 'rb')
    files = {'file': img1}
    response = requests.post(url, files=files)
    json_response=json.loads(response.text)
    vector = json_response["result"]
    
    content = model_alumno.update_alumnos( request.form['nickname']
                                , request.form['password'], request.form['nombre']
                                , request.form['apellido'], request.form['edad']
                                , request.form['genero'], request.form['correo_electronico']
                                , request.form['telefono'], request.form['direccion'],vector
                                , id_alumno, request.form['carrera'],id_user)    
    
    model.subir_foto(f_save,dni)
    
    
    return jsonify(content)


@alumno_blueprint.route('/delete_alumnos', methods=['DELETE'])
@cross_origin()
def delete_alumn():
    return jsonify(model_alumno.delete_alumnos(int(request.json['id_alumno'])))