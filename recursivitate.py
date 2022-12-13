def cautaresir(sirprincipal, subsir):
    i = 0
    n = len(sirprincipal) - len(subsir)
    while i <= n:
        j = 0
        while j < len(subsir):
            if sirprincipal[i+j] != subsir[j]:
                j = j + 1
                break
            else:
                j = j + 1
        if j == len(subsir):
            return i
        i = i + j
    return -1

def adunare(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

def adunarerec(n):
    if n == 1:
        return 1
    return n + adunarerec(n-1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    f = 0
    t1 = 0
    t2 = 1
    for i in range(2, n+1):
        f = t1 + t2
        t1 = t2
        t2 = f
    return f

# Fibonacci recursiv
# F(n) = F(n-1)+F(n-2)
def fibrec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibrec(n-1) + fibrec(n-2)

# de realizat o functie recursiva care imi determina nr. de aparitii al cifrei 0 intr-un nr.natural

def functie_recursiva(n): # Varianta 1
    sir = str(n)
    c = 0
    if sir[len(sir)-1]=="0":
        c = 1
    if len(sir)-1 <= 0:
        return c
    return c + functie_recursiva(int(sir[:len(sir)-1]))

def nr_zero(n): # Varianta 2
    c = 0
    if n == 0:
        return 0
    if n % 10 == 0:
        c = 1
    return c + nr_zero(n // 10)

# sa se realizeze o functie care ia ca parametru un nr. natural si il reintoarce in ordine inversa a unitatilor numarului.
# 20110 -> 0 1 1 0 2

def nr_reintors(n):
    sir = str(n)  # convertesc nr,natural in sir
    c = sir[len(sir)-1]  # extrag ultimul element
    if len(sir)-1 <= 0:  # verific daca nu cumva am ajuns la sfarsit
        return c
    return c + " , " + nr_reintors(int(sir[:len(sir) - 1]))



if __name__ =="__main__":
    # print(cautaresir("caini de tractiune husky", "ca"))
    # print(adunare(5))
    # print(adunarerec(5))
    # print(factorial(5))
    # print(fibonacci(15))
    # print(fibrec(15))
    print(nr_reintors(2100111010))