#Aqui le implemente un sistema de vidas, saludos.
import random

def run():
    numero_random = random.randint(1, 100)
    numero_elegido = int(input("Introduce un numero: "))
    vidas = 5

    while numero_random != numero_elegido :

        if numero_random < numero_elegido : 
            print("Elige un numero mas pequeño.")
            vidas -= 1

        elif numero_random > numero_elegido : 
            print("Elige un numero mas grande.")
            vidas -= 1

        if vidas == 0 :
            print("GAME OVER")
            break

        print("Tienes", vidas, "vidas")
        numero_elegido = int(input("Introduce numero: "))
        
    if numero_random == numero_elegido : 
        print("FELICIDADES GANASTE")


if __name__ == "__main__" : 
    run()