import os
import requests


server = "http://api.ejemplo.com/"


def comprobar_estado():
    r = requests.get(f'{server}/')


if r == 200:
    print ("OK")
else:
    print("Error")

datos = r.text
print(datos)


r = requests.get(f'{server}/estado')
if r == "error 404":
    print("FALLO DE CONEXIÓN")
