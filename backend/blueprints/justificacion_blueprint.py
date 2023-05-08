from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_justificacion_model import JustificacionModel


model_justificacion = JustificacionModel()
justificacion_blueprint = Blueprint('justificacion_blueprint',__name__)

@justificacion_blueprint.route('/get_justificacion',methods=['GET'])
@cross_origin()
def get_justificacion():
    content = model_justificacion.get_Justificaciones()
    return jsonify(content) 

@justificacion_blueprint.route('/buscar_justificacion',methods=['GET'])
@cross_origin()
def get_justificaciones():
    return jsonify(model_justificacion.get_Justificacion(int(request.json['id_justificacion'])))


@justificacion_blueprint.route('/create_justificacion',methods=['POST'])
@cross_origin()
def insert_justificacion():
    content=model_justificacion.insert_justificacion(
        request.json['fechar'],
        request.json['id_asistencia']
    )
    return jsonify(content)

@justificacion_blueprint.route('/update_justificacion',methods=['PATCH'])
@cross_origin()
def update_justificacion():
    content=model_justificacion.update_justificacion(
        request.json['id_justificacion'],
        request.json['fechar'],
        request.json['id_justificacion']
    )
    return jsonify(content)


@justificacion_blueprint.route('/delete_justificacion', methods=['DELETE'])
@cross_origin()
def delete_justificacion():
    return jsonify(model_justificacion.delete_justificacion(int(request.json['id_justificacion'])))