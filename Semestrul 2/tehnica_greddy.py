def greddy():
    T = int(input())
    M = list()
    M.sort()
    t = T
    i = 0
    while t > 0 and t <= M[i]:
        if M[i] <= t:
            M.append(M[i])
            t = t - M[i]
        i = i + 1

def greddy2():
    lista_timp_reparatie_masini = [2,3,50,20,10,3,2,5,1]
    lisa_masini_reparate = []
    T = int(input("Timp maxim de lucru: "))
    lista_timp_reparatie_masini.sort()
    t_ramas = T
    for i in range(len(lista_timp_reparatie_masini)):
        if lista_timp_reparatie_masini[i] <= t_ramas:
            t_ramas = t_ramas - lista_timp_reparatie_masini[i]
            lisa_masini_reparate.append(lista_timp_reparatie_masini[i])

    print(lisa_masini_reparate)
    print(t_ramas)

def greddy_while():
    lista_timp_reparatie_masini = [2, 3, 50, 20, 10, 3, 2, 5, 1]
    lisa_masini_reparate = []
    T = int(input("Timp maxim de lucru: "))
    lista_timp_reparatie_masini.sort()
    t_ramas = T
    i = 0
    while t_ramas > 0 and t_ramas >= lista_timp_reparatie_masini[i]:
        if lista_timp_reparatie_masini[i] <= t_ramas:
            t_ramas = t_ramas - lista_timp_reparatie_masini[i]
            lisa_masini_reparate.append(lista_timp_reparatie_masini[i])
        i = i + 1
    print(lisa_masini_reparate)
    print(t_ramas)

def suma_recursiv(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        mijloc = len(lista) // 2
        return suma_recursiv(lista[:mijloc]) + suma_recursiv(lista[mijloc:])

def suma_recusriv_par(lista):
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]
        else:
            return 0
    else:
        mijloc = len(lista) // 2
        return suma_recursiv(lista[:mijloc]) + suma_recursiv(lista[mijloc:])

def suma_recusriv_elemente(lista):
    if len(lista) == 1:
        if lista[0] % 2 != 0:
            return 1
        else:
            return 0
    else:
        mijloc = len(lista) // 2
        return suma_recursiv(lista[:mijloc]) + suma_recursiv(lista[mijloc:])


if __name__=="__main__":
   greddy_while()
   print(suma_recursiv([4,2,4,1,2]))
