#inicialmente S é vazio
# primeira linha é o total de operações


# F - FindSet(S, x) devolve um representante de Sx
# M - MakeSet(S, x) cria um novo conjunto com um unico elemento x
# U - Union(S, x, y) une dois conjuntos Sx e Sy

def makeSet(set, element):
    subset = [element]
    set.append(subset)

def findSet(set, element):
    for subset in range(len(set)):
        for key in set[subset]:
            if key == element:
                return subset
            
def unionSet(set, elementA, elementB):
    i  = findSet(set, elementA)
    j = findSet(set, elementB)
    set[i]+=set[j]
    set[j].clear()



# main
n_operacoes = int(input())
s = [] #set

for _ in range(n_operacoes):
    comando = input()
    if len(comando) > 3:
        operacao, x, y = comando.split(" ")
    else:
        operacao, x = comando.split(" ")

    if operacao.upper() == "M":
        makeSet(set=s, element=x)
        print(s)
    elif operacao.upper() == "F":
        representante = findSet(set=s, element=x)
        print(f"{representante} {s}")
    elif operacao.upper() == "U":
        unionSet(set=s, elementA=x, elementB=y)
        print(s)
    else:
        print("Entrada incorreta.")