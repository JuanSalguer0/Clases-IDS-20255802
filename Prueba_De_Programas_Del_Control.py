platos = ["Hamburguesa", "Hotdog", "Pizza", "Tacos", "Lasaña", "Ensalda", "Pupusas", "Burrito", "Alitas de pollo", "Papas fritas"]

print(platos)

plato_seleccionado = int(input("Seleccione el plato que quiere cambiar por medio de un numero del 1-10: "))

print(platos[plato_seleccionado-1])

platos = plato_seleccionado

print(platos)