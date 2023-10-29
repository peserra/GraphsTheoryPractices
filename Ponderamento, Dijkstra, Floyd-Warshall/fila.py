def verifica_vazia(fila) -> bool:
    if all(elementos == 0 for elementos in fila) and len(fila) > 0:
        return True
    return False

def insere_na_fila(fila, n):
    fila[n] = 1

def busca_elemento(fila, k):
    return fila[k]

# remove e devolve o indice de Q com a menor chave.
def extrai_minimo(fila, chaves):
    # encontra primeiro indice que eh 1 para inicializar o indice minimo
    for i in range(len(fila)):
        if fila[i] == 1:
            indice_minimo = i
            break
    
    # atualiza o indice do minimo caso ele realmente seja
    for i in range(len(fila)):
        if fila[i] == 1 and chaves[i] < chaves[indice_minimo]:
            indice_minimo = i
    
    fila[indice_minimo] = 0 # remove indice
    
    return indice_minimo 

# devolve o indice de Q com a menor chave (sem remover).
def verifica_minimo(fila, chaves):
     # encontra primeiro indice que eh 1 para inicializar o indice minimo
    for i in range(len(fila)):
        if fila[i] == 1:
            indice_minimo = i
            break
    
    # atualiza o indice do minimo caso ele realmente seja
    for i in range(len(fila)):
        if fila[i] == 1 and chaves[i] < chaves[indice_minimo]:
            indice_minimo = i
    
    
    return indice_minimo 

#main
tamanho, num_operacoes = (int(entrada) for entrada in input().split(" "))

fila = [0] * tamanho
# usado pra adicionar uma sequencia numa lista, separada por espaço
chaves = list(int(chave) for chave in input().split(" "))

operacao = ""

for _ in range(num_operacoes):
    comando = input()
    if len(comando) > 1:
        operacao, indice = comando.split(" ")
    else:
        operacao = comando

    if operacao == "I":
        insere_na_fila(fila, int(indice))
        print(fila)
    elif operacao == "M":
        indice_minimo = verifica_minimo(fila, chaves)
        print(f"{indice_minimo} {chaves[indice_minimo]} {fila}")
    elif operacao == "E":
        indice_minimo = extrai_minimo(fila, chaves)
        print(f"{indice_minimo} {chaves[indice_minimo]} {fila}")
    elif operacao == "B":
        resultado_busca = busca_elemento(fila, int(indice))
        print(f"{resultado_busca} {fila}")
    elif operacao == "V":
        print(f"{str(verifica_vazia(fila))} {fila}")
    else:
        print("Nenhum comando inserido")
        
    
    
    





