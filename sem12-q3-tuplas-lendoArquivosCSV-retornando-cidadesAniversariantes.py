'''
03. Leia um dia e um mês como números inteiros distintos e informe as cidades que fazem aniversário nessa data.
Veja o exemplo para o dia 9 e mês 2:
CIDADES QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO:
São Miguel do Passa Quatro(GO)
Centralina(MG)
Itaporanga(PB)
...
'''

#essa função ler um arquivo .csv
#função modelo
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

#essa função ler um arquivo .csv e retorna os dados solicitados
def cidades_aniversariantes(dia_ani, mes_ani):
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            if int(dia) == dia_ani and int(mes) == mes_ani:
                resultado.append(
                    #(uf, int(ibge), nome, int(dia), int(mes), int(pop))
                    (uf, nome)
                )
    arquivo.close()
    return resultado

def mes_literal(mes):
    lista_mes = [ 'JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
    return lista_mes[mes-1]
    
def main():
    '''
    cidades = carrega_cidades()
    print(cidades[:3] + cidades[-2:])
    print(cidades[1])
    print(cidades[:555])
    '''
    print(f'{"="*15}Cidades que fazem aniversário nessa data{"="*15}')
    #entrada de dados
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mês: '))

    #processamento
    cidades = cidades_aniversariantes(dia, mes)

    #saída
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes_literal(mes)}:')
    cont = len(cidades)
    i = 0
    while i < cont:
        print(f'{cidades[i][1]}({cidades[i][0]})')
        i += 1
    
    
if __name__ == '__main__':
    main()
