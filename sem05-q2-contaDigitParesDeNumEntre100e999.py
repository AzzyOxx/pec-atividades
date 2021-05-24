# Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse 
# número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.

def separa(a):#123
    b = a % 10
    #print(b)
    c = a // 10
    d = c % 10
    #print(d)
    e = c // 10
    f = e % 10
    #print(f)
    return b, d, f

def eh_par2(a, b, c):
    if a % 2 == 0:
        print(a)
    if b % 2 == 0:
        print(b)
    if c % 2== 0:
        print(c)
def eh_par(a, b, c):
    i = 0
    if a % 2 == 0:
        i += 1
    if b % 2 == 0:
        i += 1
    if c % 2== 0:
        i += 1    
    
    return i

def main():
    try:
        n = int(input('num: '))
        #n = int(input())
        if n >= 100 and n <= 999:
            n1, n2, n3 = separa(n)
            c = eh_par(n1, n2, n3)
            print(c)
        else:
            print()
        
        #eh_par2(n1, n2, n3)
    
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
