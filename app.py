import utilidades

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
 



