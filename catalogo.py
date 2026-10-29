import json

grupos= {
    "STARLINK": "Starlink",
    "ONEWEB": "OneWeb",
    "KUIPER": "Kuiper",
    "QIANFAN": "Qianfan",
    "IRIDIUM": "Iridium",
    "GLOBALSTAR": "Globalstar",
    "NAVSTAR": "GPS",
    "BEIDOU": "BeiDou"
}

def leer_satelites(ruta):
    """lee un archivo json con registros de satelites y devuelve una lista de diccionarios"""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("error al leer el archivo: ", e)
        return []
    

def anio_lanzamiento(registro):
    """devuelve el año de lanzamiento como init, a partr de los primeros cuatro caracteres de  'OJECT_ID'"""
    object_id = registro.get("OBJECT_ID", "")
    if len(object_id) >= 4 and object_id[:4].isdigit():
        return int(object_id[:4])
    return 0

def grupo(nombre):
    """devuelve el grupo al que pertenece un satelite segun como empieza su nombre"""
    for inicial, nombre_g in grupos.items():
        largo = len(inicial)
        if len(nombre) >= largo and nombre[:largo] == inicial:
            return nombre_g
    return "otros"

def contar_por_grupo(registros):
    """devuelve un diccionario {grupo: cantidad}"""
    conteo = {}
    for r in registros:
        nombre = r.get("OBJECT_NAME", "")
        g = grupo(nombre)
        conteo[g] = conteo.get(g, 0) + 1
    return conteo

def lanzamientos_por_anio(registros):
    """devuelve un diccionario {año: cantidad de satelites lanzados en ese año}"""
    conteo = {}
    for r in registros:
        anio= anio_lanzamiento(r)
        if anio > 0 :
            conteo[anio] = conteo.get(anio, 0) + 1
    return conteo
