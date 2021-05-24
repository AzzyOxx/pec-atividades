'''
01. Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:
    N ! = 1 x 2 x 3 x ... x N-1 x N
    0 ! = 1
'''

def fatorial(n):
    aux = n - 1
    if n == 0:
        return 1
    else:        
        while aux >= 1:
            n *= aux
            aux -= 1
        return n
    
def main():
    n = int(input('Digite um número para calcular a sua fatorial: '))
    print(f'A fatorial do número {n} é igual a {fatorial(n)}.')    

if __name__ == '__main__':
    main()
