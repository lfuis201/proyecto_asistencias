from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_user_model import UserModel
model = UserModel()


user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/user', methods=['PUT'])
@cross_origin()
def create_user():
    content = model.create_user(request.json['nickname']
                                , request.json['password'], request.json['nombre']
                                , request.json['apellido'], request.json['edad']
                                , request.json['genero'], request.json['correo_electronico']
                                , request.json['telefono'],request.json['direccion'])       
    return jsonify(content)

@user_blueprint.route('/user', methods=['PATCH'])
@cross_origin()
def update_user():
    content = model.update_user(request.json['id_usuario'], request.json['nickname']
                                , request.json['password'], request.json['nombre']
                                , request.json['apellido'], request.json['edad']
                                , request.json['genero'], request.json['correo_electronico']
                                , request.json['telefono'], request.json['direccion'])    
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