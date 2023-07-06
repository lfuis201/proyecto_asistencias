from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_profesor_model import ProfesorModel
from backend.models.mysql_user_model import UserModel

import requests
import json

model = UserModel()

model_profesor = ProfesorModel()
profesor_blueprint = Blueprint('profesor_blueprint',__name__)

@profesor_blueprint.route('/get_profesores',methods=['GET'])
@cross_origin()
def get_profesors():
    content = model_profesor.get_profesores()
    return jsonify(content) 

@profesor_blueprint.route('/get_profesor',methods=['GET'])
@cross_origin()
def get_profesor():
    return jsonify(model_profesor.get_profesor(int(request.json['id_profesor'])))


@profesor_blueprint.route('/create_profesor',methods=['POST'])
@cross_origin()
def insert_profesor():
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
    
    content = model_profesor.insert_profesor(request.form['nickname']
                                , request.form['password'], request.form['nombre']
                                , request.form['apellido'], request.form['edad']
                                , request.form['genero'], request.form['correo_electronico']
                                , request.form['telefono'],request.form['direccion'],request.form['dni']
                                ,vector,request.form['departamento'])
    
    dni = request.form['dni']
    
    model.subir_foto(f_save,dni)
    
    return jsonify(content)

@profesor_blueprint.route('/update_profesor',methods=['PATCH'])
@cross_origin()
def update_profesor():
    
    id_profesor = request.form['id_profesor']
    
    id_user = model_profesor.get_profesor_userid(id_profesor)[0].get("id_usuario")

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
    
    content = model_profesor.update_profesors( request.form['nickname']
                                , request.form['password'], request.form['nombre']
                                , request.form['apellido'], request.form['edad']
                                , request.form['genero'], request.form['correo_electronico']
                                , request.form['telefono'], request.form['direccion'],vector
                                , id_profesor, request.form['departamento'],id_user)    
    
    model.subir_foto(f_save,dni)
    
    
    return jsonify(content)


@profesor_blueprint.route('/delete_profesor', methods=['DELETE'])
@cross_origin()
def delete_profesor():
    return jsonify(model_profesor.delete_profesors(int(request.json['id_profesor'])))