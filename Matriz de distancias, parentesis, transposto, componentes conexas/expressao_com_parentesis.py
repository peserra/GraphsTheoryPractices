def insere_aresta(grafo, origem, destino):
  grafo[origem].append(destino)

def busca_em_profundidade(grafo,u):
  global expressao
  visitado[u] = 1
  expressao += f"({u} "

  for v in grafo[u]:
    if visitado[v] == 0:
      busca_em_profundidade(grafo, v)
  expressao+=f" {u})"
     
      

# Execução principal
n, m = (int(entrada) for entrada in input().split(" "))
grafo = [[]for _ in range(n)]

for _ in range(m):
  origem, destino = (int(aresta) for aresta in input().split(" "))
  insere_aresta(grafo, origem, destino)

visitado = [0] * n

expressao = ""

for u in range(len(grafo)):
    if visitado[u] == 0:
      busca_em_profundidade(grafo, u)

print(expressao)
