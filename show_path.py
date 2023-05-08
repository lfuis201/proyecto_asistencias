#consumir api de comparar caras de docker
import requests
import json
import numpy as np

url = 'http://0.0.0.0:81/recibir_foto'
img1 = open('photos/file.png', 'rb')

files = {'file': img1}

response = requests.post(url, files=files)

json_response=json.loads(response.text)
vector = json_response["result"]
print(vector)
print(type(vector))

#segundo_valor=json_response['file']
#print(segundo_valor)
#print(json.dumps(json_response, indent=4))
#print(response.text)


