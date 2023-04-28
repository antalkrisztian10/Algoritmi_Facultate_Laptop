def cautare(lista,numar):
    for i in range(len(lista)):
        if lista[i] == numar:
            return i
    return -1


def generare_CNP(gen, an, luna, zi, judet, NNN):
    CNP = ""
    if gen  == "M" or gen == "m" or gen == "masculin":
        if an < 2000:
            CNP += "1"
        else:
            CNP += "5"
    else:
        if an < 2000:
            CNP += "2"
        else:
            CNP += "6"
    if an < 2000:
        an = an - 1900
    else:
        an = an - 2000
    if an < 10:
        CNP += "0"
    CNP += str(an)
    if luna < 10:
        CNP += "0"
    CNP += str(luna)
    if zi < 10:
        CNP += "0"
    CNP += str(zi)
    if judet < 10:
        CNP += "0"
    CNP += str(judet)
    if NNN < 10:
        CNP += "00"
    elif NNN < 100:
        CNP += "0"
    else:
        CNP += ""
    CNP += str(NNN)
    CNP += str(generareC(CNP))
    return CNP


def generareC(sir):
    sirControl = "279146358279"
    suma = 0
    for i in range(len(sir)):
        suma += int(sir[i]) * int(sirControl[i])
    if suma % 11 == 10:
        return  1
    else:
        return suma % 11


if __name__=="__main__":
    print(cautare([2,3,4,6,6,3,2],4))
    print(generare_CNP("m", 1980, 1, 1, 24, 1))