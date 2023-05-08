#consumir api de comparar caras de docker
import requests
import json
import numpy as np

url = 'http://0.0.0.0:81/recibir_foto'
img1 = open('/home/luisfelipe/Proyectos/construccion_Software/proyecto_final/photos/file.png', 'rb')

files = {'file': img1}

response = requests.post(url, files=files)
print(response.json())