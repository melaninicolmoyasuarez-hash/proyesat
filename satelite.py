from funciones_base import crear_objeto_skyfield, obtener_posicion

class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud):
        """Guarda los cuatro datos como atributos del objeto"""
        self.nombre = nombre
        self.latitud= latitud
        self.longitud= longitud
        self.altitud= altitud

    
    def tipo_orbita(self):
        """devuleve "LEO", "MEO", "GEO" o "HEO" segun la altitud"""
        if self.altitud < 2000:
            return "LEO"
        elif self.altitud < 34000:
            return "MEO"
        elif self.altitud <= 37000:
            return "GEO"
        else:
            return "HEO"

    def esta_en_zona(self, zona):
        """True si el satelite esta adentro de la zona"""
        lon_min, lat_min, lon_max, lat_max = zona
        return (lon_min <= self.longitud <= lon_max) and (lat_min <= self.latitud <= lat_max)

    def __str__(self):
        """presentacion"""
        return f"{self.nombre} | {self.tipo_orbita()} | {self.altitud} km"

def crear_satelites(registros, momento):
    """devuelve una lista de objetos satelite con su posicion en 'momento'"""
    satelites = []
    for registro in registros:
        try: 
            obj_skyfield = crear_objeto_skyfield(registro)
            lat, lon, alt = obtener_posicion(obj_skyfield, momento)
            if alt >= 100:
                s = Satelite( nombre= registro.get("OBJECT_NAME", "desconocido"),
                             latitud=lat,
                             longitud=lon,
                             altitud=alt)
                satelites.append(s)
        except Exception:
            continue
    return satelites
            
