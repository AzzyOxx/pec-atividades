'''
04. Escreva um programa que gere a seguinte sequência: 
10, 20, 30, 40, ..., 990, 1000.
Considere a separação dos números por vírgula seguido de espaço em brando e o pontos no final da 
sequência.
'''

def main():
    #contadores
    i = 0
    a = 0

    #gerando a sequência
    while i <= 99:
        a += 10
        if a < 1000:
            print(a, end = ', ')       
            i += 1
        else:#colocando o '.' depois de 1000
            print(a, end = '.')
            i += 1            
        
if __name__ == '__main__':
    main()

#opçôes para solução:
#vetor = list(range(5))
#ii = []
