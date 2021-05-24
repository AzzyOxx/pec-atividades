#02. Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade 
#de números pares e números ímpares contidos no mesmo.

import random

#incrementa as variáveis globais 'par' ou 'imp', conforme o número seja par ou impar
def eh_par(a):
    global imp
    global par
    
    if a % 2 == 0:
        par += 1
    else:
        imp += 1
        
        

def main():
        
    global par
    par = 0
    global imp
    imp = 0
    
    i = 0 #contador    
    # o emlaço recebe 100 números, um a um, a cada número é chamada a função eh_par(a), para determinar se o número recebido é par ou impar
    while i <= 99:
        
        #a = int(input(Digite um número({i+1}/100): ))
        a = random.randrange(1, 100)
        print(f'Digite um número({i+1}/100): {a}')
        b = eh_par(a)#linha 7
        i += 1

    
    print(f'\nQuantos números pares: {par}.\nQuantos números ímpares: {imp}.')

if __name__ == '__main__':
    main()
