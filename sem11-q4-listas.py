'''
4. Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os números 
ímpares na lista IMPAR. Imprima as três listas.
'''

def recebe20():
    num = 20
    lista = []
    lista_par = []
    lista_impar = []
    cont = 0
    print('Preenchendo uma lista com 20 números: ')
    while cont < num:
        n_paraInserir =int(input('Digite um número: '))
        #n_paraInserir = formataFloatCasas(n_paraInserir,1)
        lista.append(n_paraInserir)
        if n_paraInserir % 2 == 0:
            lista_par.append(n_paraInserir)
        else:
            lista_impar.append(n_paraInserir)
        cont += 1
    return lista, lista_par, lista_impar

def main():
    #entrada e processamento
    numeros, par, impar = recebe20()
    
    #saída
    print(f'Lista dos números inseridos: {numeros}\nLista dos número pares inseridos: {par}\nLista dos números ímpares inseridos: {impar}')
    
if __name__ == '__main__':
    main()
