#consumir api de comparar caras de docker
import requests

url = 'http://0.0.0.0:81/comparar-caras'
img1 = open('photos/file.png', 'rb')
img2 = open('photos/file2.png', 'rb')
files = {'imagen1': img1, 'imagen2': img2}

response = requests.post(url, files=files)
print(response.text)
