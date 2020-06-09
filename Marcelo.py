'''
Mis modulo
Autor: Romero Marcelo
Version: 1.1
'''

__author__ = "Romero Marcelo"
__email__ = "romero-ar@hotmail.com"
__version__ = "1.1"


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
    return

def lista_aleatorios(n,m):
    import random
    lista = [0]  * 5
    for i in range(5):
        lista[i] = random.randint(1,6)
    return lista   
         


def contar (n):
    def lista_aleatorios(n,m):
        lista = [0]  * 5
        for i in range(5):
          lista[i] = random.randrange(1,9)
        return lista
    lista_al = lista_aleatorios(1,9)
    print('La lista es:', lista_al)
    if lista_al.count(1) > 1:
        veces_1 = lista_al.count( 1 )
        print("El numero 1 se repite:", veces_1)
    if lista_al.count(2) > 0:
        veces_2 = lista_al.count(2)
        print("El numero 2 se repite:", veces_2)
    if lista_al.count(3) > 1:
        veces_3 = lista_al.count(3)
        print("El numero 3 se repite:", veces_3)
    if lista_al.count(4) > 1:
        veces_4 = lista_al.count(4)
        print("El numero 4 se repite:", veces_4)
    if lista_al.count(5) > 1:
        veces_5 = lista_al.count(5)
        print("El numero 5 se repite:", veces_5)
    if lista_al.count(6) > 1:
        veces_6 = lista_al.count(6)
        print("El numero 6 se repite:", veces_6)
    if lista_al.count(7) > 1:
        veces_7 = lista_al.count(7)
        print("El numero 7 se repite:", veces_7)
    if lista_al.count(8) > 1:
        veces_8 = lista_al.count(8)
        print("El numero 8 se repite:", veces_8)
    if lista_al.count(9) > 1:
        veces_9 = lista_al.count(9)
        print("El numero 9 se repite:", veces_9)
    # Hay otra forma de hacerlo, sin hacer numero por numero? con bucle?
    return

def orden(lista):
    numeros.sort()
    return numeros 
