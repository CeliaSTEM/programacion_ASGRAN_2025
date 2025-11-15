# Vamos a crear una minicalculadora.

# 1.- 
# Solicitamos dos números.
# Hacemos la suma.
# Mostramos el resultado. Ej: "2 + 4 = 6"

# 2.- 
# Solicitamos dos números.
# Solicitamos una operacion 
#       (suma, resta, multiplicación o división)
# Mostramos el resultado. Ej: (2 * 5 = 10)

numero1 = int(input("Dime un número: "))
numero2 = int(input("Dime un número: "))
operacion = input("Dime la operación que quieres realizar (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")
# elif -
# elif *
# elif /
# else  -> ERROR