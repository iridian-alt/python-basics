##DE TEXTO A NÚMERO ENTERO.
#dejando solo con input estamos diciendo que son str.
number_one = input("Please, write a number: ")
number_two = input("Please, write another number: ")
print(number_one + number_two)
#salida> "55"

#con int los convertimos a enteros.
number_one = int(input("Please, write a number: "))
number_two = int(input("Please, write another number: "))
print(number_one + number_two)
#salida> 10

##DE DECIMAL A NUMERO ENTERO
#No lo redondea solo saca el numero entero.
numero_decimal = 2.9
int(2.9)
#salida> 2

##DE DECIMAL O ENTERO A TEXTO
numero = 7.8
str(numero)
#salida> '7.8'

