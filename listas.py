lista_colores = ["AZUL", "AMARILLO", "ROJO", "VERDE"]

print(f"El primer color de la lista es: {lista_colores[0]}")
print(f"El segundo color de la lista es: {lista_colores[1]}")
print(f"El tercero color de la lista es: {lista_colores[2]}")
print(f"El cuarto color de la lista es: {lista_colores[3]}")

print(f"La lista es: {lista_colores}")

contador = 1
for color in lista_colores:
    print(f"{contador}.- {color}")
    contador += 1

# Modificar elemento de la lista
lista_colores[0] = "Azul"
print(lista_colores)

# Añadir elemento a la lista
lista_colores.append("NARANJA")
print(lista_colores)
lista_colores.extend(["BLANCO","NEGRO"])
print(lista_colores)
lista_colores.insert(6,"GRIS")
print(lista_colores)

#Eliminar elementos lista
lista_colores.pop()
print(lista_colores)
lista_colores.pop(0)
print(lista_colores)
lista_colores.pop(3)
print(lista_colores)
lista_colores.clear()
print(lista_colores)