from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from os import remove
import requests
import os
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_user_model import UserModel
model = UserModel()


user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/user', methods=['PUT'])
@cross_origin()
def create_user():
    
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
    
    content = model.create_user(request.form['nickname']
                                , request.form['password'], request.form['nombre']
                                , request.form['apellido'], request.form['edad']
                                , request.form['genero'], request.form['correo_electronico']
                                , request.form['telefono'],request.form['direccion'],request.form['dni'],vector)
    
    dni = request.form['dni']
    
    model.subir_foto(f_save,dni)
    return jsonify(content)

@user_blueprint.route('/user', methods=['PATCH'])
@cross_origin()
def update_user():
    id_user = request.form['id_usuario']
    
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
    
    content = model.update_user(request.form['id_usuario'], request.form['nickname']
                                , request.form['password'], request.form['nombre']
                                , request.form['apellido'], request.form['edad']
                                , request.form['genero'], request.form['correo_electronico']
                                , request.form['telefono'], request.form['direccion'],vector)    
    
    model.subir_foto(f_save,dni)
    
    return jsonify(content)

@user_blueprint.route('/user', methods=['DELETE'])
@cross_origin()
def delete_user():
    return jsonify(model.delete_user(int(request.json['id_usuario'])))

@user_blueprint.route('/user', methods=['POST'])
@cross_origin()
def get_user():
    return jsonify(model.get_user(int(request.json['id_usuario'])))

@user_blueprint.route('/users', methods=['POST'])
@cross_origin()
def get_users():
    return jsonify(model.get_users())