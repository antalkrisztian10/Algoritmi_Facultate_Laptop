graph = [[0, 1], [0, 2],
         [1, 2], [1, 3],
         [2, 4], [2, 6],
         [4, 5], [4, 8],
         [5, 7]]

parcurs = []
lp = []

def parcurgere_graph(graph, start):
    if start not in lp:
        parcurs.append(start)
        for element in graph:
            if element[0] == start and start not in lp:
                lp.append(start)
                parcurgere_graph(graph, element[1])
parcurgere_graph(graph, 0)
print(parcurs)
print(lp)


cai = []
cale = []

def parcurgereit(graph, start):
    cale = []
    currentnode = start
    cale.append(currentnode)
    for element in graph:
        if element[0] == currentnode:
            currentnode = element[1]
            cale.append(currentnode)
    return cale

def toatecaile(graph):
    cai = []
    n = len(graph)
    i = 0
    while i < n:
        primelement = graph[0][0]
        cai.append(parcurgereit(graph, primelement))
        graph.pop(0)
        i = i + 1
    print(cai)


toatecaile(graph)