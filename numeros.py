import random

numero_str = "2"        # String -> Cadena de caracteres.

numero_int_uno = 3          # Integer -> Número entero.
numero_int_dos = 5
numero_float_uno = 3.5      # Float -> Número en coma flotante.
numero_float_dos = 5.5

numero_aleatorio = random.randrange(1,6)    # El 6 no está incluido
print(numero_aleatorio)

# Suma
print("Numero entero + Numero entero: ", end="")
print(numero_int_uno+numero_int_dos)
print("Numero entero + Numero decimal: ", end="")
print(numero_int_uno+numero_float_uno)
print("Numero decimal + Numero decimal: ", end="")
print(numero_float_uno+numero_float_dos)

# Resta
print("Numero entero - Numero entero: ", end="")
print(numero_int_uno-numero_int_dos)
print("Numero entero - Numero decimal: ", end="")
print(numero_int_uno-numero_float_uno)
print("Numero decimal - Numero decimal: ", end="")
print(numero_float_uno-numero_float_dos)

# Multiplicación
print("Numero entero x Numero entero: ", end="")
print(numero_int_uno*numero_int_dos)
print("Numero entero x Numero decimal: ", end="")
print(numero_int_uno*numero_float_uno)
print("Numero decimal x Numero decimal: ", end="")
print(numero_float_uno*numero_float_dos)

# División
print("Numero entero / Numero entero: ", end="")
print(numero_int_uno/numero_int_dos)
print("Numero entero / Numero decimal: ", end="")
print(numero_int_uno/numero_float_uno)
print("Numero decimal / Numero decimal: ", end="")
print(numero_float_uno/numero_float_dos)

# División exacta
print("Numero entero // Numero entero: ", end="")
print(numero_int_uno//numero_int_dos)
print("Numero entero // Numero decimal: ", end="")
print(numero_int_uno//numero_float_uno)
print("Numero decimal // Numero decimal: ", end="")
print(numero_float_uno//numero_float_dos)

print("Ejemplo división exacta: \n    Si tengo 20 caramelos y son 8 niños, ¿cuántos caramelos se come cada uno?")
print(f"    Tocamos a {20//8} caramelos por niño.")

# Exponente

print("Numero entero ** Numero entero: ", end="")
print(numero_int_uno**numero_int_dos)
print("Numero entero ** Numero decimal: ", end="")
print(numero_int_uno**numero_float_uno)
print("Numero decimal ** Numero decimal: ", end="")
print(numero_float_uno**numero_float_dos)

# Módulo de una división
print("\nEjemplo división exacta y módulo: ")
print( "    Si tengo 20 caramelos y son 8 niños... ")
print( "    ¿Cuántos caramelos se come cada uno?")
print(f"    Tocamos a {20//8} caramelos por niño.")
print( "    ¿Cuántos caramelos sobran?")
print(f"    Sobran {20%8} caramelos.")
print()

# numero_int_uno valía 3
print(f"El numero_int_uno vale: {numero_int_uno}")
numero_int_uno = numero_int_uno + 2 
# Después de sumarle 2, numero_int_uno vale 5
print(f"El numero_int_uno vale: {numero_int_uno}")
numero_int_uno += 2 
# Después de sumarle 2, numero_int_uno vale 7
print(f"El numero_int_uno vale: {numero_int_uno}")
numero_int_uno -= 2
# Después de restarle 2, numero_int_uno vale 5
print(f"El numero_int_uno vale: {numero_int_uno}")
numero_int_uno *= 2
# Después de multiplicación 2, numero_int_uno vale 10
print(f"El numero_int_uno vale: {numero_int_uno}")
numero_int_uno /= 2
# Después de dividirlo entre 2, numero_int_uno vale 5
print(f"El numero_int_uno vale: {numero_int_uno}")
