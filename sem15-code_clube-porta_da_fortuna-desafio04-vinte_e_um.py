from random import *

def passo03_quanta_sorte_voce_tem():
    
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

    tentativas = 0

    score = 0

    #o usuário muda esta variável para terminar o jogo
    jogando = True
    
    #repetir, enquanto a variável 'jogando' estiver com valor "True" 
    while score < 3:

        tentativas += 1

        print('\nTentativa', tentativas, ': Escolha uma porta (1, 2, 3)')
                                
        #get the chosen door and store it as an integer (whole number)
        chosenDoor = input()
        chosenDoor = int(chosenDoor)

        #randomly choose the winning door number (between 1 and 3)
        winningDoor = randint(1, 3)

        #show the player the winning and chosen door numbers
        print("A porta escolhida foi a", chosenDoor)
        print("A pota certa é a", winningDoor)

        #player wins if the chosen door and winning door number are the same
        if chosenDoor == winningDoor:
            print("Parabéns!")
            score += 1
        else:
            print("Que peninha!")

        print('Sua pontuação atual é', score)

    print('\n**Você conseguiu! Terminou o jogo em', tentativas, 'tentativas**')        

def desafio_vinte_e_um():
                            
    #essa variável deve ser alterada pelo usuário para terminar o jogo
    playing = True

    score = 0

    #imprime as instruções do jogo
    print('''Vinte e um!
===========
Tente fazer exatamente 21 pontos!''')

    #repete enquanto a variável 'playing' for 'True'
    while playing == True:

        #escolhe um numero aleatoriamente entre 1 e 10
        newNumber = randint(1,10)

        #soma o novo número à pontuação
        score = score + newNumber

        #mostra os dados para o jogador
        print("\nSeu próximo número é", newNumber)
        print("Sua pontuação agora é", score)

        #termina se o usuário digitar 'n'
        #ou se a pontuação for maior que 21
        print("\nGostaria de somar mais um número? (s/n)")
        answer = input()[0].lower()
        if answer.lower() == 'n' or score > 21:
            playing = False
        
    print("\nSua pontuação final é", score)

    #se o jogador marcar 21
    if score == 21:
        print("VOCÊ VENCEU!!")
    else:
        print("Que pena!")



    
def main():
    #passo03_quanta_sorte_voce_tem()
    desafio_vinte_e_um()


if __name__ == '__main__':
    main()
