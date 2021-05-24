'''
Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo 
número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos 
(excluindo o zero).
'''

def media(a,b):
    return a / (b -1)

def main():
    total = 0
    cont = 0
    while True:
        num = int(input('Digite um número(0(zero) to stop!): '))
        total += num
        cont += 1
        if num == 0: break

    if cont == 1:
        pass
    else:
        print(f'A média aritmética dos números inseridos é: {media(total, cont)}.')

if __name__ == '__main__':
    main()
