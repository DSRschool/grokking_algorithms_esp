from os import listdir
from os.path import isfile, join

def imprime_nombres(dir):
    for fich in sorted(listdir(dir)):
        ruta_completa = join(dir, fich)
        if isfile(ruta_completa):
            print(fich)
        else:
            printnames(ruta_completa)
            
imprime_nombres("fotos")
