'''
03.Fazer um programa para ler uma matriz n x m de números inteiros. Os valores de n e m são inteiros, positivos e 
devem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente:
a) a soma dos elementos da primeira linha
b) a soma dos elementos da última coluna
c) a média de todos os elementos
d) o menor elemento
e) o maior elemento
'''

def maiorEmenor_matriz(matriz):
    maior = menor = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
            if elemento < menor:
                menor = elemento
    return maior, menor

def media_dos_elementos_matriz(matriz, total): #total = len(matriz)*len(matriz[0])
    soma = 0
    for linha in matriz:
        soma += soma_lista(linha)
    return soma / total

def pega_coluna_matriz(matriz, coluna):
    matriz_colunaX = []
    for linha in matriz:
        matriz_colunaX.append(linha[coluna-1])
    return matriz_colunaX

def soma_lista(lista):
    soma = 0
    for cont in lista:
        soma += cont
    return soma

def preenche_matriz(linhas, colunas):
    matriz = [] #lista vazia
    for lin in range(linhas):
        linha = [] # cada linha é uma lista (vetor)
        for col in range(colunas):
            n = int(input('Insira um número inteiro: '))
            linha.append(n)
        #insere a linha na matriz
        matriz.append(linha)
    return matriz

def main():
    #entrada de dados
    n = int(input('Quantidades de linhas: '))
    m = int(input('Quantidades de colunas'))
    matrizNxM = preenche_matriz( n, m )
    
    #processamento
    somaPrimeiraLinha = soma_lista(matrizNxM[0])
    lista_dos_elementos_ultima_coluna = pega_coluna_matriz(matrizNxM, m)
    somaUltimaColuna = soma_lista(lista_dos_elementos_ultima_coluna)
    media_dos_elementosMatriz = media_dos_elementos_matriz(matrizNxM, m*n)
    maior_elemento_matriz, menor_elemento_matriz = maiorEmenor_matriz(matrizNxM)
    tupla_com_as_informacoes = (somaPrimeiraLinha, somaUltimaColuna, round(media_dos_elementosMatriz, 4), menor_elemento_matriz, maior_elemento_matriz,)
    
    #saída
    print(tupla_com_as_informacoes)
        
if __name__ == '__main__':
    main()
