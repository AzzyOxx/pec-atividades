'''
02. A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo 
subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que 
leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n
sempre será maior ou igual a 2.
'''

def fibonacci(n):
    fib = 0
    f1= 0
    f2 = 1
    while n-1 > 0:
        #print(fib ,end = ', ')
        fib = f1 + f2
        f2 = f1
        f1 = fib        
        n -= 1
    return fib

def main():
    n = int(input('Digite a posição de um terno da sequência de Fibonacci que deseja saber: '))
    print(f'O {n}º termo da Sequência de Fibonacci é o número {fibonacci(n)}.')

if __name__ == '__main__':
    main()
