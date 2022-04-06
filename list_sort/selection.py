#SELECTION Sort (ORDENAÇÃO POR SELEÇÃO)

#Iteração 1: percorre toda a lista, procurando o menor valor para ocupar a posição 0.
#Iteração 2: a partir da posição 1, percorre toda a lista, procurando o menor valor para ocupar a posição 1.
#Iteração 3: a partir da posição 2, percorre toda a lista, procurando o menor valor para ocupar a posição 2.
#Esse processo é repetido N-1 vezes, sendo N o tamanho da lista.
lista = [10, 9, 5, 8, 11, -1, 3]

import sys
def executar_selection_sort(selection):
    n = len(selection) #guarda tamanho da lista
    print("Elementos:", n)
    for i in range(0, n): #i para controlar a posição de inserção
        index_menor = i 
        ciclo = i + 1 #aqui é só para verificar visualmente as iterações
        for j in range(i+1, n): #j para iterar sobre os valores da lista, procurando o menor valor
            if selection[j] < selection[index_menor]:
                index_menor = j #quando o menor valor for encontrado, index_menor guardará a posição para a troca dos valores
        #usamos a seguinte atribuição múltipla para fazer a troca dos valores, quando necessário:
        selection[i], selection[index_menor] = selection[index_menor], selection[i]
        print(f"Iteração {ciclo} do sort:", selection) #para acompanhar visualmente cada iteração
    return selection