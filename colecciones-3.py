
# Diccionarios 
#{"clave": "valor"}

teacher = {
    "name":"Zuleyma",
    "l_name":"Pelcastre",
    "phone":"2411713688",
    "groups":["3ADSM","3BDSM"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3CDSM")
teacher["phone"]="2411365738"
teacher["city"]="Atlngatepec"
print(teacher)