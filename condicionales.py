numero_limite = 10

numero_mayor = 20
numero_menor = 5
numero_igual = 10

if numero_mayor > numero_limite:
    print (f"{numero_mayor} es mayor que {numero_limite}")
    print("Este print está dentro del primer if")
print("Este print está fuera del primer if")

if numero_mayor < numero_limite:
    print (f"{numero_mayor} es menor que {numero_limite}")
    print("Este print está dentro del segundo if")
print("Este print está fuera del segundo")

if numero_mayor == numero_limite:
    print (f"{numero_mayor} es igual que {numero_limite}")
 
if numero_mayor != numero_limite:
    print (f"{numero_mayor} es distinto que {numero_limite}")
 
if numero_mayor >= numero_limite:
    print (f"{numero_mayor} es mayor o igual que {numero_limite}")

if numero_mayor <= numero_limite:
    print (f"{numero_mayor} es menor o igual que {numero_limite}")
 