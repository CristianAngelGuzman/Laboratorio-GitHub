
def pedir_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre

def saludar(nombre):
    print(f"Hola, {nombre}!")



print("Bienvenidx")

nombre = pedir_nombre()
saludar(nombre)

print("Adios")