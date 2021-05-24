#03. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma CONSOANTE
#ou o valor booleano False (falso) caso contrário.

def entr():
    s = input('Digite um, e somente um, caractere: ').lower().strip()
    return ord(s)

def letra(l):
    if l >= 97 and l <= 122:
        if l != 97 and l != 101 and l!= 105 and l!= 111 and l!= 117:
            return True
        else:
            return False
    else:
        return False
    
def main():
    a = entr()
    if letra(a) == True:
        
        print(f'O caractere {chr(a)} é uma consoante. ')
    else:
        
        print(f'O caractere {chr(a)} não é uma consoante.')
    #print(letra(a))

if __name__ == '__main__':
    main()

