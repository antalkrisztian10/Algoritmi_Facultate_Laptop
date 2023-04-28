def cautare(list, element):
    for i in range (len(list)):
        if list[i] == element:
            return i
        return -1

print(cautare([2,34,3,5,1,30,200],50))

def selectionsort(itemslist):
    n = len(itemslist)
    for i in range(n):
        minvalueindex = i

        for j in range(i + 1, n):
            if itemslist[j] < itemslist[minvalueindex]:
                minvalueindex = j

        if minvalueindex != i:
            temp = itemslist[i]
            itemslist[i] = itemslist[minvalueindex]
            itemslist[minvalueindex] = temp

    return itemslist

data = [9, 5, 1, 4, 3]
selectionsort(data)
print('Sorted Array in Ascending Order:')
print(data)

employee1 = {
    'id': 14,
    'name': 'John Doe',
    'age': 36,
    'position': 'Business Manager.'

}

def pozitie(angajat):
    return angajat['position']

print(pozitie(employee1))

employee2 = {
    'id': 2,
    'name': 'Jane Doe',
    'age': 20,
    'position': 'N/A'

}

employee3 = {
    'id': 110,
    'name': 'John Smith',
    'age': 40,
    'position': 'Software Developer.'

}

employee4 = {
    'id': 40,
    'name': 'Jane Smith',
    'age': 35,
    'position': 'Engineer.'

}

list1 = [employee1, employee2, employee3, employee4]

def cautareID(lista, id_cautat):
    for i in range(len(lista)):
        if lista[i]['id'] == id_cautat:
            return lista[i]
    return None

print(cautareID(list1, 40))