import heapq

def muda_prioridade_heap(vertice, fila):
    for i in range(len(fila)):
        if fila[i][1] == vertice:
            indice = i
            break
    fila[indice] = (L[vertice], vertice)
    heapq._siftdown(fila, 0, indice)
    return

def init_custos(n):
    custos = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(0)
            else:
                linha.append(infinito)
        custos.append(linha)
    return custos


# main
n, m, s = (int(entrada) for entrada in input().split(" "))

grafo = [[] for _ in range(n)]
infinito = 99999
vetor_custos = init_custos(n) # 0 no proprio vertice, infinito nos outros

# cria arestas do grafo e adiciona custo à matriz
for i in range(m):
    origem, destino, custo = (int(aresta) for aresta in input().split(" "))
    grafo[origem].append(destino)
    vetor_custos[origem][destino] = custo

# valores iniciais
visitado = n * [0]
L = n*[infinito]
raiz = s
L[raiz] = 0
D = [(0, raiz)]
for i in range(0, n):
    if i != raiz:
        heapq.heappush(D, (L[i], i))

pai = n*[-1] # define valor inicial do pai de cada vertice

# Dijkstra
while D != []:
    Lmin, v = heapq.heappop(D)
    visitado[v] = 1
    for vertice in grafo[v]:
        if visitado[vertice] == 0:
            if L[v] + vetor_custos[v][vertice] < L[vertice]:
                L[vertice] = L[v] + vetor_custos[v][vertice]
                muda_prioridade_heap(vertice, D)
                pai[vertice] = v
print(L)
print(pai)

