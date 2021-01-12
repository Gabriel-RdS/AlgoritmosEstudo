"""
Algorítmo de ordenação da página 31

Explicação do Algoritmo: https://www.youtube.com/watch?v=S5no2qT8_xg
"""


def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave
    return lista


arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))
