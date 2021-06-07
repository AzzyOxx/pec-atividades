'''
4. Leia uma população e informe as cidades com população maior que o valor lido. Veja o exemplo:
Veja o exemplo para a leitura de 50000 para a população:
CIDADES COM MAIS DE 50000 HABITANTES:
IBGE: 120040 - Rio Branco(AC) - POPULAÇÃO: 290639
IBGE: 270030 - Arapiraca(AL) - POPULAÇÃO: 202398
IBGE: 270040 - Atalaia(AL) - POPULAÇÃO: 50323
'''

def cidades_mais_populosa(habitantes, mes_niver):
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            if int(pop) > habitantes and int(mes) == mes_niver: 
                resultado.append(
                    (uf, int(ibge), nome, int(dia), int(mes), int(pop))
                    #(uf, int(ibge), nome, int(pop))
                )
    arquivo.close()
    return resultado

def mes_literal(mes):
    lista_mes = [ 'JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
    return lista_mes[mes-1]
    
def main():
    print("Cidades que fazem aniversário no mês informado a seguir e com mais hapitantes que o informado a seguir: ")
    #entrada de dados
    mes = int(input('Mês de aniversário: '))
    populacao = int(input('População mínima: '))
        
    #processamento
    cidades_com_populacao_maior_mesAniver = cidades_mais_populosa(populacao, mes)

    #saída
    print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mes_literal(mes)}:')
    cont = len(cidades_com_populacao_maior_mesAniver)
    i = 0
    while i < cont:
        print(f'{cidades_com_populacao_maior_mesAniver[i][2]}({cidades_com_populacao_maior_mesAniver[i][0]}) tem {cidades_com_populacao_maior_mesAniver[i][5]} habitantes e faz aniversário em {cidades_com_populacao_maior_mesAniver[i][3]} de {mes_literal(mes).lower()}.')
        i += 1
    #print(cidades[:555])
    
if __name__ == '__main__':
    main()


