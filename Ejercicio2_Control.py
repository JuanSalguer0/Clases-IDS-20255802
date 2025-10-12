platos = ["Hambruguesa", "Hotdog", "Pizza", "Tacos", "Lasaña", "Ensalda", "Pupusas", "Burrito", "Alitas de pollo", "Papas fritas"]
precios = ["$3.52", "$55.15", "$4.25", "$60.25", "$5.65", "$3.15", "$2.65", "$70.75", "$6.25", "$2.55"]


print(f"Estos son los platos con sus precios {platos}, {precios}")

#Hamburguesa
plato_seleccionado = int(input("Seleccione el plato que quiere cambiar de precio por medio de un numero del 1-10: "))
print(f"Este es el precio actual de/la {platos[plato_seleccionado-1]}: {precios[plato_seleccionado-1]}")
precio_nuevo = int(input("Ingrese el nuevo valor que le pondra al plato: "))
print(precio_nuevo + 0.52)




