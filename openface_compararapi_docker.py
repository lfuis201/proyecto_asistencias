import os
import openface
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import cv2

app = Flask(__name__)

# Cargar el modelo de reconocimiento facial
align = openface.AlignDlib("/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat")
net = openface.TorchNeuralNet("/root/openface/models/openface/nn4.small2.v1.t7", 96)
# Definir la ruta para la comparacin de caras
@app.route('/comparar-caras', methods=['POST'])
@cross_origin()
def comparar_caras():
    # Obtener las imgenes de las dos caras desde la solicitud HTTP
    f1 = request.files['imagen1']
    f2 = request.files['imagen2']
    
    filename1 = f1.filename
    filename2  = f2.filename

    f1.save("/root/photos/" + filename1)
    f2.save("/root/photos/" + filename2)         

    img1 = cv2.imread("/root/photos/" + filename1)
    img2 = cv2.imread("/root/photos/" + filename2)
    # Convertir las igenes a formato OpenCV
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    bb1 = align.getLargestFaceBoundingBox(img1)
    bb2 = align.getLargestFaceBoundingBox(img2)
    
    aligned_img1 = align.align(96, img1, bb1, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    aligned_img2 = align.align(96, img2, bb2, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    # Obtener las caractersticas utilizando la funn getRep
    rep1 = net.forward(aligned_img1)
    rep2 = net.forward(aligned_img2)

    # Calcular la distancia euclidiana entre las caractersticas
    dist = np.linalg.norm(rep1 - rep2)

    return jsonify({'distancia': dist})

# Ejecutar la aplicacin Flask
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=81)