sg = 0
l1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
l2 = ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"]

def adunareelementelista(lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    return s


def adunare(*argumente):
    s = 0
    for element in argumente:
        s += element
    return s


def produs(*args):
    p = 1
    for element in args:
        p *= element
    return p


def adunarecumetoda(*args):
    global sg
    for e in args:
        sg += 0


def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f


def cautare(listadecaractere,caracter):  # functia reintoarce un index
    for i in range(len(listadecaractere)):
            if listadecaractere[i] == caracter:
                return i
    return 0


def crypt(plaintext):  # reintoarce textul final
    text = ""
    for e in plaintext:
        i = cautare(l1,e)
        if e not in ("","1","2","3","4","5","6"):
            text += l2[i]
        else:
            text += 0
    return text


def decrypt(text):  # reintoarce textul final
    plaintext = ""
    for e in text:
        i = cautare(l2,e)
        if e not in ("","1","2","3","4","5","6"):
            plaintext += l1[i]
        else:
            plaintext += 0
    return plaintext


if __name__ =="__main__":
    text = "hello world"
    ctext = crypt(text)
    print(ctext)