def conceito(a):
    if a >= 8.5:
        print('A')
    elif 7 <= a < 8.5:
        print('B')
    elif 5 <= a < 7:
        print('C')
    elif 4 <= a < 5:
        print('D')
    else:
        print('E')
    
        
        
def main():
    while True:
        nota = input('Nota do aluno: ').strip()
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                conceito(nota)
                break
            else:
                print('Nota inválida.')
        except:
            print('Nota inválida.')

            

if __name__ == '__main__':
    main()

