'''
O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.
[...]
Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da 
compra. Ao finalizar com “X”, exiba o total a pagar.
    Observações:
    • Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção 
    inválida.”.
    • Enquanto o código não for 'X' o programa deve continuar lendo os itens.
'''

def compra(opcao):
    if opcao == 'h':
        return 5.5
    elif opcao == 'c':
        return 6.8
    elif opcao == 'm':
        return 4.5
    elif opcao == 'a':
        return 7
    elif opcao == 'q':
        return 4
    else:
        print('Opção inválida.')
        return 0
        
def main():
        
    total = 0
    while True:        
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        opcao = input('Escolha: ').strip().lower()[0]        
        if opcao == 'x' :
            print(f'Valor a pagar: R$ {total:.2f} reais.')
            break
        else:
            total += compra(opcao)
            print('\n')
            

if __name__ == '__main__':
    main()

