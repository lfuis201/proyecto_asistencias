from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename


from flask_cors import CORS, cross_origin
from backend.models.postgres_seccion_profesor_model import SeccionProfesorModel


model_seccionprofesor = SeccionProfesorModel()
seccionprofesor_blueprint = Blueprint('seccionprofesor_blueprint',__name__)

@seccionprofesor_blueprint.route('/get_seccionprofesor',methods=['GET'])
@cross_origin()
def get_seccionprofesores():
    content = model_seccionprofesor.get_SeccionProfesores()
    return jsonify(content) 

@seccionprofesor_blueprint.route('/buscar_seccionprofesor',methods=['GET'])
@cross_origin()
def get_seccion_profesor():
    return jsonify(model_seccionprofesor.get_SeccionProfesor(int(request.json['id_seccion_profesor'])))


@seccionprofesor_blueprint.route('/create_seccionprofesor',methods=['POST'])
@cross_origin()
def insert_seccion_profesor():
    content=model_seccionprofesor.insert_SeccionProfesor(
        request.json['id_profesor'],
        request.json['id_seccion']
    )
    return jsonify(content)

@seccionprofesor_blueprint.route('/update_seccionprofesor',methods=['PATCH'])
@cross_origin()
def update_seccion_profesor():
    content=model_seccionprofesor.update_SeccionProfesor(
        request.json['id_seccion_profesor'],
        request.json['id_profesor'],
        request.json['id_seccion']
    )
    return jsonify(content)


@seccionprofesor_blueprint.route('/delete_seccionprofesor', methods=['DELETE'])
@cross_origin()
def delete_seccion_profesor():
    return jsonify(model_seccionprofesor.delete_SeccionProfesor(int(request.json['id_seccion_profesor'])))