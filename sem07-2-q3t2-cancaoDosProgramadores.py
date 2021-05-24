'''
03. Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 e 
parando em 250 ou antes
    99 bugs no software, pegue sete deles e conserte...
    Tecle “Ctrl+F5”
    106 bugs no software, pegue sete deles e conserte...
    Tecle “Ctrl+F5”
    113 bugs no software, pegue sete deles e conserte...
    Tecle “Ctrl+F5”
    ...
    Vamos fazer mais um café!
'''


def cancao():
    i = 99
    for cont in range(22):        
        print(f'{i} bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')
        i += 7
        
    print('Vamos fazer mais um café!')

def main():
    cancao()

if __name__ == '__main__':
    main()
