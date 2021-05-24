#Escreva um programa que leia um número inteiro entre 10 e 99,
#mostre uma das mensagens, a seguir, conforme o 
#número lido.
#• Nenhum dígito é ímpar.
#• Apenas um dígito é ímpar.
#• Os dois dígitos são ímpares

def separa(a):#123
    b = a % 10
    #print(b)
    c = a // 10
    d = c % 10
    #print(d)
    
    return b, d

def eh_par2(a, b, c):
    if a % 2 == 0:
        print(a)
    if b % 2 == 0:
        print(b)
    if c % 2== 0:
        print(c)

def eh_impar(a, b):
    i = 0
    if a % 2 != 0:
        i+=1
    if b % 2 != 0:
        i+=1
    
    return i

def classi(a):
    if a == 0:
        print('Nenhum dígito é ímpar.')
    elif a == 1:
        print('Apenas um dígito é ímpar.')
    else:
        print('Os dois dígitos são ímpares.')
    
def main():
    try:
        n = int(input('num: '))
        #n = int(input())
        if 10 <= n <= 99:
            n1, n2 = separa(n)
            c = eh_impar(n1, n2)
            #print(c)
            classi(c)
            #eh_par2(n1, n2, n3)
        else:
            print()

    except:
        print()
    


if __name__ == '__main__':
    main()

'''
123 L 10
120      12
=3
20
30
30
0
'''
