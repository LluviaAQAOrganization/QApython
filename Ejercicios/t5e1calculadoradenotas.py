cantidad_notas = int(input("¿Cuántas notas deseas introducir? "))

suma = 0
for i in range(cantidad_notas):
    nota = float(input("Introduce una nota: "))
    suma = suma + nota

media = suma / cantidad_notas
print("La nota media es:", media)