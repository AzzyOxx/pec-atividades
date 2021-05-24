'''
01. Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre 
em quantos anos o valor acumulado será o dobro do valor inicial.
'''


def dobro(din, taxa):
    taxa = taxa / 100
    ano = 0
    valor_com_juros = din
    while valor_com_juros <= (2 * din):
        valor_com_juros = valor_com_juros + (valor_com_juros * taxa)
        ano += 1
    return valor_com_juros, ano

def main():
    #dep_ini = float(input())
    dep_ini = float(input('Deposito inicial: '))
    
    #tax_juros = float(input())
    tax_juros = float(input('Taxa de juros: '))
    valor, anos = dobro(dep_ini, tax_juros )
    
    print(f'Com R$ {dep_ini:.2f} como deposito inicial, à uma taxa de juros de {tax_juros}%an, levaria {anos} ano(os) para dobrar o valor, resultando em R$ {valor:.2f} reais.')
    #print(f'{valor:.2f}')
    #print(f'{anos}')


if __name__ == '__main__':
    main()
