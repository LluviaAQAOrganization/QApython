def Adivinaelnumero(numero):
    if numero == "4":
        mensaje = "VICTORIA"
    else:
        mensaje = "Derrota"
    return mensaje

numero = input("Escoge un numero entre 1 y 10: ")
mensaje = Adivinaelnumero(numero)
print("Número elegido:", numero)
print("Resultado:", mensaje)