def insere_aresta(grafo, origem, destino):
  grafo[origem].append(destino)

def imprime_grafo(grafo):
  for n in range(len(grafo)):
    print(f"{n}:{grafo[n]}")

n, m = (int(entrada) for entrada in input().split(" "))
grafo = [[]for _ in range(n)]

for _ in range(m):
  origem, destino = (int(aresta) for aresta in input().split(" "))
  insere_aresta(grafo, origem, destino)

imprime_grafo(grafo)