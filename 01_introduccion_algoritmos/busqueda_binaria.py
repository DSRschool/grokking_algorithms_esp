def busqueda_binaria(lista, elemento):
    menor = 0
    mayor = len(lista) - 1

    while menor <= mayor:
        medio = (menor + mayor) // 2
        estimado = lista[medio] 
        if estimado == elemento:
            return medio
        elif estimado > elemento:
            mayor = medio - 1
        else:
            menor = medio + 1
    return None

mi_lista = [1, 3, 5, 7, 9]

print(busqueda_binaria(mi_lista, 3))  # => 1
print(busqueda_binaria(mi_lista, -1)) # => None
