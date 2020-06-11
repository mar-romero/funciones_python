#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import random


def ej1():
    # Ejercicios con funciones del sistema

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle
    https://docs.python.org/3.7/library/functions.html

    La función debe retornar el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado
    '''
    numeros = [4,2,6,7,12]
    def promedios(numero):
        def sumar(numero):
            resultado = 0
            for x in numeros:
                resultado += x
            print ('La suma de la lista:', resultado)
            return resultado
        def cantidad(numero):
            cantidad_numeros = len(numeros)
            print('La cantidad de numeros en la listas es:', cantidad_numeros)
            return cantidad_numeros
        res = sumar(numeros)
        cant = cantidad(numeros)
        if cant > 0:
            pro = ( res / cant)
            print ('El promedio de la lista es', pro)
        else:
            print('La lista se encuentra vacia')
    promedios(numeros)



def ej2():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    
    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.
    def lista_aleatoria (inicio, fin, cantidad)

    Dicha función debe retornar la lista de elementos random generados.
    '''
    inicio1 = 0
    fin1 = 20
    def lista_aleatoria (inicio, fin, ramdom):
        numero = random.randrange(inicio1, fin1+1)
        numero_1 = random.randrange(inicio1, fin1+1)
        lista = [numero_1, numero]
        print('Los numeros ramdom son:', lista)
        return lista
    lista_aleatoria (inicio1, fin1, 2)
    #NOSE CUAL DE LOS 2 ESTA BIEN ESTE DE ABAJO LO USE PARA EL EJ 4
    
    # Inove: Esta opcion es correcta, solo falta agregar el parametro
    # cantidad para definir el tamaño de la lista
    def lista_aleatorios(n,m):
        lista = [0] * 2
        for i in range(2):
          lista[i] = random.randrange(inicio, fin+1)
        return lista
    lista_al = lista_aleatorios(inicio, fin)
    print('La lista es:', lista_al)
    
    # Inove: Con la modificacion propuesta tendriamos
    def inove_lista_aleatoria(n,m,cantidad):
        lista = [0] * cantidad
        for i in range(cantidad):
          lista[i] = random.randrange(n, m+1)
        return lista
    lista_al = lista_aleatorios(inicio, fin)
    print('La lista es:', lista_al)

    
    # numeros = lista_aleatoria (inicio, fin, cantidad)

    # Imprima en pantalla la lista de elementos generados
    # print(....)

    # Utilice el método random.choice para obtener 2 numeros
    # de la lista de elementos generados
    # numero_1 = random.choice(...)
    # numero_2 = random.choice(...)

    # Importar en este programa/documento el modulo "math"
    # Calcular la raiz cuadrada (square root) de esos
    # dos numeros obtenidos utilizando el método del
    # módulo "math" que crea correspondiente
    # Documentación oficial de math
    # https://docs.python.org/3.7/library/math.html
    # NOTA: Puede buscar en el medio que prefiera la info
    # solicitada

    # raiz_cuadrada_1 = ....
    # raiz_cuadrada_2 = ....
    import math
    x = range(20)
    
    numero_3 = random.choice(x)
    numero_2 = random.choice(x)
    raiz_cuadrada_3 = math.sqrt( numero_3 )
    raiz_cuadrada_2 = math.sqrt( numero_2 )
    print('Los numero elegidos son:' , numero_2, numero_3)
    print ('La raiz cuadrada de los numeros son: {:.2f}, {:.2f} '.format(raiz_cuadrada_2, raiz_cuadrada_3))



def ej3():
    # Ejercicios de listas y métodos
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python
    La función no hace falta que retorne la lista ordenada,
    ya que al tratarce de una lista se pasa como referencia
    a la función (es decir que las modificaciones realizadas
    en la función afectan a la variable pasada como argumento)

    '''
    def orden(lista):
        numeros.sort()
        return numeros 
    orden(numeros)
    print(numeros)


def ej4():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado 
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''
    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)
    
    # Inove: La funcion es correcta, pero cuidado con randrange
    # Para que el 9 sea incluido debemos colocar 9+1, o en este caso m+1
    def lista_aleatorios(n,m):
        lista = [0]  * 5
        for i in range(5):
          lista[i] = random.randrange(n,m)  
        return lista
    
    lista_al = lista_aleatorios(1,9)
    print('La lista es:', lista_al)
    if lista_al.count(1) > 0:
        veces_1 = lista_al.count( 1 )
        print("El numero 1 se repite:", veces_1)
    if lista_al.count(2) > 0:
        veces_2 = lista_al.count(2)
        print("El numero 2 se repite:", veces_2)
    if lista_al.count(3) > 0:
        veces_3 = lista_al.count(3)
        print("El numero 3 se repite:", veces_3)
    if lista_al.count(4) > 0:
        veces_4 = lista_al.count(4)
        print("El numero 4 se repite:", veces_4)
    if lista_al.count(5) > 0:
        veces_5 = lista_al.count(5)
        print("El numero 5 se repite:", veces_5)
    if lista_al.count(6) > 0:
        veces_6 = lista_al.count(6)
        print("El numero 6 se repite:", veces_6)
    if lista_al.count(7) > 0:
        veces_7 = lista_al.count(7)
        print("El numero 7 se repite:", veces_7)
    if lista_al.count(8) > 0:
        veces_8 = lista_al.count(8)
        print("El numero 8 se repite:", veces_8)
    if lista_al.count(9) > 0:
        veces_9 = lista_al.count(9)
        print("El numero 9 se repite:", veces_9)
    # Hay otra forma de hacerlo, sin hacer numero por numero? con bucle?
    
    # Inove: Si señor! vamos de a poco, lo importante de la funcion "contar"
    # solicita es solo buscar y contar "1 solo" elemento deseado:
    # "cuenta la cantidad de veces que un elemento pasado
    #   por parámetro se repite en la lista."
    # Esto quiere decir que nuestra funcion contar solo deberá preocuparse
    # por contar un elemento
    # Si por ejemplo tengo mi lista:
    #  --> lista_al, supongamos que la lista se genero con los siguientes valores
    # (5 numeros aleatorios del 1 al 9):
    # [1,3,2,1,8]
    # Y supongamos que queremos saber cuantas veces se rapite el numero "1" la funcion
    # contar es tan simple como:
    
    def contar(lista, elemento):
        cantidad_repeticiones = lista.count(elemento)
        return cantidad_repeticiones
    
    lista_al = [1,3,2,1,8]  # Estoy generando a mano la lista para realizar pruebas controladas
    numero_a_contar = 1
    repeticiones = contar(lista_al, numero_a_contar)
    print('El numero', numero_a_contar, 'se repite', repeticiones)
    
    # Como podrás apreciar en este caso no es neceserario un bucle
    # ya que no es necesario buscar más de un elemento distinto en la lista


    
def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "buscar",
    que genere una lista con los índice de las posiciones
    en donde se encuentra dicho elemento en la lista.
    Si el elemento en la lista no existe, la función
    debe retornar una lista vacia.
    Para encontrar los índices del elemento en la lista
    puede usar el método "index" o bucles.
    Recuerde que el elemento puede repetirse más de una
    vez en la lista.
    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)
    def lista_aleatorios(n,m):
        lista = [0]  * 5
        for i in range(5):
          lista[i] = random.randrange(1,9)
        return lista
    lista_al = lista_aleatorios(1,9)
    print('La lista es:', lista_al)
    if 1 in lista_al: 
        print
    try:
        pos_1 = lista_al.index(1)
        print("El 1 está en la posición {} ".format(pos_1))
    except:
        print("Lo siento, el 1 no está en la lista")
    try:
        pos_2 = lista_al.index(2)
        print("El 2 está en la posición {} ".format(pos_2))
    except:
        print("Lo siento, el 2 no está en la lista")
    try:
        pos_3 = lista_al.index(3)
        print("El 3 está en la posición {} ".format(pos_3))
    except:
        print("Lo siento, el 3 no está en la lista")
    try:
        pos_4 = lista_al.index(4)
        print("El 4 está en la posición {} ".format(pos_4))
    except:
        print("Lo siento, el 4 no está en la lista")
    try:
        pos_5 = lista_al.index(5)
        print("El 5 está en la posición {} ".format(pos_5))
    except:
        print("Lo siento, el 5 no está en la lista")
    try:
        pos_6 = lista_al.index(6)
        print("El 6 está en la posición {} ".format(pos_6))
    except:
        print("Lo siento, el 6 no está en la lista")
    try:
        pos_7 = lista_al.index(7)
        print("El 7 está en la posición {} ".format(pos_7))
    except:
        print("Lo siento, el 7 no está en la lista")
    try:
        pos_8 = lista_al.index(8)
        print("El 8 está en la posición {} ".format(pos_8))
    except:
        print("Lo siento, el 8 no está en la lista")
    try:
        pos_9 = lista_al.index(9)
        print("El 9 está en la posición {} ".format(pos_9))
    except:
        print("Lo siento, el 9 no está en la lista")
    # Esto es lo mas cerca que pude estar de lograr el ejercicio
    # Tendrian la solucion o un ejemplo
    # Quiero que diga se encuentra en la posicion 1, 2 y 3
    # Pero no se como hacerlo y no dejarlo en blanco su no esta en la lista
    
    # Inove: La forma de resolverlo está perfecta, se te complicó
    # porque en realidad no hay que buscar la posición de todos lus números
    # posibles del 1 al 9, sino que hay que buscar los índices donde aparece el
    # elemento deseado a buscar.
    # Mismo ejemplo que en el anterior ejercicio, supongamos que tengo mi 
    # lista aleatorio de 5 elementos con números del 1 al 9:
    # --> lista_al, supongamos que la lista se genero con los siguientes valores
    # [1,3,2,1,8]
    # Mi funcion "buscar" debe revisar en que indices se encuentra el elemento deseado
    # a buscar. Esta tarea la puedo realizar con un bucle, recorriendo toda la lista
    # y almacenando los indices en donde encontre el elemento objeto
    def buscar(lista, elemento):
        lista_indices = []
        for i in range(len(lista)):
            if(lista[i] == elemento):
                # El elemento se encuentra en este indice
                lista_indices.append(i)  # Almaceno el indice
        # Terminado el bucle retorno la lista de indices
        return lista_indices
    
    lista_al = [1,3,2,1,8]  # Estoy generando a mano la lista para realizar pruebas controladas
    numero_a_buscar = 1
    indices = buscar(lista_al, numero_a_buscar)
    print('El numero', numero_a_buscar, 'se encuentra en', indices)
    
    # Este ejercicio tambíen puede resolverse usando solo el método
    # index, pero es bastante problematico cuando se desea buscar
    # todas las posiciones en donde se encuntra el numero



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
