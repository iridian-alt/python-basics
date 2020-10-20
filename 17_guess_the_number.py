#Modulo es un paquete de codigo escrito por las personas que hicieron python que nosotros tenemos disponibles.
#el paquete de random contiene funciones para trabajar con aleatoriedad con el lenguaje.
import random 

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('Ganaste')

if __name__ == '__main__':
    run()  