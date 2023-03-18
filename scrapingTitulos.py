#librerias
import re
import requests

#Url a scrapear
website = "https://www.vulnhub.com"

#extraer contenido HTML petision
resultado = requests.get(website)

#pasar HTML a texto
content = resultado.text

#patron para detectar lo que necesitamos en este caso es titulo
patron = r"/entry/[\w-]*"

#detecta los titulos de cada maquina (lo que esta luego de /entry/)
maquinas_repetidas = re.findall(patron, str(content)) 

#eliminar repetidas
sin_duplicados = list(set(maquinas_repetidas))

#filtra los nombres de las maquinas y quita las lineas
maquinas_final = []

print("------------------------------")
for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "") #elimina donde haya un /entry/ y quitalo
    maquinas_final.append(nombre_maquinas) #hace un push al array con los nombres limpios
    print("| " + nombre_maquinas )#POR CADA VUELTA IMPRIMIRA EL NOMBRE
print("------------------------------")
