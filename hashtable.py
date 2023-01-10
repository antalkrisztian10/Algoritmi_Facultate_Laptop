def parcurgere_lista():
    l = list()
    for i in range(len(l)):
        print(l[i])
    for element in l:
        print(element)

# fiecare litera a alfabetului primeste o valoare (key-value) exe: a=200 b=300 c=1
# sa se calculeze pentru un cuvant valoarea generata prin adunarea valorilor fiecarei litere exe:abc=501

def suma_cuvant(cuvant):
    ht = {"a": 200 , "b": 300 , "c": 1, "d": 40, "e": 50, "f": 60, "g": 70, "h": 80, "i": 90, "j": 1,
           "k": 2, "l": 3, "m": 4, "n": 5, "o": 6, "p": 7, "q": 8, "r": 9, "s": 10, "t": 11, "u": 12,
          "v": 13, "w": 14, "x": 15, "y": 16, "z": 17}
    suma = 0
    for element in cuvant:
        suma += ht[element]
    return suma

# se da o lista de nume de exemplu: ['ion' , 'vasile' , 'gheorghe' , 'ioana' , 'maria' , 'ana']
# sa se determine care numa din aceasta lista genereaza valoarea cea mai mare (conform problemei anterioare)
# si sa se afiseze acel nume


def adunare_nume(lista):
    max = 0
    maxN = ''
    for element in lista:
        vc = suma_cuvant(element)
        if vc > max:
            max = vc
            maxN = element
    return maxN


def generare_ht(tip=0):
    ht = {}
    litere = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    listanoua = []
    start = 7
    for i in range(start, len(litere)):
        listanoua.append(litere[i])
    for i in range(0, start):
        listanoua.append(litere[i])
    for i in range(len(litere)):
        if tip==0:
            ht[litere[i]] = listanoua[i]
        else:
            ht[litere[i]] = litere[i]
    return ht


def crypt_text(propozitie, tip=0):
    litere = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ht = generare_ht(tip)
    text = ''
    for element in propozitie:
        if element in litere:
            text += ht[element]
        else:
            text += element
    return text


if __name__=="__main__":
    # print(suma_cuvant("blabla"))
    # print(adunare_nume(['ion' , 'vasile' , 'gheorghe' , 'ioana' , 'maria' , 'ana']))
    # print(generare_ht())
    prop = input("Propozitie:")
    c = crypt_text(prop)
    print(c)
    d = crypt_text(c,1)
    print(d)



