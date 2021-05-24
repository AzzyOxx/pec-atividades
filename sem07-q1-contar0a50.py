#01. Escreva um programa que mostre todos os números inteiros de 1 a 50 (um por linha).

#essa função imprime na tela os números de 1 a 50.
def contando():
    #'i' é o 'contador'
    i = 1
    while i <= 50:
        print(i)
        i += 1

def main():
    contando()

if __name__ == '__main__':
    main()
