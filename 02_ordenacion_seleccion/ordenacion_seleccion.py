def encontrar_menor(arr):
    menor = arr[0]
    indice_menor = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            indice_menor = i
    return indice_menor
    
def ordenacion_seleccion(arr):
    nuevo_array = []
    copia_array = list(arr) # copy array before mutating
    for i in range(len(copia_array)):
        menor = encontrar_menor(copia_array)
    nuevo_array.append(copia_array.pop(menor))
    return nuevo_array

print(ordenacion_seleccion([5, 3, 6, 2, 10]))
