# Prima problema
def nr_opt(n):
    sir = str(n)
    c = 0
    if sir[len(sir)-1] == "8":
        c = 1
    if len(sir)-1 <= 0:
        return c
    return c + nr_opt(sir[:len(sir)-1])


# A doua problema
def matrice():
    n = 4
    sdp = 0
    matrice = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i < j:
                sdp += matrice[i][j]
    print("SDP=",sdp)


# A treia problema
def dictionar():
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z']
    c = 1
    ht = {'a':'A-1','b':'B-1','c':'C-1','d':'D-1'}

if __name__ == "__main__":
    print(nr_opt(8156878))
    matrice()
    dictionar()
