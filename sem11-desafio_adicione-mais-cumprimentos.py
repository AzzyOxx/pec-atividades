from random import *

def main():
    print("Gerador de Cumprimentos")
    print("-"*23)
    
    adjetivos = ['maravilhoso', 'acima da média', 'excelente', 'excepicional', 'muito bom', 'habilidoso' ]
    hobbies = ['andar de bicicleta', 'programar', 'fazer chá', 'tocar violão', 'nadar', 'jogar futebol', 'cantar' ]

    nome = input("Qual é o seu nome?: ")
    print(f'Aqui está o seu cumprimento {nome}:' )    
    
    print(f'{nome}, você é {choice(adjetivos)} em {choice(hobbies)}!')
    print("De nada!")
if __name__ == '__main__':
    main()
