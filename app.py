from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.user_blueprint import user_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True, port=5050)