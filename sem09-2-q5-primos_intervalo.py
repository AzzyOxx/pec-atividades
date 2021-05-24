'''
05. Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.
'''

def primos(a, b):
    if b < a:
        aux = a
        a = b
        b = aux       
    print(f'No intervalo de {a} até o {b}, estão os seguintes números primos:')
    while a <= b:
        primo = eh_primo(a)
        if 0 < primo <= 2:
            print(a)
        a += 1
    
def eh_primo(n):
    if n == 0: return 0
    i = n
    cont = 0
    while i > 0:
        if n % i == 0:
            cont += 1
        i -= 1
        
    return cont

def main():
    print('Esse programa mostra os números primos de um intervalo entre números inteiros.')
    n = int(input('Digite o primeiro número do intervalo: '))
    n1 = int(input('Digite o segundo número do intervalo: '))
    primos(n, n1)
    
if __name__ == '__main__':
    main()
