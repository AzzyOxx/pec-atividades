#Escreva um programa que leia número inteiro qualquer e mostre na forma invertida.

def inverte(num):
    a = num
    aux = 0
    while a > 0:
        b = a % 10
        a = a // 10
        aux = aux * 10 + b
        
    return aux

def main():
    num = int(input('Digite um número inteiro qualquer: '))

    print(f'Número invertido: {inverte(num)}.')

if __name__ == '__main__':
    main()


    '''
    tentando fazer de outro jeito:
    i = -1
    b = 10
    a = num
    while a >= 1:
        a = a / b #a= 0.9
        i += 1 # i = 0
    
        
    print(i)
    d = 10**i #d = 1
    cont1 = 0
    aux = 0
    while cont1 < i:
        div = num % d #div = 9
        aux = aux*10 + div        
        cont1 += 1
        d = d**(i-1)
    return aux

    
    
    #
    11
    while True:
                
        if num > maior:
            maior = num
        if num < menor and num != 0:
            menor = num
        aux = num
        if num == 0: break
    '''

