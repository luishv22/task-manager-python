from datetime import date
from tareas import GestorTareas

# Menú principal del programa
def mostrar_menu():
    print("====================")
    print("  GESTOR DE TAREAS  ")
    print("====================")
    print("1. Agregar tarea")
    print("2. Ver lista de tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

# Instancia principal que gestiona todas las tareas
gestor = GestorTareas()

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    # Opción 1: Agregar tarea
    if opcion == "1":
        titulo = input("Nombre de la tarea: ")
        fecha_limite = None  

        # Validar respuesta del usuario (si/no)
        while True:  
            respuesta = input("¿Desea agregar una fecha límite? (si/no): ").strip().lower()
            # Solo permite continuar si la respuesta es válida
            if respuesta in ("si", "sí"):
                break
            elif respuesta in ("no", "n"):
                break
            else:
                print("Respuesta inválida. Escribe 'si' o 'no'.")
        
        # Si el usuario quiere agregar una fecha, se solicita hasta que sea válida
        if respuesta in ("si", "sí"):
            while True:
                fecha_input = input("Ingresa la fecha (YYYY-MM-DD): ")
                try:
                    # Convierte el texto a un objeto date
                    fecha_limite = date.fromisoformat(fecha_input)
                    break
                except ValueError:
                    print("Formato inválido. Usa YYYY-MM-DD (ej: 2026-05-01)")

        # Se crea la tarea (con o sin fecha)
        gestor.agregar_tarea(titulo, fecha_limite)    
        print("-Tarea agregada-")

    # Opción 2: Listar tareas
    elif opcion == "2":
        gestor.listar_tareas()

    # Opción 3: Completar tarea
    elif opcion == "3":
        gestor.listar_tareas()
        try:
            # Se pide el número de la tarea a completar
            numero = int(input("Ingrese el número de la tarea completada: "))
            gestor.completar_tarea(numero)
        except ValueError:
            print("Ingrese solo números")

    # Opción 4: Eliminar tarea
    elif opcion == "4":
        gestor.listar_tareas()
        try:
            # Se pide el número de la tarea a eliminar
            numero = int(input("Ingrese el numero de la tarea a eliminar: "))
            gestor.eliminar_tarea(numero)
        except ValueError:
            print("Ingrese solo números")
    
    # Opción 5: Salir
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    # Opción inválida
    else:
        print("Opción inválida, intenta de nuevo") 