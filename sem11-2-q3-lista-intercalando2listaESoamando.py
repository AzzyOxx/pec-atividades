'''
3. Leia duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo 
tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.
'''
def recebe20():
    num = 20
    lista = []
    cont = 0
    print('Criando uma lista com 20 itens: ')
    while cont < num:
        n_paraInserir =int(input(f'{cont+1}º elemento: '))
        lista.append(n_paraInserir)
        cont += 1
    return lista

def intercalacaoSomaDe2Listas(listaA, listaB):
    num = 20
    cont = 0
    listaC = []
    while cont < num:
        itemToInsert = listaA[cont] + listaB[cont]
        listaC.append(itemToInsert)
        cont += 1
    return listaC

def main():
    #entrada
    listaA = recebe20()
    listaB = recebe20()
    
    #processamento
    listaC = intercalacaoSomaDe2Listas(listaA, listaB)

    #saída
    print(f'Itens da lista A: {listaA}')
    print(f'Itens da lista B: {listaB}')
    print(f'Lista da soma dos itens da lista A e lista B: {listaC}')
    
if __name__ == '__main__':
    main()
