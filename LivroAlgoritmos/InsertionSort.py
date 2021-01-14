"""
Algorítmo de ordenação da página 31

Explicação do Algoritmo insertionSort: https://www.youtube.com/watch?v=S5no2qT8_xg

Explicação do Algoritmo PesquisaLinear: ->
https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/pesquisa-linear/

"""


# -------------------------------------------------------------
def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave
    return lista


arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))
# -------------------------------------------------------------


# -------------------------------------------------------------
# Execícios página 15(34 de 239)
# Reescrever o insertionSort para que saia em ordem decrescente
def insertionSort2(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] < chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave
    return lista


arranjo2 = [31, 41, 59, 26, 41, 58]
print(insertionSort2(arranjo2))
# -------------------------------------------------------------

# -------------------------------------------------------------
# Execícios página 16(3 de 239)
# Pesquisa linear


def pesquisaLinear(arranjo, elementoDesejado):
    for elemento in arranjo:
        if elementoDesejado == elemento:
            return f'Elemento está presente no arranjo'
    return f'Elemento não está presente no arranjo'


arranjo3 = [31, 41, 59, 26, 41, 58, 77, 39, 100, 22]
print(pesquisaLinear(arranjo3, 100))

# -------------------------------------------------------------
