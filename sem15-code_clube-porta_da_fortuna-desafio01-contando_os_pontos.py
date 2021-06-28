from random import *

def passo01():
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
    
    #deixe o jogador fazer 3 tentativas
    for attempt in range(3):

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
        else:
            print("Que peninha!")

def desafio_contando_os_pontos():
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
    
    #deixe o jogador fazer 3 tentativas
    for attempt in range(3):

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
            print("Que peninha!")
            
    print("\nSua pontuação final é", score,'.')
        

def main():
    #passo01()
    desafio_contando_os_pontos()

if __name__ == '__main__':
    main()
