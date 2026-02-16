def busca_llave(caja_inicial):
    pila = caja_inicial.arma_una_pila_para_buscar()
    while pila is not empty:
        caja = pila.escoge_una_caja()
        for item in caja:
            if item.es_una_caja(): 
                pila.append(item)
            elif item.es_una_llave(): 
                print("¡llave encontrada!")
