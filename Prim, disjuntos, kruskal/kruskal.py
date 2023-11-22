def insere_aresta(grafo, origem, destino):
    grafo[origem].append(destino)

def makeSet(set, element):
    subset = [element]
    set.append(subset)

def findSet(set, element):
    for subset in range(len(set)):
        for key in set[subset]:
            if key == element:
                return subset
            
def unionSet(set, elementA, elementB):
    i  = findSet(set, elementA)
    j = findSet(set, elementB)
    set[i]+=set[j]
    set[j].clear()

def Kruskal(grafo, pesos):
    t = []
    s = []
    for vertice in range(len(grafo)):
        makeSet(s, vertice)
    
    for aresta in pesos:
        u = aresta[0]
        v = aresta[1]
        if findSet(s,u) != findSet(s,v):
            unionSet(s, u, v)
            t.append([u, v,pesos[aresta]])
    
    return t



# main
n, m = (int (entrada) for entrada in input().split(" ")) 

grafo = [[] for _ in range(n)]

matriz_pesos = [[0 for col in range(n)] for row in range(n)] 

arestas_pesos = {}

# insere arestas na lista com seu peso
for a in range(m):
    origem, destino, peso = (int (aresta) for aresta in input().split(" "))
    insere_aresta(grafo, origem, destino)
    arestas_pesos[(origem, destino)] = peso

arestas_pesos = dict(sorted(arestas_pesos.items(), key = lambda item: item[1]))


mst = Kruskal(grafo, arestas_pesos)
print(mst)




