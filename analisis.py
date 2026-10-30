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
    """devuelve el satelite de mayor altitud"""
    if not satelites:
        return None
    sat_max = satelites[0]
    for sat in satelites:
        if sat.altitud > sat_max.altitud:
            sat_max = sat
    return sat_max

def mas_bajo(satelites):
    """devuelve el satelite de menor altitud"""
    if not satelites:
        return None
    sat_min= satelites[0]
    for sat in satelites:
        if sat.altitud < sat_min.altitud:
            sat_min = sat
    return sat_min

def en_zona(satelites, zona):
    """devuelve una lista de los satélites dentro de la zona"""
    resultado = []
    for sat in satelites:
        if sat.esta_en_zona(zona):
            resultado.append(sat)
    return resultado

def ordenar_por(satelites,atributo, descendente=False):
    """funcion generica que devuelve una lista nueva ordenada por cualquier atributo"""
    def clave_orden(sat):
        if atributo == "altitud":
            return sat.altitud
        elif atributo == "latitud":
            return sat.latitud
        elif atributo == "nombre":
            return sat.nombre
        return sat.altitud
    return sorted(satelites, key= clave_orden, reverse=descendente)

def top_n(satelites, n, mas_alto=True):
    """devuelve los n satelites mas altos (o bajos)"""
    ordenados = ordenar_por(satelites, "altitud", descendente=mas_alto)
    return ordenados[:n]


def resumen_por_grupo(satelites):
    """devuelve un diccionario con un resumne de las altitudes de cada grupo"""
    agrupados = {}
    for sat in satelites:
        g= grupo(sat.nombre)
        if g not in agrupados:
            agrupados[g] = []
        agrupados[g].append(sat.altitud)
    resumen= {}
    for g, altitudes in agrupados.items():
        resumen[g] = {
            "cantidad": len(altitudes),
            "minima": min(altitudes),
            "maxima": max(altitudes),
            "media": sum(altitudes)/len(altitudes)
        }
    return resumen
