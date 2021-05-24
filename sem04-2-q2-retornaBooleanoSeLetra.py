#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal 
#ou consoante) ou o valor booleano False (falso) caso contrário

def retorna_unicode(l):    
    return ord(l)

def eh_letra(n, b):
    if letra(b) == True:
        print(f'O caractere {n}, é uma letra.')
    else:
        print(f'O caractere {n}, não é uma letra.')
        

def letra(l):
    return l >= 97 and l <= 122

def main():
    s = input('Digite um, E SOMENTE UM, caractere qualquer: ').lower().strip()
    a = retorna_unicode(s)
    eh_letra(s, a)
    #print(letra(a))

if __name__ == '__main__':
    main()


