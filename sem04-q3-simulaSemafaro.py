#Escreva um programa que leia a cor de um sinal de trânsito
#(“V” é verde; “A” é amarelo; “E” é vermelho) e retorne 
#a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.
    
def sinal(s):
    if s == 'v':
        return 'Siga'
    elif s == 'a':
        return 'Atenção'
    elif s == 'e':
        return 'Pare'
    #caso não seja digitado v, a ou e
    else:
        print("Você não digitou 'V', 'A' ou 'E'. Tente novamente!")
        #chamando a função principal de novo, se as entradas não corresponderem ao esperado
        main()


def main():
    
    s = input('Digite o caractere correspondente a cor sinal:( V = verde ou A = amarelo ou E = vermelho)\n').lower().strip()
    print(f'{sinal(s)}\n')
        


if __name__ == '__main__':
    main()
