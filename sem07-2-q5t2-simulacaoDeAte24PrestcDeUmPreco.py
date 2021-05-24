'''
05. Escreva um programa que simula o valor (com duas casas decimais) da prestação de uma compra 
parcelada sem juros de 1x até 24x. O valor da compra é digitado pelo usuário. O valor da prestação sem 
juros, deve ser calculado como o valor da compra dividido pelo número de prestações de 1 até 24. O 
programa estará correto se o usuário informar o valor 1000 e o programa produzir o seguinte resultado:
    1x de R$ 1000.00
    2x de R$ 500.00
    3x de R$ 333.33
    4x de R$ 250.00
    [...]
    23x de R$ 43.48
    24x de R$ 41.67
'''

def prestacao(v):
    i = 0
    for cont in range(24):
        i += 1
        prest = v / i
        print(f'{i}x de R$ {prest:.2f}')
        


def main():
    valor = float(input('Digite o valor do produto: R$ '))
    print('\nOpções de parcelamento:\n')
    prestacao(valor)


if __name__ == '__main__':
    main()
