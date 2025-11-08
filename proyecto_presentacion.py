mi_edad = 29

# Preguntamos el nombre y lo guardamos en una variable.
nombre = input("¿Cómo te llamas? ")
print (f"Te llamas {nombre}.")
# Preguntamos la edad y la guardamos en una variable.
edad = int(input("¿Cuántos años tienes? "))
print(f"Tienes {edad} años.")
# Preguntar el número favorito y guardarlo en una variable.
# Preguntar el color favorito y guardarlo en una variable.

# ESCRIBIR: "A {nombre}, que tiene {edad} años, 
# le gusta el número {numero} y el color {color}"
print(f"A {nombre}, que tiene {edad} años...")

# 1.- Mostrar las respuestas en un texto.
# 2.- Comparar las respuestas con tus respuestas: 
#           ¿Es mayor o menor que tu?
if edad > mi_edad:
    print(f"{nombre} es mayor que yo.")
elif edad < mi_edad:
    print(f"{nombre} es menor que yo.")
else:
    print(f"{nombre} tiene los mismos años que yo.")
#           ¿Su número favorito es mayor o menor que el tuyo?
#           ¿Tenéis el mismo color favorito?
#           ¿Su número favorito es par o impar?