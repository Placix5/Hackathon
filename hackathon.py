import requests
import json

codigoProducto = input("Introduzca un código de producto: ")

r = requests.get('https://c0cb63ab.us-south.apigw.appdomain.cloud/apishopping/getProduct?id=' + codigoProducto)
r.status_code

json_body = r.json()

print()
print("Nombre de producto: " + json_body["producto"])
print()
print("Alérgenos que contiene el producto: ")


if(json_body["celiaco"] == '1'):
    print("Apto para celiacos: NO")
else:
    print("Apto para celiacos: SI")

if(json_body["diabetes"] == '1'):
    print("Apto para diabeticos: NO")
else:
    print("Apto para diabeticos: SI")


if(json_body["cereales"] == '1'):
    print("Cereales: SI")
else:
    print("Cereales: NO")


if(json_body["fructosa"] == '1'):
    print("Fructosa: SI")
else:
    print("Fructosa: NO")


if(json_body["frutosSecos"] == '1'):
    print("Frutos secos: SI")
else:
    print("Frutos secos: NO")


if(json_body["histamina"] == '1'):
    print("Histamina: SI")
else:
    print("Histamina: NO")


if(json_body["huevo"] == '1'):
    print("Huevo: SI")
else:
    print("Huevo: NO")


if(json_body["lactosa"] == '1'):
    print("Lactosa: SI")
else:
    print("Lactosa: NO")


if(json_body["legumbres"] == '1'):
    print("Legumbres: SI")
else:
    print("Legumbres: NO")


if(json_body["mar"] == '1'):
    print("Productos del mar: SI")
else:
    print("Productos del mar: NO")