def Colorganador(color):
    if color == "azul":
        mensaje = "VICTORIA"
    else:
        mensaje = "Intenta de nuevo"
    return mensaje

for i in range(5):
    color = input("Introduce un color: ")
    mensaje = Colorganador(color)
    print(mensaje)