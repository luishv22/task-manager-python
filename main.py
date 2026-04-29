from datetime import date
from tareas import GestorTareas

def mostrar_menu():
    print("====================")
    print("  GESTOR DE TAREAS  ")
    print("====================")
    print("1. Agregar tarea")
    print("2. Ver lista de tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

gestor = GestorTareas()

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        titulo = input("Nombre de la tarea: ")
        fecha_limite = None  

        while True:  
            respuesta = input("¿Desea agregar una fecha límite? (si/no): ").strip().lower()
            if respuesta in ("si", "sí"):
                break
            elif respuesta in ("no", "n"):
                break
            else:
                print("Respuesta inválida. Escribe 'si' o 'no'.")

        if respuesta in ("si", "sí"):
            while True:
                fecha_input = input("Ingresa la fecha (YYYY-MM-DD): ")
                try:
                    fecha_limite = date.fromisoformat(fecha_input)
                    break
                except ValueError:
                    print("Formato inválido. Usa YYYY-MM-DD (ej: 2026-05-01)")

        gestor.agregar_tarea(titulo, fecha_limite)    
        print("-Tarea agregada-")

    elif opcion == "2":
        gestor.listar_tareas()

    elif opcion == "3":
        gestor.listar_tareas()
        try:
            numero = int(input("Ingrese el número de la tarea completada: "))
            gestor.completar_tarea(numero)
        except ValueError:
            print("Ingrese solo números")

    elif opcion == "4":
        gestor.listar_tareas()
        try:
            numero = int(input("Ingrese el numero de la tarea a eliminar: "))
            gestor.eliminar_tarea(numero)
        except ValueError:
            print("Ingrese solo números")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida, intenta de nuevo") 