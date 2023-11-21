def insere_aresta(grafo, origem, destino):
    grafo[origem].append(destino)

def extrai_minimo(fila,chaves):
    indice_minimo = 0 

    # atualiza o indice do minimo caso ele realmente seja
    for i in range(len(fila)):
        if chaves[i] < chaves[indice_minimo]:
            indice_minimo = i
        
    return fila.pop(indice_minimo) # retorna o valor 

def Prim(grafo, matriz_pesos, raiz):
    infinito = 999

    chaves = [infinito] * len(grafo) # valor da distancia de cada vertice     
    pai = [-1] * n                  # vetor de quem precede quem  

    chaves[raiz] = 0
    fila = [i for i in range(len(grafo))] # vertices do grafo     
    
  
    while(len(fila) != 0): # roda ate nao ter mais vertice pra visitar
        u = extrai_minimo(fila, chaves) # vertice de G que possui menor distancia (raiz na primeira iteração) 
        for v in grafo[u]:
            if v in fila and matriz_pesos[u][v] < chaves[v]:
                chaves[v] = matriz_pesos[u][v]
                pai[v] = u
                
    
    print(chaves)
    print(pai)
      
     


# main
n, m, raiz = (int (entrada) for entrada in input().split(" ")) 

grafo = [[] for _ in range(n)]

matriz_pesos = [[0 for col in range(n)] for row in range(n)] 

for a in range(m):
    origem, destino, peso = (int (aresta) for aresta in input().split(" "))
    insere_aresta(grafo, origem, destino)
    matriz_pesos[origem][destino] = peso

Prim(grafo, matriz_pesos, raiz)




