# VARIABLES
palabra = "ballena"
numero_uno = 2
numero_dos = 5

# Imprimiendo strings ("cadenas de caracteres")
print ("Me gustan las " + palabra + "!")
print (f"Me gustan las {palabra}!")

# Imprimiendo números separados por " .. "
print (numero_uno, end=" .. ")
print (numero_uno+numero_dos)

# Imprimiendo números y strings.
print ("1.- Hay " + str(numero_uno) + " " + palabra + "s!")
print (f"2.- Hay {numero_uno} {palabra}s!")
# La , deja siempre espacios.
print("3.- Hay",2,"ballenas!")
print("4.- Hay",2,palabra,"s!")
print("5.- Hay",numero_uno,"ballenas!")
print("6.- Hay",numero_uno,palabra,"s!")
