from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_alumno_model import AlumnoModel


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
    content=model_alumno.insert_alumnos(
        request.json['carrera'],
        request.json['id_usuario']
    )
    return jsonify(content)

@alumno_blueprint.route('/update_alumnos',methods=['PATCH'])
@cross_origin()
def update_alumn():
    content=model_alumno.update_alumnos(
        request.json['id_alumno'],
        request.json['carrera']
    )
    return jsonify(content)


@alumno_blueprint.route('/delete_alumnos', methods=['DELETE'])
@cross_origin()
def delete_alumn():
    return jsonify(model_alumno.delete_alumnos(int(request.json['id_alumno'])))