#03. Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles.
#Considere que todos os valores são diferentes. NÃO use as funções embutidas min() e max().
'''
def maior(a, b, c, d, e):
    m = 0
    if a > b:
        m = a
    else:
        m = b
    if c > m:
        m = c
    if d > m:
        m = d
    if e > m:
        m = e
    return m
'''
def maior(a, b, c, d, e):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    if d > m:
        m = d
    if e > m:
        m = e
    return m

def menor(a, b, c, d, e):
    m = a
    if b < m:
        m = b
    if c < m:
        m = c
    if d < m:
        m = d
    if e < m:
        m = e    
    return m
       
def main():
    
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    n4 = int(input('Digite um número: '))
    n5 = int(input('Digite um número: '))

    
    a = maior(n1, n2, n3, n4, n5)
    b = menor(n1, n2, n3, n4, n5)
    
    #print(f'Maior: {a}\nMenor: {b}')
    #print(a, b)
    print(a)
    print(b)

if __name__ == '__main__':
    main()



'''
def maior_e_menor(a, b, c, d, e):
    
    if (a > b and b > c and c > d and d > e):
        return a
    elif (a < b and b > c and c > d and d > e): #2
        return b
    elif (a < b and b < c and c > d and d > e): #3
        return c
    elif (a < b and b < c and c < d and d > e):
        return d
    else:
        return e
    
def maior_e_menor2(a, b, c, d, e):
    if a > b > c > d > e:
        return a    
    elif a < b > c > d > e: #2
        return b 
    elif a < b < c > d > e: #3
        return c
    elif a < b < c < d > e:
        return d
    else:
        return e
''' 
