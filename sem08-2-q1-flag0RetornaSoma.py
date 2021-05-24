'''
01. Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação: 
A condição de saída do laço será a leitura do valor 0 (flag).
'''


def main():
    soma = 0
    while True:
        num = int(input('Digite um número: '))
        soma += num
        
        if num == 0: break

    print(f'A soma dos valores inseridos é {soma}.')

if __name__ == '__main__':
    main()
