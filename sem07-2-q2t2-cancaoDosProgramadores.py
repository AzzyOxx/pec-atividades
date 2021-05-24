'''
02. Modifique a canção dos programadores do exercício anterior para incluir o refrão: Tecle “Ctrl+F5”. 
    Termine a canção com “Vamos fazer mais um café!”.
        99 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        100 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        101 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        ...
        250 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        Vamos fazer mais um café!
'''

def cancao():
    i = 99
    for cont in range(152):        
        print(f'{i} bugs no software, pegue um deles e conserte...')
        print('Tecle "Ctrl+F5"')
        i += 1
        
    print('Vamos fazer mais um café!')

def main():
    cancao()

if __name__ == '__main__':
    main()
