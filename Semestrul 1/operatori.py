def suma():


    print("SUMA")

    print("\nIntroduceti a")
    a = input()
    print("S-a introdus primul nr., adica a= ", a)

    print("\nIntroduceti b")
    b = input()
    print("S-a introdus al 2-lea nr., adica b=", b)

    print("\nadunarea a+b = ", int(a) + int(b))


def scadere():

    print("\nSCADERE")

    print("\nIntroduceti a")
    a = input()
    print("S-a introdus primul nr., adica a= ", a)

    print("\nIntroduceti b")
    b = input()
    print("S-a introdus al 2-lea nr., adica b=", b)

    print("\nscaderea a-b = ", int(a) - int(b))


def produs():


    print("\nPRODUS")

    print("\nIntroduceti a")
    a = input()
    print("S-a introdus primul nr., adica a= ", a)

    print("\nIntroduceti b")
    b = input()
    print("S-a introdus al 2-lea nr., adica b=", b)

    print("\nprodusul a*b = ", int(a) * int(b))


def impartire():


    print("\nIMPARTIRE")

    print("\nIntroduceti a")
    a = input()
    print("S-a introdus primul nr., adica a= ", a)

    print("\nIntroduceti b")
    b = input()
    print("S-a introdus al 2-lea nr., adica b=", b)

    print("\nimpartire a//b = ", int(a) // int(b))


def arie():
    print("\nARIA TRIUNGHIULUI")

    print("\nintroduceti cateta 1")
    a = input()
    print("S-a introdus cateta 1, adica c1= ", a)
    print("\nIntroduceti cateta 2")
    b = input()
    print("S-a introdus cateta 2, adica c2= ", b)
    print("\nAria triunghiului c1*c2/2 = ", (int(a) * int(b)) // 2)


def arie_dreptunghi():


    print("\nARIA DREPTUNGHIULUI")

    print("\nIntroduceti l")
    l = input()
    print("S-a introdus lungimea, adica l= ", l)

    print("\nIntroduceti L")
    L = input()
    print("S-a introdus latimea, adica L=", L)

    print("\nAria dreptunghiului l*L = ", int(l) * int(L))


def perimetru():


    print("\nPERIMETRUL TRIUNGHIULUI")

    print("\nIntroduceti a")
    a = input()
    print("S-a introdus latura 1, adica a= ", a)

    print("\nIntroduceti b")
    b = input()
    print("S-a introdus latura 2, adica b=", b)

    print("\nIntroduceti c")
    c = input()
    print("S-a introdus latura 3, adica c=", c)

    print("\nPerimetrul triunghiului = ", int(a) + int(b) + int(c))


if __name__ == '__main__':
    suma()
    scadere()
    produs()
    impartire()
    arie()
    arie_dreptunghi()
    perimetru()