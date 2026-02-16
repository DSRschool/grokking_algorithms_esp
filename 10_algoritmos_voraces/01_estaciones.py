estados = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estaciones = {}
estaciones["kuno"] = set(["id", "nv", "ut"])
estaciones["kdos"] = set(["wa", "id", "mt"])
estaciones["ktres"] = set(["or", "nv", "ca"])
estaciones["kcuatro"] = set(["nv", "ut"])
estaciones["kcinco"] = set(["ca", "az"])
estaciones_finales = set()

mejor_estacion = None 
estados_cubiertos = set()
for estacion, estados_por_estacion in estaciones.items():
  cubiertos = estados & estados_por_estacion
  if len(cubiertos) > len(estados_cubiertos): 
    mejor_estacion = estacion
    estados_cubiertos = cubiertos
    while estados: 
        mejor_estacion = None 
        estados_cubiertos = set()
        for estacion, estados_por_estacion in estaciones.items():
            cubiertos = estados & estados_por_estacion
            if len(cubiertos) > len(estados_cubiertos): 
                mejor_estacion = estacion
                estados_cubiertos = cubiertos
        estados -= estados_cubiertos
        estaciones_finales.add(mejor_estacion)

print(estaciones_finales)
