from datetime import datetime


class Tarea:
    def __init__(self, texto:str, completada:bool, prioridad:int, fecha_creada:datetime) -> None:
        self.texto=texto
        self.completada=completada
        self.prioridad=prioridad
        self.fecha_creada=fecha_creada

class Lista:

    def __init__(self) -> None:
        self.tareas=[]

    def agregar_tarea(self, ):
        pass
    