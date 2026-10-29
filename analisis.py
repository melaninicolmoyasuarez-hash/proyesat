from catalogo import grupo

def contar_por_tipo(satelites):
    """devuelve un diccionario {"LEO": n, "MEO": n, "GEO": n, "HEO": n} """
    conteos = {"LEO": 0 , "MEO": 0, "GEO": 0, "HEO": 0}
    for satelite in satelites:
        tipo = satelite.tipo_orbita()
        if tipo in conteos:
            conteos[tipo] += 1
    return conteos

def mas_alto(satelites):
    """devuelve el objeto de mayor altitud"""
    if not satelites:
        return None
    sat_max = satelites[0]
    for sat in satelites:
        if sat.altitud > sat_max.altitud:
            sat_max = sat
    return sat_max


