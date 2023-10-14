def insere_aresta(grafo, origem, destino):
    grafo[origem].append(destino)

def imprime_grafo(grafo):
  for n in range(len(grafo)):
    print(f"{n}:{' '.join(map(str,grafo[n]))}")


def main():
    n, m = (int(entrada) for entrada in input().split(" "))
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        origem, destino = (int(aresta) for aresta in input().split(" "))
        # um grafo transposto inverte origem e destino
        insere_aresta(grafo, destino, origem) 

    imprime_grafo(grafo)




if __name__ == "__main__":
    main()