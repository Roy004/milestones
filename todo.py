from datetime import datetime
import json
import pprint
import random
import sys


class Tarea:
    def __init__(self, texto:str, id:int, completada:bool=False, prioridad:str='Media') -> None:
        self.id=id
        self.texto=texto
        self.completada=completada
        self.prioridad=prioridad
        self.fecha_creada=datetime.now()

    def to_dict(self):
        return {
            'texto':self.texto,
            'id':self.id,
            'completada':self.completada,
            'prioridad':self.prioridad,
            'fecha_creacion':self.fecha_creada.isoformat()

        }

class Lista:

    NOMBRE_ARCHIVO="tareas.json"

    @staticmethod
    def _cargar_tareas():
        try:
            with open(Lista.NOMBRE_ARCHIVO, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
        
    @staticmethod
    def guardar_tarea(tarea:Tarea):
        datos=Lista._cargar_tareas()

        if len(datos)>tarea.id:
            datos.insert(tarea.id,tarea.to_dict())
        else:
            datos.append(tarea.to_dict())

        with open(Lista.NOMBRE_ARCHIVO, 'w') as f:
            json.dump(datos, f, indent=4)

    @staticmethod
    def limpiar_tareas():
        with open(Lista.NOMBRE_ARCHIVO, "w") as f:
            json.dump([],f,indent=4)

    @staticmethod
    def _encontrar_dic_bin(lista: list[dict], id: int):
        mitad=len(lista)/2
        if lista[id]['id'] < id:
            return Lista._encontrar_dic_bin(lista[mitad:], id)
        elif lista[id]['id'] > id:
            return Lista._encontrar_dic_bin(lista[:mitad],id)
        else:
            return lista[id]

    @staticmethod
    def selec_tarea(id:int):
        try:
            with open(Lista.NOMBRE_ARCHIVO, "r") as f:
                datos=json.load(f)
                dic=Lista._encontrar_dic_bin(datos, id)
        except json.JSONDecodeError:
            return {}
        return {}
    
    @staticmethod
    def obtener_tareas():
        try:
            with open('tareas.json','r') as f:
                return json.load(f)
        except:
            return []
    
    @staticmethod
    def obt_cant_tareas():
        try:
            with open('tareas.json','r') as f:
                lista=json.load(f)
                return len(lista)
        except json.JSONDecodeError:
            return 0
        

# Lista.limpiar_tareas()

# for i in range(0,1000):
    
#     Lista.guardar_tarea(Tarea(f'Tarea numero {i}',i,prioridad=random.choice(['Alta', 'Media', 'Baja'])))


while True:
    cant=Lista.obt_cant_tareas()

    print('Bienvenido a su sistema de gestion de tareas\nSeleccione una opción:')
    print('1-Agregar una tarea')
    print('2-Mostrar tareas')
    print('3-Seleccionar una tarea')
    print('4-Marcar una tarea como completada')
    print('0-Salir de la app')

    try:
        op=int(input('Escriba su opcion: '))
    except ValueError:
        print('Introduzca solo el número de la opcion deseada!')
        continue

    if op == 0:
        sys.exit()
    elif op == 1:
        txt = input('Tarea: ')
        prioridad_in = input('Prioridad (A-Alta, M-Media, B-Baja): ')
        tarea=Tarea(txt, cant, prioridad = prioridad_in)
        Lista.guardar_tarea(tarea)
    elif op == 2:
        lista=Lista.obtener_tareas()
        for d in lista:
            pprint.pprint(d)

        #Para continuar:
        cont=input('Desea continuar (s/n): ')
        if cont == 's':
            continue
        elif cont == 'n':
            sys.exit()
    elif op == 3:
        input('Proximamente ...(Enter para continuar)')
        continue
    elif op==4:
        input('Proximamente ...(Enter para continuar)')
        continue