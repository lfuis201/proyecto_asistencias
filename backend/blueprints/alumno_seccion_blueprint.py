from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_alumno_seccion_model import AlumnoSeccionModel


model_alumnoseccion = AlumnoSeccionModel()
alumnoseccion_blueprint = Blueprint('alumnoseccion_blueprint',__name__)

@alumnoseccion_blueprint.route('/get_alumnoseccion',methods=['GET'])
@cross_origin()
def get_alumnoseccion():
    content = model_alumnoseccion.get_AlumnoSecciones()
    return jsonify(content) 

@alumnoseccion_blueprint.route('/buscar_alumnoseccion',methods=['GET'])
@cross_origin()
def get_horario():
    return jsonify(model_alumnoseccion.get_AlumnoSeccion(int(request.json['id_alumno_seccion'])))


@alumnoseccion_blueprint.route('/create_alumnoseccion',methods=['POST'])
@cross_origin()
def insert_asistencia():
    content=model_alumnoseccion.insert_alumno_seccion(
        request.json['id_alumno'],
        request.json['id_seccion']
    )
    return jsonify(content)

@alumnoseccion_blueprint.route('/update_alumnoseccion',methods=['PATCH'])
@cross_origin()
def update_asistencia():
    content=model_alumnoseccion.update_alumno_seccion(
        request.json['id_alumno_seccion'],
        request.json['id_alumno'],
        request.json['id_seccion']
    )
    return jsonify(content)


@alumnoseccion_blueprint.route('/delete_alumnoseccion', methods=['DELETE'])
@cross_origin()
def delete_asistencia():
    return jsonify(model_alumnoseccion.delete_alumno_seccion(int(request.json['id_alumno_seccion'])))