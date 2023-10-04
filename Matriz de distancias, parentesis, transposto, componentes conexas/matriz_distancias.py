def busca_em_largura(grafo, s):
  visitados = [0] * len(grafo)
  dist_para_s = [0] * len(grafo)
  visitados[s] = 1

  fila_busca = []
  fila_busca.append(s)
  distancia_acumulada = 0
  while len(fila_busca) > 0:
    u = fila_busca.pop(0) # primeiro vértice na fila
    for v in grafo[u]:
      if visitados[v] == 0:
        visitados[v] = 1
        dist_para_s[v] = dist_para_s[u] + 1
        fila_busca.append(v)
  return dist_para_s

def insere_aresta(grafo, origem, destino):
  grafo[origem].append(destino)

def imprime_matriz(matriz):
  linhas = ""
  for linha in range(len(matriz)):
    linhas += f"{linha}:{' '.join(map(str, matriz[linha]))}\n"
  print(linhas)

#Execução principal

n, m = (int(entrada) for entrada in input().split(" "))
grafo = [[]for _ in range(n)]

for _ in range(m):
  origem, destino = (int(aresta) for aresta in input().split(" "))
  insere_aresta(grafo, origem, destino)

matriz_distancias = []*n

for u in range(len(grafo)):
    matriz_distancias.append(busca_em_largura(grafo, u)) 

imprime_matriz(matriz_distancias)
  