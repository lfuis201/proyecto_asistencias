from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_profesor_model import ProfesorModel


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
    content=model_profesor.insert_profesor(
        request.json['departamento'],
        request.json['id_usuario']
    )
    return jsonify(content)

@profesor_blueprint.route('/update_profesor',methods=['PATCH'])
@cross_origin()
def update_profesor():
    content=model_profesor.update_profesors(
        request.json['id_profesor'],
        request.json['departamento']
    )
    return jsonify(content)


@profesor_blueprint.route('/delete_profesor', methods=['DELETE'])
@cross_origin()
def delete_profesor():
    return jsonify(model_profesor.delete_profesors(int(request.json['id_profesor'])))