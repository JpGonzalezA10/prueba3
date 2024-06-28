import random
import math
alumnos = {}
def agregar_alumno():
  try:
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    grado = input("Ingrese el grado del alumno: ")
    notas = random.randint(1, 10)
    
    

    alumnos[grado] = {
      'nombre': nombre,
      'apellido': apellido,
      'edad': edad,
      'grado': grado,
      'notas': notas,
    
    }

    print(f"alumno agregado exitosamente con el grado {grado}!")
  except ValueError:
    print("Error: Ingreso de datos inválidos. Asegúrese de ingresar la edad como un número.")



def listar_alumnos():
  if alumnos:
    for grado, datos in alumnos.items():
      print(f"grado: {grado}")
      print(f"Nombre: {datos['nombre']}")
      print(f"apellido: {datos['apellido']}")
      print(f"edad: {datos['edad']}")
      print(f"grado: {datos['grado']}\n")
      
  else:
    print("No hay alumnos registrados.")



def buscar_alumno():
  try:
    grado_buscar = int(input("Ingrese el código del grado a buscar: "))
    if grado_buscar in alumnos:
      datos = alumnos[grado_buscar]
      print(f"Nombre: {datos['nombre']}")
      print(f"apellido: {datos['apellido']}")
      print(f"edad: {datos['edad']}")
      print(f"grado: {datos['grado']}\n")

    else:
      print("No se encontró ningun alumno en este grado.")

  except ValueError:
    print("Error: Ingrese un grado válido.")

def calcular_nota():
  nota=random

def guardar_alumnos():
  try:
    with open("archivo.txt", "w") as archivo:
      for codigo, datos in alumnos.items():
        archivo.write(f"Nombre: {datos['nombre']}\n")
        archivo.write(f"Apellido: {datos['apellido']}\n")
        archivo.write(f"Edad: {datos['edad']}\n")
        archivo.write(f"Grado: {datos['grado']}\n\n")
        
        

    print("alumno guardados en archivo.txt")
  except Exception as muestra:
    print(f"Error al guardar el alumno: {muestra}")


while True:
    print("Menú de Usuario")
    print("1. Registrar Alumno")
    print("2. Listar Alumno")
    print("3. Buscar Alumno por nivel")
    print("4. Calcular la nota promedio de los alumnos")
    print("5. Salir")

    try:
      opcion = int(input("Seleccione una opción: "))
      if opcion == 1:
        agregar_alumno()
      elif opcion == 2:
        listar_alumnos()
      elif opcion == 3:
        buscar_alumno()
      elif opcion == 4:  
        calcular_nota()
      elif opcion == 5:
        guardar_alumnos()
        print("Saliendo del programa...")
        break

      else:
        print("Opción no válida. Intente de nuevo.")

    except ValueError:
      print("Error: Ingrese un número válido.")
 






