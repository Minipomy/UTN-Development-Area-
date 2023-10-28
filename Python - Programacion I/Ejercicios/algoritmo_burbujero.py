import random as rd
from time import time
import os

ITERACIONES = 100
lista_random = [rd.randint(0, 100) for _ in range(ITERACIONES)]

def algoritmo_burbuja(lista):
    n = len(lista)
    for index_1 in range(n):
        for index_2 in range(0, index_1-1):
            if lista[index_2] > lista[index_2+1] :
                lista[index_2], lista[index_2+1] = lista[index_2+1], lista[index_2]
    return lista



def algo():
    lista_random_nueva = [rd.randint(0, 5)]
    for index in range(len(lista_random_nueva)):
        print(lista_random_nueva[index:])


if __name__ == '__main__':
    start = time()
    print("Lista desordenada:", lista_random)
    algoritmo_burbuja(lista_random)
    print("Lista ordenada:", lista_random)
    algo()
    end = time()
    total_tiempo = end - start
    print(f'Tardo: {total_tiempo}')
    