def busqueda(nombre): 
    cola = deque()
    cola += grafo[nombre]
    visitados = set()
    while cola:
        persona = cola.popleft()
        if not persona in visitados:
            if es_vendedor(persona):	
                print("¡" + persona + " es vendedor de mangos!")
                return True
            else:
                cola += grafo[persona]
                visitados.add(persona)
        return False 

busqueda("tú")
