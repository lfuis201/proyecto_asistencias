from flask import Flask
from flask import request
from flask import jsonify
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def user():
    nombre = request.form["nombre"]
    edad = request.form['edad']
    foto = request.files['foto']

    
    # Realizar acciones con la información recibida
    
    response = {'nombre': nombre, 'edad': format(edad),'foto':foto.filename}
    print(nombre)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)