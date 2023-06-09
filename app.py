from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.user_blueprint import user_blueprint
from backend.blueprints.curso_blueprint import curso_blueprint
from backend.blueprints.seccion_blueprint import seccion_blueprint
from backend.blueprints.alumno_blueprint import alumno_blueprint
from backend.blueprints.profesor_blueprint import profesor_blueprint
from backend.blueprints.horario_blueprint import horario_blueprint
from backend.blueprints.justificacion_blueprint import justificacion_blueprint
from backend.blueprints.participicacion_blueprint import participacion_blueprint
from backend.blueprints.asistencia_blueprint import asistencia_blueprint
from backend.blueprints.seccion_profesor_blueprint import seccionprofesor_blueprint
from backend.blueprints.alumno_seccion_blueprint import alumnoseccion_blueprint
app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(seccion_blueprint)
app.register_blueprint(alumno_blueprint)
app.register_blueprint(profesor_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(justificacion_blueprint)
app.register_blueprint(participacion_blueprint)
app.register_blueprint(seccionprofesor_blueprint)
app.register_blueprint(alumnoseccion_blueprint)
app.register_blueprint(participacion_blueprint)
app.register_blueprint(asistencia_blueprint)
cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True, port=5050)