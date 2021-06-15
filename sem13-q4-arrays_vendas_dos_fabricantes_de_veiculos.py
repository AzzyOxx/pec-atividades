'''
04.A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em 
mil unidades.

Fabricante/Ano      2013    2014   2015     2016    2017    2018
Fiat                204     223    230      257     290     322
Ford                195     192    198      203     208     228
GM                  220     222    217      231     245     280
Wolkswagen          254     262    270      284     296     330

Faça um programa que:
a) leia os dados da tabela pelo teclado;
b) leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
c) determine e exiba o ano de maior volume geral de vendas.
d) determine e exiba a média anual de vendas de cada fabricante durante o período.
'''

def media_de_valor_por_linhaDaMatriz(matriz):
    medias = []
    soma = 0
    for linha in matriz:
        for coluna in linha:
            soma += coluna[2]
        medias.append(soma/len(matriz[0]))
        soma = 0
    return medias

#essa função deve somar os elementos por coluna e retornar qual acumula maior valor
def maior_valor_coluna_matriz(matriz):
    soma_por_coluna = 0
    maior = 0, 0
    ano = matriz[0][0][1]
    qntd_colunas = len(matriz[0])
    for colunas in range(qntd_colunas):
        for linha in matriz:
            #ano = linha[1]
            for elemento in linha:
                if elemento[1] == ano:
                    soma_por_coluna += elemento[2]
        if soma_por_coluna > maior[0]:
            maior = soma_por_coluna, ano
        ano += 1
        soma_por_coluna = 0
    return maior

def mais_vendido(matriz, ano):
    maior = (0, 0, 0)
    for linha in matriz:
        for elemento in linha:
            if elemento[1] == ano and elemento[2] > maior[2]:
                    maior = elemento
    return maior                    

def preenche_matriz( linhas , colunas):
    matriz = [] #lista vazia
    for fab in linhas:
        linha = [] # cada linha é uma lista (vetor)
        for ano in colunas:
            vendas = int(input(f'Vendas da {fab} no ano de {ano}: '))
            linha.append((fab, ano, vendas) )
        #insere a linha na matriz
        matriz.append(linha)
    return matriz

def main():
    #entrada de dados
    fabricantes = ('Fiat', 'Ford', 'GM', 'Wolkswagen')
    periodo = list(ano for ano in range(2013, 2019))
    vendas_dos_fabricantes = preenche_matriz(fabricantes, periodo)
    ano_fabricante_mais_vendeu = int(input('Ano que deseja consultar qual fabricante foi a campeã de vendas: '))
    
    #processamento
    campeao_de_vendas_ano = mais_vendido(vendas_dos_fabricantes, ano_fabricante_mais_vendeu)
    ano_mais_lucrativo = maior_valor_coluna_matriz(vendas_dos_fabricantes)
    media_de_vendas_2013_2018 = media_de_valor_por_linhaDaMatriz(vendas_dos_fabricantes)

    #saida    
    print(f'A fabricante que mais vendeu em {ano_fabricante_mais_vendeu} foi a {campeao_de_vendas_ano[0]} com {campeao_de_vendas_ano[2]} mil unidades.')
    print(f'O ano de maior volume geral de vendas foi {ano_mais_lucrativo[1]} com {ano_mais_lucrativo[0]} mil unidades.')
    print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')

    cont = 0
    for fab in fabricantes: 
        print(f'A {fab} vendeu em média {round(media_de_vendas_2013_2018[cont],2)} unidades por ano.')
        cont += 1
            
if __name__ == '__main__':
    ''' 
    testes
    '''
    main()
