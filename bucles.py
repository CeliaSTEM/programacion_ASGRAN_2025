linea = 30 * "-"            # Crea una variable linea que 
                            # contine 30 guiones.

for numero in range(5):     # Es un bucle que se lee:
                            # Para cada numero en un 
                            # rango del 0 al 5.
    print(numero, end="   ")# Imprimir el número 
                            # El print termina con tres
                            # espacios en vez de con un
                            # salto de línea
print("\n" + linea)         # Fuera del bucle:
                            # Imprime un espacio \n y la
                            # línea de 30 guiones.

for numero in range(1,6):
    print(numero, end="   ")
print("\n" + linea)

for numero in range(10,21):
    print(numero, end="   ")
print("\n" + linea)

# -------------------------------------------------------
# TAREA 0.- Pedir dos números por teclado e imprimir todos
#           los números intermedios.

numero_inicio = int(input("Introduce un número de inicio: "))
numero_fin = int(input("Introduce un número de fin: "))
for numero in range(numero_inicio,numero_fin+1):
    print(numero, end="   ")
print("\n" + linea)
# -------------------------------------------------------

salto = int(input("¿De cuánto en cuanto quieres saltar?: "))
for numero in range(numero_inicio,numero_fin+1,salto):
    print(numero, end="   ")
print("\n" + linea)

numero_repeticiones = int(input("Dime un número para hacer repeticiones: "))
for numero in range(numero_repeticiones):
    print("*", end="   ")
print("\n" + linea)

# TAREA 1.- Pedir un número y una palabra y escribir esa
#           palabra ese número de veces.

# TAREA 2.-  Pedir dos números y contar desde el 0 hasta 
#            cada uno de ellos.

# TAREA 3.- Pedir dos números y contar desde su resta hasta
#           su suma.

# TAREA 4.- Pedir dos números, comprobar que el primero
#           es mayor que el segundo antes de mostrar 
#           todos sus números intermedios.

# TAREA 5.- Pide dos números y un salto.
#           Comprueba si el salto es positivo o negativo 
#           y crea un bucle en consecuencia.