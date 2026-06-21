
def convertir_dolares (cantidad_euros):
    dolares = cantidad_euros * 1.1
    return dolares 

def convertir_libras(cantidad_euros):
    libras = cantidad_euros * 0.87
    return libras

cantidad_euros = float(input("¿Cuantos euros quieres convertir? "))

dolares = convertir_dolares(cantidad_euros)
libras = convertir_libras(cantidad_euros) 

print("Euros:", cantidad_euros)
print("Dólares:", dolares)
print("Libras:", libras)