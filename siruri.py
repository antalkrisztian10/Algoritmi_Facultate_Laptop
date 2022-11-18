def schimbare():
    print("Introduceti un cuvant:")
    cuvant = input().strip()
    index = 0
    for caracter in cuvant:
        if caracter in "aeiou":
            print(caracter.upper(), "am gasit vocala", index)
        else:
            print(caracter, index)
        index = index + 1


def prima_ultima_litera():
    print("Introduceti un cuvant:")
    cuvant = input().strip()
    cuvantn = ""
    index = 0
    for caracter in cuvant:
        if index==0 or index==len(cuvant)-1:
            cuvantn = cuvantn + caracter.upper()
        else:
            cuvantn = cuvantn + caracter
        index = index + 1
    print(cuvantn)


def sufix_prefix_adaug():
    print("Introduceti un cuvant:")
    sufix = "_"
    prefix = "#"
    cuvant = input().strip()
    cuvantn = prefix + cuvant + sufix
    print(cuvantn)


def sufix_prefix_extrag():
    print("Introduceti un cuvant:")
    nrsf = 2
    cuvant = input()
    print(cuvant[:nrsf], cuvant[len(cuvant)-nrsf:])


def asterix():
    print("Introduceti un cuvant:")
    cuvant = input().strip()
    cuvantn = ""
    for caracter in cuvant:
        if caracter in "aeiou":
            cuvantn = cuvantn + caracter + "*"
        else:
            cuvantn = cuvantn + caracter
    print(cuvantn)


def contror():
    print("Introduceti un cuvant:")
    cuvant = input().strip()
    contor = 0
    for caracter in cuvant:
        if caracter in "aA":
            contor += 1
    print(contor)


def lista():
    print("Lista realizata este:")
    l = [234, 100, 98, 300, 11, 2, 1, 5, 0]
    jumatate = len(l) // 2
    l1 = l[:jumatate:]
    l1.sort()
    print(l1)
    l2 = l[jumatate::]
    l2.append(4)
    l2.append(8)
    l2.sort(reverse=True)
    print(l2)
    l.pop()
    print(l)

if __name__ == "__main__":
    schimbare()
    prima_ultima_litera()
    sufix_prefix_adaug()
    sufix_prefix_extrag()
    asterix()
    contror()
    lista()