def encuentra_nodo_de_menor_coste(costes): 
    menor_coste = math.inf
    nodo_menor_coste = None
    for nodo in costes:
        coste = costes[nodo]
        if coste < menor_coste and nodo not in procesados:
            menor_coste = coste
            nodo_menor_coste = nodo	
    return nodo_menor_coste

costes = ["2", "3"]
nodo = encuentra_nodo_de_menor_coste(costes)	
while nodo is not None:	
    coste = costes[nodo]
    vecinos = grafo[nodo]
    for n in vecinos.keys():	
        coste_nuevo = coste + vecinos[n]
        if costes[n] > coste_nuevo:	
            costes[n] = coste_nuevo	
            padres[n] = nodo	
    procesados.append(nodo)	
    nodo = encuentra_nodo_de_menor_coste(costes)
