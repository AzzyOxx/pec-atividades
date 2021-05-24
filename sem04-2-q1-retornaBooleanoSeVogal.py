#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou o 
#valor booleano False (falso) caso contrário.

#processamento da entrada
def resul(l):
    print(f'O caractere {l} é uma vogal??')
    if vog(l) == True:
        print(f'{vog(l)}, o caractere {l} é uma vogal.')
    else:
        print(f'{vog(l)}, o caractere {l} não é uma vogal.')

#função 'é uma vogal??'    
def vog(l):
    return l in 'aeiou'

def main():
    
    s = input('Digite UM, e SOMENTE UM, caractere: ').lower().strip()

    resul(s)#função resul(), linha 5
    


if __name__ == '__main__':
    main()
