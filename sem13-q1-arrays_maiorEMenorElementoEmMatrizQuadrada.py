'''
01.Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do 
maior e menor elemento. O valore de n é inteiro, positivo e deve ser informados pelo usuário
'''

def preenche_matriz(linhas, colunas):
    matriz = [] #lista vazia
    for lin in range(linhas):
        linha = [] # cada linha é uma lista (vetor)
        for col in range(colunas):
            n = int(input('Inserir número inteiro: '))
            linha.append(n)
        # insere a linha na matriz
        matriz.append(linha)
    return matriz

'''
def imprime_matriz(matriz):     
    for linha in matriz:        
        print('|', end = '')    
        for elemento in linha:
            print(f'{elemento:3d}', end = ' ') 
        print('|')

-- ou --

def imprime_matriz_indice(matriz):
    for i_linha in range(len(matriz)):
        print('|', end = '')
        for i_coluna in range(len(matriz[i_linha])):
            print(f'{matriz[i_linha][i_coluna]:3d}', end = ' ')
        print('|')
'''

def imprime_maiorOUmenor_matriz(matriz):
    maior = menor = matriz[0][0], 1, 1
    line = col = 1
    for linha in matriz:
        col = 1
        for elemento in linha:            
            if elemento > maior[0]:
                maior = elemento, line, col 
            if elemento < menor[0]:
                menor = elemento, line, col
            col += 1
        line += 1
    maior = maior[1] , maior[2] 
    menor = menor[1] , menor[2]
    '''
    maior = maior[1] -1, maior[2] -1
    menor = menor[1] -1, menor[2] -1
    '''
    return maior, menor
    
def main():
    #entrada de dados
    ordemDaMAtriz = int(input('Ordem da matriz quadrada: '))

    #processamento
    matriz = preenche_matriz( ordemDaMAtriz, ordemDaMAtriz )
    maiorEmenor = imprime_maiorOUmenor_matriz(matriz)

    #saída
    print('Posição do maior número inserido: ',maiorEmenor[0])
    print('Posição do menor número inserido: ',maiorEmenor[1])
    
if __name__ == '__main__':
    main()

