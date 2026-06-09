planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]
numero = int(input("Introduce un numero del 1 al 8: "))

if numero < 1 or numero > 8:
    print("Número inválido")
else:
    print(planetas[numero - 1])