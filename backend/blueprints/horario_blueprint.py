from flask import Flask,Blueprint,request,jsonify
import json
from flask_cors import CORS, cross_origin
from backend.models.postgres_horario_model import HorarioModel


model_horario = HorarioModel()
horario_blueprint = Blueprint('horario_blueprint',__name__)

@horario_blueprint.route('/get_horarios',methods=['GET'])
@cross_origin()
def get_horarios():
    return jsonify(model_horario.get_horarios())

@horario_blueprint.route('/get_horario',methods=['GET'])
@cross_origin()
def get_horario():
    return jsonify(model_horario.get_horario(int(request.json['id_horario'])))


@horario_blueprint.route('/create_horarios',methods=['POST'])
@cross_origin()
def insert_horario():
    content=model_horario.insert_horarios(
        request.json['num_horas'],
        request.json['descripcion'],
        request.json['hora_inicio'],
        request.json['hora_fin'],
        request.json['dia_semana'],
        request.json['id_seccion']
    )
    return jsonify(content)

@horario_blueprint.route('/update_horarios',methods=['PATCH'])
@cross_origin()
def update_horario():
    content=model_horario.update_horarios(
        request.json['id_horario'],
        request.json['num_horas'],
        request.json['descripcion'],
        request.json['hora_inicio'],
        request.json['hora_fin'],
        request.json['dia_semana'],
        request.json['id_seccion']
    )
    return jsonify(content)


@horario_blueprint.route('/delete_horarios', methods=['DELETE'])
@cross_origin()
def delete_horario():
    return jsonify(model_horario.delete_horarios(int(request.json['id_horario'])))