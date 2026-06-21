#Pedir a usuaria 5 veces que introduzca un color
for i in range(5):
    colorElegido = input("Introduce un color ").lower()
    if (colorElegido == "azul"):
        mensaje = "Premio conseguido"
        print(mensaje)
        break;
    else:
        mensaje = "Prueba otro color"
        print(mensaje)