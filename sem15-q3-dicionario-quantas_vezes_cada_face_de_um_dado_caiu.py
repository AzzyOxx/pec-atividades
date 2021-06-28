'''
03.Suponha que vamos jogar um dado e queremos saber quantas vezes cada face (de 1 a 6) caiu. Faça um programa que 
leia o resultado de cada jogada do dado e armazena em um dicionário. A face do dado é a chave para o dicionário e 
a leitura de um valor 0 (zero) na face encerra o jogo. Mostre quantas vezes o dado foi lançado e quantas vezes cada 
face saiu.
'''

def main():
    faces_dado = {1: 0,
               2: 0,
               3: 0,
               4: 0,
               5: 0,
               6: 0
               }

    #entrada
    jogadas_feitas = 0
    while True:
        jogada = int(input('Joque o dado e informe qual o número da face sorteada:\n(press 0 to stop)\n'))
        if jogada == 0: break
        faces_dado[jogada] = faces_dado[jogada] + 1
        jogadas_feitas += 1

    #saída
    print(f'O dado foi lançado {jogadas_feitas} vezes.')
    for item in faces_dado:
        print(f'A face {item} saiu {faces_dado[item]} vezes.')
    
    
    
if __name__ == '__main__':
    main()

'''
O dado foi lançado 32 vezes.
A face 1 saiu 4 vezes.
A face 2 saiu 7 vezes.
A face 3 saiu 5 vezes.
A face 4 saiu 9 vezes.
A face 5 saiu 6 vezes.
A face 6 saiu 1 vezes.
'''

'''
1
3
3
2
5
4
4
4
1
5
2
2
5
4
5
2
5
4
2
4
5
4
4
4
2
2
3
1
6
1
3
3
0
'''
