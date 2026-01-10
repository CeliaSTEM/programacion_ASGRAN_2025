import random

contador = 0
while contador < 5:
    contador += 1
    print(contador)
print(20*"-")

contador = 1
while contador <= 5:
    print(contador)
    contador += 1
print(20*"-")

# 1.- Acierta el número.
numero = random.randint(1,10)
contadorIntentos = 1
numeroIntroducido = int(input("Introduce un número: "))
while numeroIntroducido != numero:
    contadorIntentos += 1
    numeroIntroducido = int(input("Introduce otro número: "))
print(f"Lo has intentado {contadorIntentos} veces")

# 2.- Contraseña correcta

contrasenia = "Boniato"
intentosQueQuedan = 3
contraseniaIntroducida = input(f"Introduce una contraseña, tienes {intentosQueQuedan} intentos: ") 
intentosQueQuedan -= 1
while contrasenia != contraseniaIntroducida and intentosQueQuedan > 0:
    contraseniaIntroducida = input(f"Introduce otra contraseña, te quedan {intentosQueQuedan} intentos: ") 
    intentosQueQuedan -= 1

if intentosQueQuedan > 0:
    print("Has introducido la contraseña correcta.")
else:
    print ("Te has quedado sin intentos.")