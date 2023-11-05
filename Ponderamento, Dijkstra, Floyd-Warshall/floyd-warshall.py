def floyd_warshall(n, m, arestas):
    
    #vetor de caminhos minimos
    distancia = [[float('inf')] * n for _ in range(n)]
        
    pai = [[-1] * n for _ in range(n)]

    for i in range(n):
        distancia[i][i] = 0

    for u, v, w in arestas:
        distancia[u][v] = w
        pai[u][v] = u

    # Algoritmo
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancia[i][k] + distancia[k][j] < distancia[i][j]:
                    distancia[i][j] = distancia[i][k] + distancia[k][j]
                    pai[i][j] = pai[k][j]

   
    return distancia, pai

# main
n, m = map(int, input().split())
arestas = []
for _ in range(m):
    # vertice, vertice, custo
    u, v, w = map(int, input().split())
    arestas.append((u, v, w))

# Ira executar o floyd_warshall
distancia, pai = floyd_warshall(n, m, arestas)

#  imprime matriz de distancia
print("[",end = "")
for x in range (len(distancia)):
    if (x!= len(distancia)- 1):
        print(distancia[x])
    else:
        print( distancia[x], end= "]\n")

# imprime matriz de parentesco
print("[",end = "")
for x in range (len(pai)):
    if (x!= len(pai)- 1):
        print(pai[x])
    else:
        print( pai[x], end= "]")