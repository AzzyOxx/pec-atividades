'''
05.Faça um programa que leia e armazene em um array tridimensional contendo os valores do faturamento anual de 
uma empresa, especificados por filial e também mês a mês. Veja a estrutura do array seguinte:
Após a leitura dos dados faça o seguinte:
a) Calcule o total de cada ano por filial;
b) Calcule o total de todas as filiais por ano;
c) Calcule o total do período para todas as 
filiais;
d) Mostre todos os dados lidos e calculados
de acordo com o período que ocorrer, 
por exemplo:

2014;Filial 1;Janeiro;210
...
2014;Filial 1;Dezembro;463
TOTAL 2014 FILIAL 1;3526
2014;Filial 2;Janeiro;430
...
2014;Filial 3;Dezembro;310
TOTAL 2014 FILIAL 3;3346
TOTAL 2014 TODAS FILIAIS;10727
2015;Filial 1;Janeiro;316
...
2017;Filial 3;Dezembro;354
TOTAL 2017 FILIAL 3;3550
TOTAL 2017 TODAS FILIAIS;11123
TOTAL PERIODO TODAS FILIAIS;42855

'''

def soma_todo_faturamento_filial(matriz, filiais): # -->> c) Calcule o total do período para todas as filiais;
    i_filial = -1
    i_ano = -1
    valor_periodo_filial = []
    for filial in filiais:
        i_filial += 1
        soma = 0
        for ano in matriz:#linha
            soma += ano[i_filial]
        valor_periodo_filial.append(soma)

    return valor_periodo_filial

def faturamento_por_ano(matriz_tri): # -->> b) Calcule o total de todas as filiais por ano; 
    matriz_linha_faturamento_ano = []
    for ano in matriz_tri:
        matriz_linha_faturamento_ano.append(sum(ano))
    return matriz_linha_faturamento_ano

def faturamento_ano_filial(matriz_tri):#, filiais, anos, meses / -->> a) Calcule o total de cada ano por filial;
    matriz_tridimensional = []
    for  ano in matriz_tri:#cada 'ano' vai pegar uma bidimensional
        matriz_linha_coluna_faturamento_ano = []
        for filial in ano:#cada filial representa uma linha dentro da matriz 'ano'            
            faturamento_filial_ano = 0
            for mes in filial:
                faturamento_filial_ano += mes[3]
            matriz_linha_coluna_faturamento_ano.append(faturamento_filial_ano)            
        matriz_tridimensional.append(matriz_linha_coluna_faturamento_ano)    
    return matriz_tridimensional

def preenche_matriz( matrizes_bi, linhas , elementos):
    matriz_tridimencional = [] #matriz_tri[matriz_bi[linhas[]]] (matriz tridimensional)
    for ano in matrizes_bi:
        matriz_bidimencional = [] # matriz_bi[linhas[]] (matriz bidimensional)
        for filial in linhas:
            linha = []         #linha[] (linhas da matriz)
            for mes in elementos:
                #faturamento_mes = int(input())
                faturamento_mes = int(input(f'Insira as vendas da {filial} no mês de {mes} do ano de {ano}: '))
                #insere o elemento na linha
                linha.append((ano, filial, mes, faturamento_mes))
            #insere a linha na matriz bidimensional
            matriz_bidimencional.append(linha)
        #insere a matriz bidimensional na matriz tridimensional
        matriz_tridimencional.append(matriz_bidimencional)
    return matriz_tridimencional

def main():
    #entrada de dados
    filiais = ('Filial 1', 'Filial 2', 'Filial 3')
    lista_meses = ( 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    periodo = list(ano for ano in range(2014, 2018))

    #processamento das informações
    faturamento_anual = preenche_matriz(periodo, filiais, lista_meses)
    faturamento_por_ano_filial = faturamento_ano_filial(faturamento_anual)#, filiais, periodo, lista_meses
    faturamento_total_por_ano = faturamento_por_ano(faturamento_por_ano_filial)
    faturamento_total_do_periodo_por_filial = soma_todo_faturamento_filial(faturamento_por_ano_filial, filiais)

    #saída    
    i_ano = -1
    for ano in faturamento_anual:
        i_ano += 1
        i_filial = -1
        for filial in ano:
            i_filial += 1
            i_mes = -1
            for mes in filial:
                i_mes += 1
                print(f'{filial[i_mes][0]};{filial[i_mes][1]};{filial[i_mes][2]};{filial[i_mes][3]}')
            
            print(f'TOTAL {filial[i_mes][0]} {filial[i_mes][1].upper()}; {faturamento_por_ano_filial[i_ano][i_filial]}' )
        print(f'TOTAL {filial[i_mes][0]} TODAS FILIAIS;{faturamento_total_por_ano[i_ano]}')
    print(f'TOTAL PERÍODO TODAS FILIAIS;{sum(faturamento_total_do_periodo_por_filial)}')
        
if __name__ == '__main__':
    ''' 
    testes
    '''
    main()
