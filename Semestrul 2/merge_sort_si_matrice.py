# Se da o matrice patratica sa se determine elementul care contine valoarea maxima si elementrul care contine valoarea minima
def matrice():
    n = 0
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i],[j] = int(input())

def matrice_min(matrice):
    m = len(matrice)
    n = len(matrice[0])
    # definesc min cu o valoare foarte mare ex: 999999
    # definesc max cu o valoare mica , de ex: 0
    min = 999999
    max = 0
    imax = ""
    imin = ""
    # parcurge matrice
    # intr-o matrice i si j reprezinta indicii , iar un element al matricei se regaseste folosind  expresia [i][j]
    for i in range(m):
        for j in range(n):
            if matrice[i][j] > max:
                max = matrice[i][j]
                imax = i + "," + j
            if matrice[i][j] < min:
                min = matrice[i][j]
                imin = i + "," + j
    print("Maxim: " , max)
    print("Minim: " , min)

# Se da o matrice patratica sa se genereze elementele matricii dupa urmatoarele reguli:
# elementele pentru care produsul indicilor este un nr par vor avea valoarea 1
# elementele pentru care produsul indicilor este un nr impar vor avea valoarea 0
# elementele de pe diagonala principala vor avea valoarea 2.

def matrice_patratica(n):
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrice[i][j] = 2
            elif (i * j) % 2 == 0:
                matrice[i][j] = 1
            else:
                matrice[i][j] = 0
    return matrice

def matrice_generare(matrice):
    m = len(matrice)
    n = len(matrice[0])
    for i in range(m):
        for j in range(n):
            if (i*j) % 2 == 0:
                matrice[i][j] = 1
            if i * j % 2 != 0:
                matrice[i][j] = 0
            if i == j:
                matrice[i][j] = 2

def unire(listas,listad):
    rezultat = []
    i = 0
    j = 0
    while i < len(listas) and j < len(listad):
        if(listas[i] < listad[j]):
            rezultat.append(listas[i])
            i = i + 1
        else:
            rezultat.append(listad[j])
            j = j + 1
    while i < len(listas):
        rezultat.append(listas[i])
        i = i + 1
    while j < len(listad):
        rezultat.append(listad[j])
        j = j + 1
    return rezultat

def msort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mij = len(lista) // 2
        stanga = msort(lista[:mij])
        dreapta = msort(lista[mij:])

        return unire(stanga, dreapta)


if __name__=="__main__":
    print(msort([2,5,10,25,3,1,8]))