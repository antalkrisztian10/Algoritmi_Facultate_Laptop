#din lista de adiacenta [[0,1],[0,2],[1,2],[1,3][3,4]] sa se construiasca matricea prezentata
#[[0,1,1,0,0],[1,0,1,1,0],[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,0]
import random


#def lista_matrice(lista):
#    lista = [[0,1],[0,2],[1,2],[1,3][3,4]]
#    marime_lista = len(lista)
#    matrice = [[0 for i in range(marime_lista)] for j in range(marime_lista)]
#    for i in range(lista):
#        for j in range(lista):
#            matrice[i][j]


def nr_elemente(lista):
    maxim = 0
    for element in lista:
        for e in element:
            if e > maxim:
                maxim = e
    return maxim
    matrice = []
    n = nr_elemente(lista) + 1
    for i in range(n):
        rand = []
        for j in range(n):
            rand.append(0)
        matrice.append(rand)
    for element in lista:
        x = element[0]
        y = element[1]
        matrice[x][y] = 1
        matrice[y][x] = 1


def lista_adiacenta(matrice):
    lista_rezultat = []
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 1 and i > j:
                lista_rezultat.append([i,j])


def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == dice2:
        return True
    else:
        return False
    v = 0
    for i in range(1000):
        v += roll_dice()
