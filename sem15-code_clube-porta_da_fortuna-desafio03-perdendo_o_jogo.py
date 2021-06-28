from random import *

def desafio_perdendo_o_jogo():
    
    #imprime as três portas e as instruções do jogo
    print('''Porta da Fortuna!
=========

Existe um super prêmio atrás de uma dessas 3 portas!
Adivinhe qual é a porta certa para ganhar o prémio!
 _____   _____   _____
|     | |     | |     |
| [1] | | [2] | | [3] |
|    o| |    o| |    o|
|_____| |_____| |_____|
''')

    score = 0

    #o usuário muda esta variável para terminar o jogo
    jogando = True
    
    #repetir, enquanto a variável 'jogando' estiver com valor "True" 
    while jogando == True:

        print('\nEscolha um porta (1, 2 ou 3):')                
        #get the chosen door and store it as an integer (whole number)
        chosenDoor = input()
        chosenDoor = int(chosenDoor)

        #randomly choose the winning door number (between 1 and 3)
        winningDoor = randint(1,3)

        #show the player the winning and chosen door numbers
        print("A porta escolhida foi a", chosenDoor)
        print("A pota certa é a", winningDoor)

        #player wins if the chosen door and winning door number are the same
        if chosenDoor == winningDoor:
            print("Parabéns!")
            score += 1
        else:
            score = 0
            print("Que peninha!\nSua pontuação foi zerada T.T")

        #pergunte ao jogador se ele quer continuar jogando
        print("\nVocê quer jogar de novo?(s/n)")
        resposta = input()[0].lower()

        #termina o jogo se o jogador digitar 'n'
        if resposta == 'n':
            jogando = False

    print('Obrigado por jogar.')        
    print("Sua pontuação final é", score,'.')
        

def main():
    desafio_perdendo_o_jogo()


if __name__ == '__main__':
    main()
