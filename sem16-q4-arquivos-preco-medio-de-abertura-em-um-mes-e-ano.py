'''
A imagem, abaixo, mostra um trecho de arquivo csv (Comma-separated values) com informações acerca de empresas 
que negociam ações na bolsa de valores de São Paulo:

timestamp,open,high,low,close,volume
2020-10-09,13.6400,13.9300,13.5400,13.5700,24150400
2020-10-08,13.6100,13.7800,13.4300,13.6800,42956600
2020-10-07,13.4300,13.8600,13.4000,13.5300,36713000
2020-10-06,12.9300,13.7000,12.8900,13.3400,55057200
2020-10-05,12.5600,12.8400,12.5400,12.8100,17205900
2020-10-02,12.6100,12.8300,12.5300,12.5300,18790500
2020-10-01,12.5500,12.7800,12.4800,12.7000,20801000
2020-09-30,12.4500,12.6800,12.3600,12.5400,23701700
2020-09-29,12.4600,12.6900,12.2800,12.3500,25093301
2020-09-28,12.9700,12.9700,12.4200,12.4800,37529699
2020-09-25,12.6500,12.9100,12.5000,12.8400,26282600
2020-09-24,12.5000,12.8300,12.3600,12.6700,30795400
2020-09-23,12.6800,12.7600,12.4400,12.4400,27644500
2020-09-22,12.7200,12.8800,12.5700,12.8000,13561500
2020-09-21,12.7000,12.8000,12.5100,12.7300,18931400
2020-09-18,13.1100,13.1700,12.7900,12.7900,46635300
2020-09-17,12.5200,13.2600,12.4000,13.1600,58315300
[...]

fonte: https://www.alphavantage.co/

As colunas, separadas por vírgula, representam:
timestamp: data do pregão em formato americano (aaaa-mm-dd);
open: valor da ação no momento da abertura dos negócios na data;
high: maior valor atingido pela ação durante o pregão;
low: menor valor atingido pela ação durante o pregão;
close: valor da ação no momento de fechamento dos negócios na data.
volume: quantidade de negociações com as ações da empresa na data do pregão.
Leia o nome de um arquivo csv com dados de uma empresa, conforme o apresentado, faça o carregamento das 
informações e responda:
1. Qual o maior preço de abertura e a data que correu?
2. Qual o menor preço de fechamento e a data que correu?
3. Qual o volume médio de negociações em um mês e ano informados?
4. Qual o preço médio de abertura em um mês e ano informados?
5. Em quais dias de um mês e ano lidos houve queda no preço da ação? Qual o preço de abertura e o preço do 
fechamento na data e a variação do preço em moeda corrente? Observação: há queda no preço quando o 
valor de abertura é maior que o de fechamento.
'''
'''
from operator import itemgetter


def formatar_data(data):
    meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    d, m, a = data['dia'], data['mes'], data['ano']

    return f'{d:0>2d} de {meses[m - 1]} de {a}'
'''

def media_abertura(dados, mes_d, ano_d):
    volume_periodo = 0
    pregoes = 0
    for preg in dados:
        if preg['mes'] == mes_d and preg['ano'] == ano_d:
            volume_periodo += preg['abertura']
            pregoes += 1
    return volume_periodo / pregoes

    
def carrega(arquivo):
    linhas = []
    with open(arquivo) as d:
        d.readline() #descarta a primeira linha(cabeçalho do arquivo)
        for linha in d.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes,dia = data.split('-')
            linhas.append(
                {
                    'ano' : int(ano),
                    'mes' : int(mes),
                    'dia' : int(dia),
                    'abertura' : float(abertura),
                    'alta' : float(alta),
                    'baixa' : float(baixa),
                    'fechamento' : float(fechamento),
                    'volume' : int(volume)
                    }
                )
        return linhas
        

def main():
    #entrada
    arquivo = input('Nome do arquivo(ex: olamundo.py): ').strip()
    mes_choice = int(input('mês(ex: 2): '))
    ano_choice = int(input('ano: '))

    #processamento
    #carrega os dados do precão a partir do arquivo csv
    pregao = carrega(arquivo)

    #4. Qual o preço médio de abertura em um mês e ano informados?
    preco_medio_abertura = media_abertura(pregao, mes_choice, ano_choice)
    
    print(f'O preço médio de abertura em {mes_choice}/{ano_choice} foi {preco_medio_abertura:.2f}')
    

if __name__ == '__main__':
    main()
    
