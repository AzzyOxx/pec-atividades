'''
5. Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, 
cujos elementos sejam a intercalação dos elementos de A e B.
'''

def recebe25():
    num = 25
    lista = []
    cont = 0
    print('Preencendo uma lista com 25 termos: ')
    while cont < num:
        n_paraInserir =int(input('Digite um número: '))
        #n_paraInserir = formataFloatCasas(n_paraInserir,1)
        lista.append(n_paraInserir)
        cont += 1
    return lista

def intercalacaoDe2Listas(listaA, listaB):
    num = 25
    cont = 0
    listaC = []
    while cont < num:        
        #n_paraInserir = formataFloatCasas(n_paraInserir,1)
        listaC.extend([listaA[cont]])
        listaC.extend([listaB[cont]])
        cont += 1
    return listaC

def main():
    #entrada
    print('Intercalação de listas: ')
    listaA = recebe25()
    listaB = recebe25()

    #processamento
    listaC = intercalacaoDe2Listas(listaA, listaB)
    #saída
    print(f'Lista de números da primeira lista: {listaA}\nLista de números da segunda lista: {listaB}\nIntercalação das duas listas anteriores: {listaC}')
    
if __name__ == '__main__':
    main()
