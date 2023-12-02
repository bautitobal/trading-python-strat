from medias_moviles import calcular_medias_moviles
import descargar_datos

fscope = open("scope.txt", "r")
scope = fscope.read().splitlines()
fscope.close()

for linea in scope:
    activo, nombre_empresa = map(str.strip, linea.split('/'))
    
    datos = descargar_datos(activo)
    calcular_medias_moviles(datos, nombre_empresa)
