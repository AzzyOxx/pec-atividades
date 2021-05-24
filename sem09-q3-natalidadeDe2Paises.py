'''
02. Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3% 
ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a 
população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a 
população do país A.
'''

def popB_superaA(popA, popB):
    ano = 0    
    if popA > popB:
        while popB < popA:#=
            popA = 1.02 * popA
            popB = 1.03 * popB
            ano += 1
    else:
        aux = popA
        popA = popB
        popB = aux
        while popB < popA:#=
            popA = 1.02 * popA
            popB = 1.03 * popB
            ano += 1
    return ano

def main():
    populacao_A = int(input('Qual é a população do país A? '))
    populacao_B = int(input('Qual é a população do país B? '))
        
    print(f'Será necessário {popB_superaA(populacao_A,populacao_B )} ano(s) para que o páis com a menor população atualmente, se torne o país mais populoso.')

if __name__ == '__main__':
    main()
