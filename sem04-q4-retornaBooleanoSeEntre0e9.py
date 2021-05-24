#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um dígito entre ‘0’ 
#e ‘9’ ou o valor booleano False (falso) caso contrário

def e_num(n, a):
    #global crc
    print(f'O caractere {a} é um dígito entre 0 e 9?')
    if n == True:
        print(f'{n}, o caractere {a} é um dígito entre 0 e 9.')
    else:
        print(f'{n}, o caractere {a} não é um dígito entre 0 e 9.')

def uni(n):
    return '0' <= n <= '9'


def main():
    #variável global 'crc' criada, para melhor uso da função 'e_num()' linha 4
    #global crc(solução alternativa)
    #'crc' recebe o caractere
    #n = input()    
    crc = input('Digite UM, e SOMENTE UM, caractere qualquer:\n').lower().strip()
    
    c = uni(crc) #função uni(), linha 11
    e_num(c, crc) #processmento final, função e_num(), linha 4

if __name__ == '__main__':
    main()
