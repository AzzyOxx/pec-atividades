#1. Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

def soma(lista):
    cont = len(lista) - 1
    soma = 0
    i = 0
    while i <= cont:
        soma += lista[i]
        i += 1
    return soma
    
def multiplica(lista):
    cont = len(lista) - 1
    mult = 1
    i = 0
    while i <= cont:
        mult *= lista[i]
        i += 1
    return mult
    
def main():
    lista_d_nums = []
    i = 0

    print('Preencha a lista com 10 números: ')
    while i <= 9:
        num = int(input(f'{i+1}º termo: '))
        lista_d_nums.append(num)
        i += 1

    print(f'Lista com os números inseridos: {lista_d_nums}')    
    print(f'Soma dos termos da lista: {soma(lista_d_nums)}')
    print(f'Multiplicação dos termos da lista: {multiplica(lista_d_nums)}')
    
if __name__ == '__main__':
    main()
