'''
05. Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro 
também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a 
situação se refere ao mês de outubro do ano de 2016, faça um programa leia o valor do salário e o valor 
da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com 
o cartão de crédito será superior ao seu próprio salário. 
Represente os meses como inteiros de 1 a 12. 
    Dica: Controle essas quatro variáveis:
    “dívida” que aumenta todo mês;
    “salário” que aumenta apenas se o número do mês for 3 (março);
    “mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12;
    “ano” que só é incrementado quando o mês retornar a 1
'''

def divida(sal, div):
    mes = 10
    ano = 2016
    while div <= sal:
        div = div + (div * 0.15)
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1
        if mes == 3:
            sal = sal + (sal * 0.05)
    return mes, ano

def main():
    salr = int(input('Salário atual: '))
    divd = int(input('Valor da dívida: '))
    a, b = divida(salr, divd)
    print(f'De acordo com as informações, se sua dívida não for paga, ela irá se tornar maior que o seu salário na data de {a}/{b}.')
    
if __name__ == '__main__':
    main()
