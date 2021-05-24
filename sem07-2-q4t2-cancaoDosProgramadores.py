'''
04. Modifique mais um vez a canção dos programadores, dessa vez, gerando a canção dos bons 
programadores, que resolvem 11 erros de cada vez e ao chegar a zero declaram que o software está 
estabilizado. Atenção para o exemplo a seguir, especialmente, os versos finais.
    99 bugs no software, pegue onze deles e conserte...
    Tecle “Ctrl+F5”
    88 bugs no software, pegue onze deles e conserte...
    Tecle “Ctrl+F5”
    77 bugs no software, pegue onze deles e conserte...
    Tecle “Ctrl+F5”
    ...
    11 bugs no software, pegue onze deles e conserte...
    Tecle “Ctrl+F5”
    Sem erros no software! Está estabilizado!
'''

def cancao():
    i = 99
    for cont in range(9):        
        print(f'{i} bugs no software, pegue onze deles e conserte...')
        print('Tecle "Ctrl+F5"')
        i -= 11
        
    print('Sem erros no software! Está estabilizado!')

def main():
    cancao()

if __name__ == '__main__':
    main()
