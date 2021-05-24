#Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média 
#das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, 
#se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

def media(a, b, c):
    return (a + b + c) / 3

def nota( m, n3):
    if n3 > 8:
        m += 1
        if m > 10:
            m = 10
    print(f'O aluno obteve como média final {m} pontos.')

def main():
    n1 = int(input('Digite a primeira nota do aluno:\n'))
    n2 = int(input('Digite a segunda nota do aluno:\n'))
    n3 = int(input('Digite a terceira nota do aluno:\n'))    
    med = media(n1, n2, n3)#função media(), linha 5
    nota(med, n3)#função nota(), linha 8


if __name__ == '__main__':
    main()
