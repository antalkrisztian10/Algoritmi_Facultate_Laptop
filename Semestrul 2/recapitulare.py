# Sa se defineasca o functie care primeste ca parametru un numar natural si o lista de numere naturale si reintoarece true daca nr trimis ca parametru este in lista si false in caz contrar.

def lista(nr_natural,lista_numere):
    if nr_natural in lista_numere:
        return True
    else:
        return False

def lista1(lista,n):
    for i in range(len(lista)):
        if n== lista[i]:
            return True
    return False

# Definiti o functie care primeste ca parametru o matrice de numere matruale si functia sa imi reintoarca true daca imi gaseste numar natural si false in caz contrat.

def cautare(matrice):
    for i in matrice:
        for element in i:
            if type(element) == int and element >= 0 and element == int(element):
                return True
    return False

def cautam(matrice,n):
    r = len(matrice)
    c = len(matrice[0])
    for i in range(r):
        for j in range(c):
            if matrice[i][j] == n:
                return True
    return False

# Sa se scrie o functie recursiva care calculeaza factorialul unui numar natrural primit ca parametru.

def recursiv(n):
    if n == 0:  # se verifica daca numarul natrula este = 0
        return 1  # daca este egal cu 0 rezultatul este 1
    else:   # in caz contrar se calculeaza factorial de numar
        return n * recursiv(n-1)

def digits(n):
    d = n//10
    r = n%10
    return recursiv(d)

# Sa se scrie o functie care implementeaza bubble sort pe o lista.
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

if __name__=="__main__":
    print(lista1([1,3,4,5],4))

    lista_numere = [1,2,3,4,5]
    print(lista(4,lista_numere))

    matrice1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(cautare(matrice1))

    print(recursiv(2))

    print(bubble_sort([2,10,6,7,8]))