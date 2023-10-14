
def insere_aresta(grafo, origem, destino):
    grafo[origem].append(destino)

def busca_em_profundidade(grafo,u):
  global tempo
  global expressao
  expressao += f"({u} "
  visitado[u] = 1
  tempo += 1  

  for v in grafo[u]:
    if visitado[v] == 0:
      busca_em_profundidade(grafo, v)
  
  expressao+=f" {u})"
  tempo += 1
  finalizacao[u] = tempo


n, m = (int (entrada) for entrada in input().split(" "))
grafo = [[] for _ in range(n)] # lista de adjacência
grafo_transposto = [[] for _ in range (n)]
expressao = ""
#adiciona arestas nos grafos
for _ in range(m):
    origem, destino = (int (aresta) for aresta in input().split(" "))
    insere_aresta(grafo, origem, destino)
    insere_aresta(grafo_transposto, destino, origem)

visitado = [0] * n
finalizacao = {} # dicionario
tempo = 0

# executar dfs em G e guardar vertice:tempo em um dicionario
for u in range(len(grafo)):
    if visitado[u] == 0:
        busca_em_profundidade(grafo, u)

# ordenar vertices em ordem decrescente, transformar em dicionario
finalizacao_descendente = dict(sorted(finalizacao.items(), key = lambda x:x[1] ,reverse = True))

vertices_decrescente = list(finalizacao_descendente)

# executar dfs no grafo transposto, a partir da lista em ordem decrescente de vertices
visitado = [0] * n
expressao = ""
for v in range(len(vertices_decrescente)):
   # cada elemento da lista é o vertice no grafo transposto para executar a busca
   if visitado[vertices_decrescente[v]] == 0:
      busca_em_profundidade(grafo_transposto, vertices_decrescente[v]) 

print(expressao)


