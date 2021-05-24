'''
05. Escreva um programa que leia três números por
parâmetro e mostre na tela em ordem crescente.
'''
def maior(a, b):
    if a > b:
        return a , b
    else:
        return b , a

def ordem(a, b, c):
    t = a
    if b > a:
        t = b
    if c > t:
        t = c
        
    if t == a:
        s , p = maior(b , c)
    elif t == b:
        s , p = maior(a , c)
    else:
        s , p = maior(a , b)
        
    return p, s, t
        
    
def main():
    n1 = int(input('número: '))
    n2 = int(input('número: '))
    n3 = int(input('número: '))
    p, s, t = ordem(n1, n2, n3)

    #print(p , s, t)
    print(p)
    print(s)
    print(t)

if __name__ == '__main__':
    main()
