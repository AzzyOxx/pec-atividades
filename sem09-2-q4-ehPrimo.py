'''
04. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa 
que leia um número e determine se ele é ou não primo.
'''

def eh_primo(n):
    if n == 0: return False
    i = n
    cont = 0
    while i > 0:
        if n % i == 0:
            cont += 1
        i -= 1        
    return cont <= 2

def main():
    n = int(input('Digite um número qualquer para saber se ele é um número primo: '))
    if eh_primo(n) == True:
        print(f'O número {n} é um número primo.')
    else:
        print(f'O número {n} não é um número primo.')
    
if __name__ == '__main__':
    main()
