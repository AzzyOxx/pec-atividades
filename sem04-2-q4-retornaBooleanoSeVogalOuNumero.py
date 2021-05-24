#04. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal 
#ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.

def entr():
    s = input('Digite um, e somente um, caractere: ').lower().strip()
    return ord(s)

def oQue(l):
    if (l >= 97 and l <= 122) or (l >= 48 and l <= 57):
        return True
    else:
        return False
   
def main():
    a = entr()
    if oQue(a) == True:
        print(f'O caractere {chr(a)} é uma letra ou um número.')
    else:
        print(f'O caractere {chr(a)} não é uma letra ou um número.')

if __name__ == '__main__':
    main()
