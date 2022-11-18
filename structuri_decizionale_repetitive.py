def fib():
    f1 = 0
    f2 = 1
    contor = 0
    while contor<10:
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        contor += 1
    print(f3)


# se da un sir de numere naturale, sa se calculeze numarul de aparitii ale cifrei 5
def sir5():
    print("Introduceti sirul de numere naturale")
    sir = input()
    contor = 0
    for index in range(0,len(sir),1):
        if sir[index]=="5":
            contor += 1
        print("Numarul de aparitii al cifrei 5 este:", contor)
# se da o lista de numere naturale, sa se calculeze numarul de aparitii ale cifrei 5
def lista5():
    print("Introduceti sirul de numere naturale despartit prin virgula")
    l = input().split(",")
    contor = 0
    for index in  range(len(l)):
        contor += 1
    print("Numarul de aparitii al cifrei 5 este:", contor)


# de realizat o functie care imi verifica apartenenta unui numar la un domeniu
# 0 --> 4000 - mic
# 4000 --> 800 - mediu
# 8000 --> - mare
def incadrare():
    print("Va rog sa introduceti un numar pentru care dorim incadrarea in domeniile date:")
    nr = int(input())
    if nr<4000:
        print("mic")
    else:
        if nr<8000:
            print("mediu")
        else:
            print("mare")
# de realizat o functie care creaza un meniu de forma
# Apasai 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire, 4 pentru imparire
def adunare():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a+b", a+b)


def scadere():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a-b", a - b)


def inmultire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a*b", a * b)


def impartire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a/b", a // b)


def meniu():
    print("Apasati 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire, 4 pentru imparitre, 5 pentru incadrare, 6 pentru sir5 , 7 pentru lista5")
    opt = input().strip()
    if opt == "1":
        print("adunare")
        adunare()
    else:
        if opt == "2":
            print("scadere")
            scadere()
        else:
            if opt == "3":
                print("inmultire")
                inmultire()
            else:
                if opt == "4":
                    print("imparire")
                    impartire()
                else:
                    if opt == "5":
                        print("incadrare")
                        incadrare()
                    else:
                        if opt == "6":
                            print("sir5")
                            sir5()
                        else:
                            if opt == "7":
                                print("lista5")
                                lista5()
                            else:
                                print("Optiunile disponibile sunt 1 2 3 4 5 6 7")


if __name__ == "__main__":
    exit_ = ""
    while exit_!="0":
        meniu()
        print("Pentru iesire inserai 0 sau orice alta tasta pentru continuare")
        exit_ = input().strip()