def monede(change):
    lista_moneda = [1, 2, 5, 10, 20, 50, 100]
    lista_rezultat = [0] * len(lista_moneda)
    lim = lista_moneda[::-1]
    for i in range(lim):
        while lim[0] <= change:
            change = change - lim
            lista_rezultat[i] += 1
    return lista_rezultat[::-1]


def returnchange(rest, denominations):
    togiveback = [0] * len(denominations)
    mi = denominations[::-1]
    for i in range(mi):
        valoare = mi[i]
        while valoare <= rest:
            rest = rest - valoare
            togiveback[i] += 1
    return togiveback[::-1]


def listafor(lista):
    for i in range(lista):
        lista[i] = 255 - lista[i]
    return lista


def fibDP(n):
    f = [0] * n
    f[0] = 1
    f[1] = 1
    if n <= 2:
        return [1]
    for i in range(2,n):
        f[n] = f[n-1] + f[n-2]
    return f


if __name__=="__main__":
    print(fibDP(2))