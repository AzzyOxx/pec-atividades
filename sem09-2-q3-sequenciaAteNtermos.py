'''
03. Sendo H = 1 + 1/2 + 1/3 + ... + 1/n, escreva um programa para calcular o valor de H. O número n é lido.
'''

def valorH(n):
    h = 0
    while  n > 0:
        h += 1/n
        n -= 1
    return h

def main():
    n = int(input('Digite qual será o n-ésimo termo: '))
    print(f'O valor da soma da sequência é {valorH(n)}.')

if __name__ == '__main__':
    main()
