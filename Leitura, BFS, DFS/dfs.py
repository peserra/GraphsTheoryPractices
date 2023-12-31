def insere_aresta(grafo, origem, destino):
  grafo[origem].append(destino)

def busca_em_profundidade(grafo,u):
  global tempo
  visitado[u] = 1
  tempo += 1
  tempo_descoberta[u] = tempo

  for v in grafo[u]:
    if visitado[v] == 0:
      busca_em_profundidade(grafo, v)
  
  tempo += 1
  tempo_finalização[u] = tempo

# Execução principal
n, m = (int(entrada) for entrada in input().split(" "))
grafo = [[]for _ in range(n)]

for _ in range(m):
  origem, destino = (int(aresta) for aresta in input().split(" "))
  insere_aresta(grafo, origem, destino)

visitado = [0] * n
tempo_descoberta = [0] * n
tempo_finalização = [0] * n
tempo = 0

for u in range(len(grafo)):
    if visitado[u] == 0:
      busca_em_profundidade(grafo, u)

print(tempo_descoberta)
print(tempo_finalização)