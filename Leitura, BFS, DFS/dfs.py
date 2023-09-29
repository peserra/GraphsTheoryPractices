def insere_aresta(grafo, origem, destino):
  grafo[origem].append(destino)

def busca_em_profundiade(grafo, visitado, vertice):
  if vertice not in visitado:
    visitado.add(vertice)
    descoberta[vertice] += 1
    for vizinho in grafo[vertice]:
      busca_em_profundiade(grafo, visitado, vizinho)
    
    finalização[vertice] += 1

n, m = (int(entrada) for entrada in input().split(" "))
grafo = [[]for _ in range(n)]

for _ in range(m):
  origem, destino = (int(aresta) for aresta in input().split(" "))
  insere_aresta(grafo, origem, destino)

visitado = set()
descoberta = [0] * n
finalização = [0] * n
busca_em_profundiade(grafo, visitado, 0)
print(descoberta)
print(finalização)

