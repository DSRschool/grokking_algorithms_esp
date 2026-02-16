votantes = {}
def comprueba_votante(nombre):
    if nombre in votantes: 
        print("¡echadlo de ahí!")
    else:
        votantes[nombre] = True
        print("¡dejadlo votar!")
