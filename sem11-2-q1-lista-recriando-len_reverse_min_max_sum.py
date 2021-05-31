'''
1. As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as 
estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
a) len(), que recebe uma lista e retorna número de itens;
b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
c) min(),que recebe uma lista e retorna o menor valor
d) max(), que recebe uma lista retorna o maior valor
e) sum(), que recebe uma lista retorna a soma dos valores
Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a 
leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o 
resultado encontrado.
Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(), 
minimo(), maximo(), soma().
'''

def criaLista():
    lista = []
    print(f'{"="*4}Criando uma lista: {"="*4}')
    while True:
        n = int(input('Adicione(press 0 to stop): '))
        #n = int(input())
        if n == 0:
            break        
        lista.append(n)
        
    return lista

def comprimento(lista):
    tem = True
    cont = 0
    i = 0
    while True:
        try:
            if lista[i] != '':
                cont += 1
            i += 1
        except:
            break
    return cont

def inverter(lista):
    tamanho = comprimento(lista)
    lista_invertida = []
    i = 0
    while i < tamanho:
        lista_invertida.insert(0,lista[i])
        i += 1
        
    return lista_invertida  

def minimo(lista):
    tamanho = comprimento(lista)
    i = 1
    minimo = lista[0]
    while i < tamanho:
        if lista[i] < minimo:
            minimo = lista[i]
        i += 1
    return minimo

def maximo(lista):
    tamanho = comprimento(lista)
    i = 1
    maximo = lista[0]
    while i < tamanho:
        if lista[i] > maximo:
            maximo = lista[i]
        i += 1
    return maximo

def soma(lista):
    tamanho = comprimento(lista)
    i = 0
    soma = 0
    while i < tamanho:
        soma += int(lista[i])
        i += 1
    return soma
    
def main():
    #entrada
    lista1 = criaLista()
    #lista2 = criaLista()
    #lista3 = criaLista()
    #lista4 = criaLista()
    #lista5 = criaLista()
    
    #processamento
    comprimento_lista1 = comprimento(lista1)    
    lista2_invertida = inverter(lista1)
    
    try:
        minimo_lista3 = minimo(lista1)
    except:
        minimo_lista3 = 0
    
    try:
        maior_lista4 = maximo(lista1)
    except:
        maior_lista4 = 0
    
    soma_itens_lista= soma(lista1)

    
    #saída
    '''{
    print(f'Primeira lista: {lista1}')
    print(f'Quantidade de itens da primeira lista: {comprimento_lista1}')
    print(f'Segunda lista: {lista2}')
    print(f'Segunda lista invertida: {lista2_invertida}')
    print(f'Terceira lista: {lista3}')
    print(f'Menor item da terceira lista: {minimo_lista3}')
    print(f'Quarta lista: {lista4}')
    print(f'Maior item da quarta lista: {maior_lista4}')
    print(f'Quinta lista: {lista5}')
    print(f'Soma dos itens da quinta lista: {soma_itens_lista}')
    }'''

    print(f'Itens inseridos na lista: {lista1}')
    print(f'Número de itens existentes na lista: {comprimento_lista1}')
    print(f'Lista com a ordem dos itens invertida: {lista2_invertida}')
    print(f'Menor item existente na lista: {minimo_lista3}')
    print(f'Maior item existente na lista: {maior_lista4}')
    print(f'Valor correspondente a soma de todos os itens dessa lista: {soma_itens_lista}')
    
if __name__ == '__main__':
    main()
