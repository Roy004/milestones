import os
import time
import random


if __name__=='__main__':
    num=random.randint(0,100)
    while True:
        print('El sistema ha seleccionado un número al azar entre 0 y 100 \n intente adivinarlo ;)')
        
        try:
            n=int(input('Intoduzca el numero: '))
            
        except Exception as error:
            print('Ese no es un número')
            os.system('clear')
            continue

        if n==num:
            print('Felicidades, ha adivinado')
            op=input('Desea jugar de nuevo (y/n)')
            if op =='y'or op=='Y':
                num=random.randint(0,100)
                os.system('clear')
                continue
            else:
                break
        elif n<num:
            os.system('clear')
            print('te quedaste corto!!!')
            

        else:
            os.system('clear')
            print('te fuiste por encima!!!')

        




