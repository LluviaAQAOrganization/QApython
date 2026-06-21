def ruletafortunacolores(color):
    #pasamos el color a minúscula para comparar
    color = color.lower()

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
    else:
        mensaje = "Color elegido inválido"

    return mensaje


#Pedimos color al usuario
color = input("Selecciona un color: rojo, verde, azul, amarillo o morado ")

mensaje = ruletafortunacolores(color)

print("Color:", color)
print("Mensaje:", mensaje)