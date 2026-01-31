import getpass
import random

lista_opciones = ["piedra", "papel", "tijera"]
# eleccion_jugador_1 = input("JUGADOR 1: Piedra, papel, tijera -> ").lower()
# eleccion_jugador_2 = input ("JUGADOR 2: Piedra, papel, tijera -> ").lower()
eleccion_jugador_1 = getpass.getpass(("JUGADOR 1: Piedra, papel, tijera -> ").lower())
while eleccion_jugador_1 not in lista_opciones:
    print(f"Has escrito {eleccion_jugador_1}")
    eleccion_jugador_1 = getpass.getpass(("JUGADOR 1 (otra vez): Piedra, papel, tijera -> ").lower())


#eleccion_jugador_2 = getpass.getpass(("JUGADOR 2: Piedra, papel, tijera -> ").lower())
eleccion_pc = random.choice(lista_opciones)
print(f"Elección jugador 1: {eleccion_jugador_1}")
#print(f"Elección jugador 2: {eleccion_jugador_2}")
print(f"Elección pc: {eleccion_pc}")

# Cuarta forma: ¿Funciona? Lo mejor que podemos hacer con if/else [sin vectores circulares]
if eleccion_jugador_1 == eleccion_pc:
    print ("Empate")
elif (eleccion_jugador_1 == "piedra" and eleccion_pc == "tijera") or (eleccion_jugador_1 == "papel" and eleccion_pc == "piedra") or (eleccion_jugador_1 == "tijera" and eleccion_pc == "papel"):
    print ("Gana el jugador 1")
else:
    print ("Gana la IA")

# TODO:
# - Vamos a gestionar turnos. Para que si el humano se equivaca metiendo su elección, le permita repetir.
# - Vamos a darle nombres a los jugadores.
# - Añadir un jugador PC, para que juegue con nosotros eligiendo aleatoriamente entre piedra, papel y tijera.
# - Programamos un mejor-de-tres: En el que gana el primero que venza dos veces.+
# - Trabajamos con mayúsculas para utilizar .upper()

"""
# Pimera forma: ¿Funciona? Si, pero no es sufiente.
if eleccion_jugador_1 == eleccion_jugador_2:
    print ("Empate")
if eleccion_jugador_1 == "piedra" and eleccion_jugador_2 == "tijera":
    print ("Gana el jugador 1")
if eleccion_jugador_1 == "papel" and eleccion_jugador_2 == "piedra":
    print ("Gana el jugador 1")
if eleccion_jugador_1 == "tijera" and eleccion_jugador_2 == "papel":
    print ("Gana el jugador 1")
if eleccion_jugador_2 == "piedra" and eleccion_jugador_1 == "tijera":
    print ("Gana el jugador 2")
if eleccion_jugador_2 == "papel" and eleccion_jugador_1 == "piedra":
    print ("Gana el jugador 2")
if eleccion_jugador_2 == "tijera" and eleccion_jugador_1 == "papel":
    print ("Gana el jugador 2")
# ...

# Segunda forma: ¿Funciona? Si, pero todavía no es eficiente del todo.
if eleccion_jugador_1 == eleccion_jugador_2:
    print ("Empate")
elif eleccion_jugador_1 == "piedra" and eleccion_jugador_2 == "tijera":
    print ("Gana el jugador 1")
elif eleccion_jugador_1 == "papel" and eleccion_jugador_2 == "piedra":
    print ("Gana el jugador 1")
elif eleccion_jugador_1 == "tijera" and eleccion_jugador_2 == "papel":
    print ("Gana el jugador 1")
elif eleccion_jugador_2 == "piedra" and eleccion_jugador_1 == "tijera":
    print ("Gana el jugador 2")
elif eleccion_jugador_2 == "papel" and eleccion_jugador_1 == "piedra":
    print ("Gana el jugador 2")
elif eleccion_jugador_2 == "tijera" and eleccion_jugador_1 == "papel":
    print ("Gana el jugador 2")

# Tercera forma: ¿Funciona? Si, pero todavía no es eficiente del todo.
if eleccion_jugador_1 == eleccion_jugador_2:
    print ("Empate")
elif eleccion_jugador_1 == "piedra" and eleccion_jugador_2 == "tijera":
    print ("Gana el jugador 1")
elif eleccion_jugador_1 == "papel" and eleccion_jugador_2 == "piedra":
    print ("Gana el jugador 1")
elif eleccion_jugador_1 == "tijera" and eleccion_jugador_2 == "papel":
    print ("Gana el jugador 1")
else:
    print ("Gana el juegador 2")
"""


