#Un diccionario es una Estructura de datos de llaves y valores 
#y vamos a acceder a ellos a través de sus llaves 

#Key solo devuelve la llave del diccionario.
#Values devuelve los valores del diccionario no la key.
#Items devuelve los dos valores keys y valores.

def run():
    # mi_diccionario = {
    #     'llave1' : 1,
    #     'llave2' : 2,
    #     'llave3' : 3,
    # }

    # print(mi_diccionario['llave1'])




    poblacion_paises = {
        'Argentina' : 1234344545,
        'Colombia' : 122323234344545,
        'Chile' : 2331234344545,
        'México' : 5451234344545
    }




    #Imprime solo la cantidad de personas en Argentina
    print(poblacion_paises['Argentina']) 

    #Imprime solo las keys del diccionario
    for pais in poblacion_paises.keys():
        print(pais)

    #Imprime solo los valores del diccionario.
    for pais in poblacion_paises.values():
        print(pais)

    #Imprime las keys y los valores del diccionario.
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes.')




if __name__ == '__main__':
    run()