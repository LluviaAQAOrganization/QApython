precio_camiseta = 10 
precio_sudadera = 20.5
precio_gorra = 5.5 

cantidad_camiseta =  int (input ("¿Cuantas camisetas deseas comprar?"))
cantidad_sudadera =  int (input ("¿Cuantas sudaderas deseas comprar?"))
cantidad_gorra =  int (input ("¿Cuantas gorras deseas comprar?"))

total_camiseta = precio_camiseta * cantidad_camiseta
total_sudadera = precio_sudadera  * cantidad_sudadera
total_gorra = precio_gorra  * cantidad_gorra 

Total = total_camiseta + total_sudadera + total_gorra  
print("El total de la compra es:", Total)

iva = Total * 1.21
print("El total con IVA es:", iva)  