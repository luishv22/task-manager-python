from datetime import date
import json

class Tarea:
    """Representa una tarea con estado y fecha opcional."""

    def __init__(self, titulo, estado=False, fecha_limite=None):
        self.titulo = titulo
        self.estado = estado
        self.fecha_limite = fecha_limite

    def __str__(self):
        """Devuelve una representación legible de la tarea."""
        simbolo = "✅" if self.estado else "❎"

        if self.fecha_limite:
            fecha_formateada = self.fecha_limite.strftime("%d/%m/%Y")
            return f"{simbolo} {self.titulo} (Límite: {fecha_formateada})"
        else: 
            return f"{simbolo} {self.titulo}"

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.estado = True

class GestorTareas:
    """Gestiona tareas y su almacenamiento en JSON."""

    def __init__(self):
        self.tareas = []
        self.cargar_tareas()

    def agregar_tarea(self, titulo, fecha_limite=None):
        """Agrega una nueva tarea."""
        tarea = Tarea(titulo, False, fecha_limite)
        self.tareas.append(tarea)
        self.guardar_tareas()

    def listar_tareas(self):
        """Muestra todas las tareas."""
        if not self.tareas:
            print("No hay tareas registradas")
            return
        
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea}")

    def completar_tarea(self, numero):
        """Marca la tarea completada."""
        try:
            indice = numero - 1
            self.tareas[indice].marcar_completada()
            print("Tarea completada ✅")
            self.guardar_tareas()

        except IndexError:
            print("Número invalido ❎")


    def eliminar_tarea(self, numero):
        """Elimina la tarea."""
        try:
            indice = numero - 1
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea eliminada: {tarea_eliminada.titulo}")
            self.guardar_tareas()
            
        except IndexError:
            print("La tarea no existe")


    def guardar_tareas(self):
        """Guarda las tareas en un archivo JSON."""
        datos = []

        for tarea in self.tareas:
            datos.append({
                "titulo": tarea.titulo,
                "estado": tarea.estado,
                "fecha_limite": tarea.fecha_limite.isoformat() if tarea.fecha_limite else None
            })
            
        with open("tareas.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)


    def cargar_tareas(self):
        """Carga las tareas desde un archivo JSON."""
        try:
            with open("tareas.json", "r") as archivo:
                datos = json.load(archivo)
            
            for tarea in datos:
                titulo = tarea["titulo"]
                estado = tarea["estado"]
                fecha_str = tarea.get("fecha_limite")

                if fecha_str:
                    fecha_limite = date.fromisoformat(fecha_str)
                else:
                    fecha_limite = None

                nueva_tarea = Tarea(titulo, estado, fecha_limite)
                self.tareas.append(nueva_tarea)

        except FileNotFoundError:
            pass