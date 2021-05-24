'''
03. Escreva um programa Python que apresente o menu
[...]
Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção inválida.”. 
Enquanto a opção for diferente de 0 (zero) deve-se continuar apresentando as opções. Obs: use como 
estrutura de repetição com teste no final e como estrutura condicional múltipla escolha.

'''

def menu(opcao):
    if opcao == 0:
        print('0 - Fim de serviço.')
    elif opcao == 1:
        print('1 - Olá. Como vai?')
    elif opcao == 2:
        print('2 - Vamos estudar mais.')
    elif opcao == 3:
        print('3 - Meus Parabéns!')
    else:
        print('Opção inválida.')
        
def main():    
    while True:
        print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')#
        opcao = input('Escolha: ')
        try:
            opcao = int(opcao)
            if opcao == 0 :
                menu(opcao)
                break
            else:
                menu(opcao)
                print('\n')
        except:
            menu(opcao)
            print('\n')

if __name__ == '__main__':
    main()

