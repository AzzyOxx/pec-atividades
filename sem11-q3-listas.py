'''
3. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) 
casas decimais.
b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa 
decimal. Se n = 0, imprima “SEM NOTAS”.
c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
Dica: certifique-se de ler apenas um caractere com input()[0]
'''
def formataFloatCasas(num,casas):
    semCasasDecimais = int(num)
    depoisDaVirgula = num - semCasasDecimais
    depoisDaVirgula = depoisDaVirgula * 10**casas
    depoisDaVirgula = int(depoisDaVirgula)
    depoisDaVirgula = depoisDaVirgula / 10**casas

    return semCasasDecimais + depoisDaVirgula    
    
def inverteInsersaoFloats(num):
    lista = []
    cont = 0
    print('Preenchendo a lista com {num} termos: ')
    while cont < num:
        n_paraInserir =float(input(f'{cont+1}º termo: '))
        #n_paraInserir = formataFloatCasas(n_paraInserir,4)
        n_paraInserir = round(n_paraInserir, 4)
        lista.insert(0,n_paraInserir)
        cont += 1
    return lista

def recebe_notas(num):
    lista = []
    cont = 0
    print('Lista de notas: ')
    while cont < num:
        n_paraInserir =float(input('Digite uma nota: '))
        #n_paraInserir = formataFloatCasas(n_paraInserir,1)
        lista.append(n_paraInserir)
        cont += 1
    return lista

def mediaAritimetrica(lista, num):#n é igual ao númuero de termos da lista
    cont = 0
    total = 0
    while cont < num:
        total += lista[cont]
        #n_paraInserir = formataFloatCasas(n_paraInserir,1)
        cont += 1
    media = total / num
    media = round(media, 1)        
    return media

def recebe_Nletras(num):
    lista = []
    cont = 0
    vogais = 0
    consoantes = []
    print('Preenchendo uma lista de caracteres: ')
    while cont < num:
        l_paraInserir =input('Digite uma letra: ')[0]
        lista.append(l_paraInserir)
        if l_paraInserir in 'AEIOUaeiou':
            vogais += 1
        elif l_paraInserir not in '0123456789':
            consoantes.append(l_paraInserir)
        cont += 1
    
        
    return lista , vogais, consoantes

def main():
    #entrada
    n_ezimoTermo = int(input('Tamanho da Lista: '))

    #processamento
    recebe_na_ordemInversa = inverteInsersaoFloats(n_ezimoTermo)
    n_notas = recebe_notas(n_ezimoTermo)
    lista_completa, vogais, consoantes = recebe_Nletras(n_ezimoTermo)
    

    #saída
    print(f'Termos da lista na ordem inversa: {recebe_na_ordemInversa}')
    print(f'Listas das notas inseridas: {n_notas}')
    if n_ezimoTermo != 0:
        print(f'Média das notas: {mediaAritimetrica(n_notas, n_ezimoTermo)}')        
    else:
        print('SEM NOTAS')
    #lista_completa,'\n',
    print(f'Vogais encontradas na lista de caracteres: {vogais}')
    print(f'Consoantes encontradas na lista de caracteres: {consoantes}')
    
if __name__ == '__main__':
    main()

