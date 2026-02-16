def busca_la_llave(caja):
    for item in caja:
        if item.es_una_caja(): 
            busca_la_llave(item)
        elif item.es_una_llave(): 
            print("¡llave encontrada!")
