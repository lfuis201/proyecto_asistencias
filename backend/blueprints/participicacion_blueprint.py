from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_participacion_model import ParticipacionModel


model_participacion = ParticipacionModel()
participacion_blueprint = Blueprint('participacion_blueprint',__name__)

@participacion_blueprint.route('/get_participacion',methods=['GET'])
@cross_origin()
def get_participaciones():
    content = model_participacion.get_Partipaciones()
    return jsonify(content) 

@participacion_blueprint.route('/buscar_participacion',methods=['GET'])
@cross_origin()
def get_participacion():
    return jsonify(model_participacion.get_Participacion(int(request.json['id_participacion'])))


@participacion_blueprint.route('/create_participacion',methods=['POST'])
@cross_origin()
def insert_participacion():
    content=model_participacion.insert_participacion(
        request.json['fecha'],
        request.json['participacion'],
        request.json['id_horario']
    )
    return jsonify(content)

@participacion_blueprint.route('/update_participacion',methods=['PATCH'])
@cross_origin()
def updateparticipaciones():
    content=model_participacion.update_participacion(request.json['id_participacion'],request.json['fecha'],
                                                     request.json['participacion'],request.json['id_horario'],)
    return jsonify(content)


@participacion_blueprint.route('/delete_participacion',methods=['DELETE'])
@cross_origin()
def delete_asistparticipacion():
        return jsonify(model_participacion.delete_participacion(int(request.json['id_participacion'])))