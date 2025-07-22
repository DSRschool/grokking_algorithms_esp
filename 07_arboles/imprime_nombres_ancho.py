from os import listdir
from os.path import isfile, join
from collections import deque

def imprime_nombres(dir_inicial):
    cola_busqueda = deque()	
    cola_busqueda.append(dir_inicial)
    while cola_busqueda:	
        dir = cola_busqueda.popleft()
        for fich in sorted(listdir(dir)):	
            ruta_completa = join(dir, fich)
            if isfile(ruta_completa):
                print(fich)	
            else:
                cola_busqueda.append(ruta_completa)	

imprime_nombres("fotos")
