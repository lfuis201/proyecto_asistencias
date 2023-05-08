#consumir api de comparar caras de docker
import requests
import json
import numpy as np
url = 'http://0.0.0.0:81/comparar-caras'
imagen1 = "photos/file.png"
imagen2 = "photos/file2.png"

# Crea un diccionario con las imágenes
files = {'imagen1': open(imagen1, 'rb'), 'imagen2': open(imagen2, 'rb')}

response = requests.post(url, files=files)
print(response.text)

json_response=json.loads(response.text)

vector = json_response["distancia"]
print(vector)
#
print(type(vector))

#segundo_valor=json_response['file']
#print(segundo_valor)
#print(json.dumps(json_response, indent=4))
#print(response.text)


