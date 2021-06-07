'''
4. Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo:
Veja o exemplo para a leitura de 50000 para a população:
CIDADES COM MAIS DE 50000 HABITANTES:
IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639
IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398
IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323
'''

#essa função lê um arquivo CSV que contêm dados sobre cidades BR e retorna as cidades mais populosas que a informada na entrada
def cidades_mais_populosa(habitantes):
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            if int(pop) > habitantes: 
                resultado.append(
                    #(uf, int(ibge), nome, int(dia), int(mes), int(pop))
                    (uf, int(ibge), nome, int(pop))
                )
    arquivo.close()
    return resultado
    
def main():
    print('Cidades com população maior que o seguinte valor:')
    #entrada de dados
    populacao = int(input())
    
    #processamento
    cidades_com_populacao_maior = cidades_mais_populosa(populacao)

    #saída
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    cont = len(cidades_com_populacao_maior)
    i = 0
    while i < cont:
        print(f'IBGE: {cidades_com_populacao_maior[i][1]} - {cidades_com_populacao_maior[i][2]}({cidades_com_populacao_maior[i][0]}) - POPULAÇÃO: {cidades_com_populacao_maior[i][3]}')
        i += 1
        
if __name__ == '__main__':
    main()
