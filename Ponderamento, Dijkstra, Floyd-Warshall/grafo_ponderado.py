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
    
n, m = (int(entrada) for entrada in input().split(" "))

# grafo é uma lista, que para cada elemento (no) contém sua vizinhanca
grafo = [[] for _ in range(n)]

for _ in range(m):
    origem, destino, peso = (int (aresta) for aresta in input().split(" "))
    insere_aresta(grafo, origem, destino, peso)

imprime_grafo(grafo)
