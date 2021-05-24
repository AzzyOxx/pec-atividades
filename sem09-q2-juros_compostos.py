'''
01. Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o
preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e 
calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o 
carro à vista.
'''

def quando_vou_comprar(valor_car):
    poup = 10000
    aplicacao = 0
    mes = 0
    while poup < valor_car:
        aplicacao = 0.007 * poup
        valor_car += 0.004 * valor_car
        poup += aplicacao
        mes += 1
    return mes
       
def main():
    valor_car = float(input('Valor do carro: R$ '))
    #valor_car = float(input())
    
    print(f'Levariam {quando_vou_comprar(valor_car)} meses para a aplição render o valor necessário para comprar o carro à vista.')
    #print(mes, poup, valor_car)
    
if __name__ == '__main__':
    main()
