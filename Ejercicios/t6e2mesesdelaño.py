
def obtener_mes(numero):
   #Lista de meses
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    #validar que se encuentra dentro del rango 
    if numero >= 1 and numero <= 12:
        meses = meses[numero - 1]
        mensaje = "El mes seleccionado es: " + meses
        #si el numero introducido es mayor que 12 manda mensaje de error 
        if numero==6:
            mensaje += " sin duda es el mejor MES!!"
    else:
        mensaje = "¡Numero incorrecto! ¡Solo hay 12 meses!."
    
    return mensaje


#conversion nº a texto
numero = int(input("Elige un número del 1 al 12 como meses hay en el Año: "))

mensaje = obtener_mes(numero)

print(mensaje)