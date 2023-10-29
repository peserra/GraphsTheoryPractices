class VerticeDestino:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso # peso da aresta que conecta a origem ate esse vertice
    
    def __str__(self) -> str:
       return f"{self.nome}({self.peso})"

def insere_aresta(grafo, origem, destino, peso):
  vizinho = VerticeDestino(destino, peso)
  grafo[origem].append(vizinho)

def imprime_grafo(grafo):
  for n in range(len(grafo)):
    print(f"{n}:", end="")
    for v in grafo[n]: # imprime metodo __str__ de cada objeto na vizinhança de n
        print(f"{str(v)}", end = " ")
    print("")

def dijkstra(G, s):
   
   pred = [0] * len(G)      # guarda o predecessor do vertice indice
   dist = [10000] * len(G)  # guarda a distancia de s ate vertice indice
   visitado = [0] * len(G)  # guarda qual vertice ja foi visitado
   
   dist[s] = 0

   for u in range(len(G)):
      if visitado[u] == 0 and dist[u] != 10000:
         
   
    
# main
n, m, s = (int(entrada) for entrada in input().split(" "))

# grafo é uma lista, que para cada elemento (no) contém sua vizinhanca
grafo = [[] for _ in range(n)]

for _ in range(m):
    origem, destino, peso = (int (aresta) for aresta in input().split(" "))
    insere_aresta(grafo, origem, destino, peso)

