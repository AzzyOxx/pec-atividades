#Escreva um programa que leia um conjunto 100 números inteiros e exiba o valor médio dos mesmos (com 
#duas casas decimais).

import random

def main():
    total = 0
    i = 0
    while i <= 99:#99
        #a = int(input())
        a = random.randrange(1, 100)
        print(a)
        total += a        
        i += 1    
    print("\nValor médio dos números inseridos: %.2f"%(total/100))

if __name__ == '__main__':
    main()
