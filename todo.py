from datetime import datetime
import json


class Tarea:
    def __init__(self, texto:str, completada:bool, prioridad:str) -> None:
        self.texto=texto
        self.completada=completada
        self.prioridad=prioridad
        self.fecha_creada=datetime.now()

    def to_dict(self):
        return {
            'texto':self.texto,
            'completada':self.completada,
            'prioridad':self.prioridad,
            'fecha_creacion':self.fecha_creada.isoformat()
        }

class Lista:

    def agregar_tarea(self, tarea:Tarea):
        with open('tareas.json','r+',encoding='utf-8') as tareas:
            for t in tareas:
                if t==tarea:
                    print('ya existe esta tarea')
                    return
            json.dump(tarea.to_dict(), tareas)
        return True


lista=Lista()

lista.agregar_tarea(Tarea('Ir a buscar el pollo',False,'Alta'))