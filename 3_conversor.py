# #Convierte de pesos mexicanos a dolares
# pesos_mexicanos = input("¿Cuántos pesos mexicanos tienes?: ")
# pesos_mexicanos = float(pesos_mexicanos)
# valor_dolar_mexico =  22
# total_dolares = pesos_mexicanos / valor_dolar_mexico
# total_dolares = round(total_dolares, 2)
# total_dolares = str(total_dolares)
# print("Tienes $" + total_dolares + " dólares.")

# #Convierte de dolares a pesos mexicanos.

# dollar = input("How many dollars do you have?")
# dollar = float(dollar)
# mexican_peso = 22
# dollar_total = mexican_peso * dollar
# dollar_total = round (dollar_total)
# dollar_total = str(dollar_total)
# print("You have $" + dollar_total + "mexican pesos.")

#Te pregunta que moneda quieres convertir a dolares.
#Si tenemos tres comillas python nos permite hacer una cadena de caracteres de varias líneas.

# menu = """
# Bienvenido al conversor de monedas 🎈

# 1 - Pesos Colombianos
# 2 - Pesos Argentinos
# 3 - Pesos Mexicanos

# Elige una opción: 

# """

# opcion = int(input(menu))

# if opcion == 1:
#     pesos_colombianos = input("¿Cuántos pesos colombianos tienes?: ")
#     pesos_colombianos = float(pesos_colombianos)
#     valor_dolar_colombianos =  3875
#     total_dolares = pesos_colombianos / valor_dolar_colombianos
#     total_dolares = round(total_dolares, 2)
#     total_dolares = str(total_dolares)
#     print("Tienes $" + total_dolares + " dólares.")
# elif opcion == 2:
#     pesos_argentinos = input("¿Cuántos pesos argentinos tienes?: ")
#     pesos_argentinos = float(pesos_argentinos)
#     valor_dolar_argentina =  65
#     total_dolares = pesos_argentinos / valor_dolar_argentina
#     total_dolares = round(total_dolares, 2)
#     total_dolares = str(total_dolares)
#     print("Tienes $" + total_dolares + " dólares.")
# elif opcion == 3:
#     pesos_mexicanos = input("¿Cuántos pesos mexicanos tienes?: ")
#     pesos_mexicanos = float(pesos_mexicanos)
#     valor_dolar_mexico =  25
#     total_dolares = pesos_mexicanos / valor_dolar_mexico
#     total_dolares = round(total_dolares, 2)
#     total_dolares = str(total_dolares)
#     print("Tienes $" + total_dolares + " dólares.")
# else:
#     print("Ingrese una opción correcta por favor.")


#Aprendiendo a no repetir codigo con funciones
def imprimir_dolares(valor_moneda):
    dinero_usuario = input("¿Cuánto dinero tienes?: ")
    dinero_usuario = float(dinero_usuario)
    valor_dolar =  valor_moneda
    total_dolares = dinero_usuario / valor_dolar
    total_dolares = round(total_dolares, 2)
    total_dolares = str(total_dolares)
    print("Tienes $" + total_dolares + " dólares.")


mensaje = """
Bienvenido al conversor de monedas 🎈

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción en número: 
"""

opcion = int(input(mensaje))

if opcion == 1:
    imprimir_dolares(3875)
elif opcion == 2:
    imprimir_dolares(65)
elif opcion == 3:
    imprimir_dolares(25)
else:
    print("Ingresa una opción correcta.")


