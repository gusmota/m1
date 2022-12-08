
# definición de variables iniciales
while True:
    try:
        nombre = input("Ingrese su nombre: ")
        nombre[0]

        apellidos = input("Ingrese sus apellidos: ")
        apellidos[0]

        break

    except:
        print("Error: Ingrese caracteres en este campo")

try:
    edad = float(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))

    edad - altura 
    nombre[:1]

except:
    print("Error: Ingrese números en este campo")
    exit()

# cálculo del IMC 
imc = peso / altura ** 2

print(nombre, apellidos, "tiene", edad, "años y su índice de masa corporal es", imc)

#comentario de la nueva versión