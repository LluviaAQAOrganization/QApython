def planeta (numero):
    #Lista de planetas
    planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
    #Comprobar si es valido
    if numero >= 1 and numero <= 8:
        mensaje = "El planeta en la posición", numero, "es", planetas[numero - 1]
    else:
        mensaje = "Error: número inválido."
    return mensaje


#Pide a la usuaria un número del 1 al 8
numero = int(input("Introduce un número del 1 al 8: "))

#obtiene el planeta
nombre_planeta = planeta(numero)

print(nombre_planeta)