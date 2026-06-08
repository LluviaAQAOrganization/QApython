nombre_producto = input("Nombre del producto: ")
precio = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento en porcentaje: "))

def calcular_descuento(precio, cantidad, descuento):
    total_sin_descuento = precio * cantidad
    descuento_aplicado = total_sin_descuento * (descuento / 100)
    total_con_descuento = total_sin_descuento - descuento_aplicado
    return total_con_descuento

def calcular_iva(total_con_descuento):
    iva = total_con_descuento * 1.21
    return iva

total_con_descuento = calcular_descuento(precio, cantidad, descuento)
iva = calcular_iva(total_con_descuento) 
 
print("Producto:", nombre_producto)
print("Cantidad:", cantidad)
print("Descuento:", descuento, "%")
print("Total con descuento:", total_con_descuento)
print("Total con IVA:", iva)