#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError 
# y muestra un mensaje de error al usuario.

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

#Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError 
# y muestra un mensaje de error al usuario.

try:
    numero = 10
    cadena = "5"
    resultado = numero + cadena  
    print("Resultado:", resultado)
except TypeError:
    print("Error: No se puede sumar un número y una cadena.")

# Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
# Si se produce una excepción KeyError, captura la excepción y muestra

try:
    diccionario = {"nombre": "Michelle", "edad": 25}
    print(diccionario["direccion"])  
except KeyError:
    print("Error: La clave no existe en el diccionario.")

#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, 
# captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe

try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no fue encontrado. Creando archivo...")
    with open("archivo.txt", "w") as archivo:
        archivo.write("Este archivo ha sido creado porque no existía.")


#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. 
# Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Debes ingresar un número válido.")


# Calcular el mayor de dos números ingresados por teclado usando un operador ternario

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
mayor = a if a > b else b
print("El número mayor es:", mayor)

#  Buscar una palabra en una lista ingresada por teclado usando *args y un operador ternario

def buscar_palabra(palabra, *args):
    print("Encontrada" if palabra in args else "No encontrada")

lista = input("Ingresa palabras y separelas por coma: ").split(",")
palabra = input("Palabra a buscar: ")
buscar_palabra(palabra.strip(), *[p.strip() for p in lista])

# Determinar si un número es par o impar

n = int(input("Ingresa un número: "))
print("Par" if n % 2 == 0 else "Impar")

# Calcular el promedio de una lista de números usando *args y un operador ternario

def calcular_promedio(*args):
    promedio = sum(args) / len(args) if args else 0
    print("Promedio:", promedio)

numeros = input("Ingresa números y separelos por coma: ").split(",")
numeros = [float(n.strip()) for n in numeros]
calcular_promedio(*numeros)

# Imprimir un mensaje de error si no se pasan suficientes argumentos

def funcion(*args):
    if len(args) < 2:
        print("Error: se necesitan al menos dos argumentos.")
    else:
        print("Se recibieron los argumentos:", args)

funcion(10)  