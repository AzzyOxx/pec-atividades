#05. Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.

import random

def num_maior(a):
    global maior
    if a > maior:
        maior = a
    
def main():
    
    global maior
    maior = 0
    
    i = 0
    for cont in range(100):#100
        #a = int(input())
        a = random.randrange(1, 1000)
        print(f'Número({i+1}/100): {a}')
        num_maior(a)
        i += 1
    print(maior)

            
        
if __name__ == '__main__':
    main()

