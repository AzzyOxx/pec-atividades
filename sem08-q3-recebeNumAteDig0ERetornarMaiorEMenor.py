'''
Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo 
número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos 
(excluindo o zero).
'''

def main():
    maior = 0
    menor = 0
    i = 0
    while True:
        num = int(input('Digite um número(0(zero) to stop!): '))
        if num == 0:
            break
        if i == 0:
            maior = num
            menor = num            
            i += 1
        elif num > maior:
            maior = num        
        elif num < menor:
            menor = num

    if i != 0:    
        print(f'O maior valor digitado foi o número {maior}.')
        print(f'Já o menor valor válido digitado foi o número {menor}.')
    else:
        pass

if __name__ == '__main__':
    main()
