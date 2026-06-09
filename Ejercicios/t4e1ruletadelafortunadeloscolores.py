def Ruletafortunacolores(color):
    if color == "rojo":
        mensaje = "Pasión y energía"
    elif color == "verde":
        mensaje = "Esperanza y crecimiento"
    elif color == "azul":
        mensaje = "Calma y serenidad"
    elif color == "amarillo":
        mensaje = "Felicidad y optimismo"
    elif color == "morado":
        mensaje = "Sabiduría y creatividad"
    return mensaje

color = input("Selecciona un color: ")
mensaje = Ruletafortunacolores(color)

print("Color:", color)
print("Mensaje:", mensaje)