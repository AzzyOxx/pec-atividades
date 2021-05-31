'''
2. Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe 
uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo 
count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2 
aparece na lista.
Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois 
o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.
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

def contem(lista, valor_pesquisa):
    tamanho = comprimento(lista)
    i = 0
    tem = 0
    while i < tamanho:
        if valor_pesquisa == lista[i]:
            tem += 1
        i += 1
    return tem
            
def main():
    #entrada
    lista = criaLista()
    valor_pesquisa = int(input('Digite um número para ser pesquisado na lista: '))

    #processamento
    tem_na_lista = contem(lista, valor_pesquisa)

    #saída
    print(f'Lista criada: {lista}')
    print(f'Valor para ser pesquisado: {valor_pesquisa}')
    print(f'Número de vezes que o item aparece nessa lista: {tem_na_lista}')
    
if __name__ == '__main__':
    main()
