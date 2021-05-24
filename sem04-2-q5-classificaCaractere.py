#05. Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou 
#“símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”;

def entr():
    s = input('Digite um, e somente um, caractere: ').lower().strip()
    return ord(s)

def oQue(l):
    if l >= 97 and l <= 122:
        if (l == 97 or l == 101 or l == 105 or l== 111 or l == 117):
            return 'vogal'
        else:
            return 'consoante'
    elif l >= 48 and l <= 57:
        return 'número'
    else:
        return 'símbolo'


def main():
    a = entr()
    print(f'O caractere {chr(a)}, é um(a) {oQue(a)}.')

if __name__ == '__main__':
    main()
