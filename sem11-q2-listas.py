'''
2. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
    a) preencha com 0 (zero) e imprima a lista;
    b) preencha com os números de 1 a n e imprima a lista;
    c) preencha com valores inteiros lidos pelo teclado e imprima a lista;
    d) preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert
para sempre incluir os elementos no início da lista;
'''
def preencheComZeros(num):
    lista = []
    cont = 0
    while cont < num:
        lista.append(0)
        cont += 1
    return lista

def oneToNterm(num):
    lista = []
    cont = 1
    while cont <= num:
        lista.append(cont)
        cont += 1
    return lista

def insere_c_teclado(num):
    lista = []
    cont = 1
    print('Preenchendo a lista:')
    while cont <= num:        
        n_paraInserir =int(input('Digite um número: '))
        lista.append(n_paraInserir)
        cont += 1
    return lista

def inverteInsersao(num):
    lista = []
    cont = 0
    print('Preenchendo a lista para depois inverter: ')
    while cont < num:
        n_paraInserir =int(input('Digite um número: '))
        lista.insert(0,n_paraInserir)
        cont += 1
    return lista

def main():
    #entrada
    n_ezimoTermo = int(input('Tamanho da lista: '))

    #processamento
    lista_deZeros = preencheComZeros(n_ezimoTermo)
    lista_de1AteN_termo = oneToNterm(n_ezimoTermo)
    preenche_c_teclado = insere_c_teclado(n_ezimoTermo)
    recebe_na_ordemInversa = inverteInsersao(n_ezimoTermo)
    
    #saida
    print(f'Lista preenchida com zeros: {lista_deZeros}')
    print(f'Lista com os termos de 1 a N: {lista_de1AteN_termo}')
    print(f'Lista com os termos inseridos com o teclado: {preenche_c_teclado}')
    print(f'Lista anterior na ordem invertida: {recebe_na_ordemInversa}')
        
    

if __name__ == '__main__':
    main()
