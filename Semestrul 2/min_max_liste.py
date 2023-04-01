def min_max_lista(lista):
    min = lista[0]
    max = lista[0]
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    print(min,max)
    min1 = lista[0]
    max1 = lista[0]
    for i in range(len(lista)):
        if lista[i] > max1 and lista[i]!= max:
            max1 = lista[i]
        if lista[i] < min1 and lista[i]!= min:
            min1 = lista[i]
    print(min, min1, max, max1)

def min_max2(lista):
    lista.sort()
    min1 = lista[0]
    min2 = lista[1]
    max1 = lista[len(lista)-2]
    max2 = lista[len(lista)-1]
    prod_min = min1 + min2
    prod_max = max1 + max2
    print(min1,min2,max1,max2)
    print(prod_min,prod_max)

def parcurgere_m(matrice):
    sir = "abcd" # sir de aceeasi dimensiune cu n
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1 and i != j:
                print(sir[i], sir[j], end="/")

# Sa se scrie o functie Python recursica care sa returneze numarul de cifre egale cu zero ale unui numar natural transmis ca parametru
def nr_cifre_zero(n):
    if n == 0:
        return 1
    elif n < 10: # daca numarul are o singura cifra
        return 0
    else: # daca avem cel putin 2 cifre
        m = n % 10

def nr_zero(n):
    if n == 0:
        return 0
    if n % 10:
        return 1 + nr_zero(n//10)
    else:
        return nr_zero(n//10)


if __name__=="__main__":
    min_max_lista([1,2,4,5,6,7])
    min_max2([1, 2, 4, 5, 6, 7])
    parcurgere_m([[1,1,1],[1,1,1],[1,1,1]])
    print(nr_zero(10001))