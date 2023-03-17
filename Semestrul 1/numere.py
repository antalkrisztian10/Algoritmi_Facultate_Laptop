def adunare2():
   print("Va rog sa introduceti un numar natural de cel putin 2 cifre:")
   x = int(input())
   s = 0
   z = x % 10
   u = x // 10 % 10
   n = z + u
   print("Suma dintre cifra zecilor si cifra unitatilor este:", n)


def adunare3():
    print("Va rog sa introduceti un numar natural de doua cifre")
    x = int(input())
    s = x // 100
    z = x// 10
    u = x % 10
    print("Numarul rezultat ca urmare a adunarii cifrelor sutelor, zecilor si unitatilor este:", s + z +u)


def produs():
    print("Va rog sa introduceti un numar natural de trei cifre:")
    x = int(input())
    s = x // 100
    u = x % 10
    print("Produsul dintre cifra unitailor si cifra sutelor este:", u * s)


def numerecapetesipicioare():
   print("Va rog sa introduceti numarul de gaini:")
   G = int(input())
   print("Va rog sa intoduceti numarul de oi")
   O = int(input())
   capete = G + O
   picioare= 2 * G + 4 * O
   print("Numarul de capete este:", capete, "Numarul de picioare este:", picioare)


def cub():
    print("Va rog introduceti latura cubului:")
    l = int(input())
    aria = 6 * l * l
    volum = 3 * l
    print("Aria cubului este:" , aria, "Volumul cubului este:", volum)


def orasiminute():
    print("Va rog sa introduceti ora:")
    h = int(input())
    print("Va rog sa introduceti minutele:")
    m = int(input())
    print("Va rog sa introduceti minutele pe care doriti sa le adaugati orei initiale:")
    x = int(input())
    hn = h*60+m+x
    print("Ora finala va fi:", hn // 60, "minute:", hn % 60)


def numaranimale():
    print("Va rog sa introduceti numarul de capete:")
    c = int(input())
    print("Va rog sa introduceti numarul de picioare:")
    p = int(input())
    o = (p - 2+c) //2
    g = c - o
    print("Gaini:", g, "Oi:", o)


def eliminare():
    print("Va rog sa introduceti un numar natural de trei cifre:")
    n = int(input())
    m = (n // 100) * 10 + n % 10
    print("Numarul natural de trei cifre fara a doua zecimala este:", m)


def globuri():
    print("Va rog sa introduceti numarul de globuri albe:")
    a = int(input())
    r = 2 * a
    v = r - 3
    t = a + r + v
    print("Totalul de globuri din brad este:" , t)


def gauss():
    print("Va rog sa introduceti un numar natural:")
    n = int(input())
    s = (n*(n+1))//2
    print("suma lui Gauss este:", s)


def animale():
    print("Introduceti numarul de caini din curte:")
    c = int(input())
    p = 2 * c
    g = 2 * p
    t = c + p + g
    print("Numarul total de animale incluzand caini, pisici si gaini este:", t)


if __name__=="__main__":
    adunare2()
    adunare3()
    produs()
    numerecapetesipicioare()
    cub()
    orasiminute()
    numaranimale()
    eliminare()
    globuri()
    gauss()
    animale()