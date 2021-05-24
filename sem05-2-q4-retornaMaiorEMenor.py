#03. Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles.
#Considere que todos os valores são diferentes. NÃO use as funções embutidas min() e max().

def maior(a, b, c, d, e, med):  
    if a > med:
        print(a)
    if b > med:
        print(b)
    if c > med:
        print(c)
    if d > med:
        print(d)
    if e > med:
        print(e)
    #return m

def media(a, b, c, d, e):
    return (a + b + c + d + e) / 5
      
def main():
    
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    n4 = int(input('Digite um número: '))
    n5 = int(input('Digite um número: '))
    
    
    m = media(n1, n2, n3, n4, n5)
    #round(m,2)
    #print("Média = %.2f" % m)
    print("%.2f" % m)
    maior(n1, n2, n3, n4, n5, m)
    #print(f'Maior: {a}\nMenor: {b}')

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
