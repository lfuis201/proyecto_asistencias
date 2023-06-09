from flask import Flask,Blueprint,request,jsonify
from werkzeug.utils import secure_filename
import requests
import json
from flask_cors import CORS, cross_origin
from backend.models.postgres_asistencia_model import AsistenciaModel
from backend.models.mysql_user_model import UserModel
from backend.models.postgres_alumno_model import AlumnoModel
umodel = UserModel()
model_alumno = AlumnoModel()
model_asistencia = AsistenciaModel()
asistencia_blueprint = Blueprint('asistencia_blueprint',__name__)

@asistencia_blueprint.route('/get_asistencias',methods=['GET'])
@cross_origin()
def get_horarios():
    content = model_asistencia.get_asistencias()
    return jsonify(content) 

@asistencia_blueprint.route('/buscar_asistencia',methods=['GET'])
@cross_origin()
def get_horario():
    return jsonify(model_asistencia.get_Asistencia(int(request.form['id_asistencia'])))


@asistencia_blueprint.route('/create_asistencia',methods=['POST'])
@cross_origin()
def insert_asistencia():
    
    f = request.files['foto']
    filename = f.filename
    
    f.save("/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos_asistencia/" +request.form['dni']+ filename)
    
    f_save = ("/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos_asistencia/" +request.form['dni']+ filename)
    
    fotouserpath=umodel.get_photo_by_dni(request.form['dni'])
    
    img1 = open(f_save, 'rb')
    img2 = open(fotouserpath[0].get("foto"), 'rb')
    
    url = 'http://0.0.0.0:81/comparar-caras'
    
    files = {'imagen1': img1, 'imagen2':img2}
    
    response = requests.post(url, files=files)
    json_response=json.loads(response.text)
    vector = json_response["distancia"]
    estado=False
    
    
    if float(vector)<0.6:
        estado=True
   
    content=model_asistencia.insert_asistencias(
        estado,
        request.form['fecha'],
        request.form['id_horario'],
        vector,
        f_save,
        request.form['dni']
    )
    return jsonify(content)

@asistencia_blueprint.route('/update_asistencia',methods=['PATCH'])
@cross_origin()
def update_asistencia():
    f = request.files['foto']
    filename = f.filename
    dir ="/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos_asistencia/" + "nuevo"+filename
    f.save(dir)
    
    f_save = dir
    content=model_asistencia.update_asistencia(
        request.form['id_asistencia'],
        request.form['estado'],
        request.form['fecha'],
        request.form['id_horario'],
        
        f_save
    )
    return jsonify(content)


@asistencia_blueprint.route('/delete_asistencia', methods=['DELETE'])
@cross_origin()
def delete_asistencia():
    return jsonify(model_asistencia.delete_asistencia(int(request.json['id_asistencia'])))


@asistencia_blueprint.route('/get_id_alumno_por_dni', methods=['POST'])
@cross_origin()
def get_id_alumno_por_dni():
    dni = request.json['dni']
    id_alumno = model_alumno.get_id_alumno_por_dni(dni)
    return jsonify(id_alumno)