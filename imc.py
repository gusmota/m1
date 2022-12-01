
# definición de variables iniciales

nombre = input("Ingrese su nombre: ")
if nombre == "":
    print("Debe ingresar su nombre")
    exit()

apellidos = input("Ingrese sus apellidos: ")
if apellidos == "":
    print("Debe ingresar sus apellidos")
    exit()


try:
    edad = float(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))

except:
    print("Error: Ingrese números en este campo")
    exit()

# cálculo del IMC 
imc = peso / altura ** 2

print(nombre, apellidos, "tiene", edad, "años y su índice de masa corporal es", imc)