'''
01. Considereuma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes: 
temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é 
representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as 
temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de 
duas temperaturas, na forma temperatura e escala (t, e) separadamente, e mostre qual é a maior. Considere até 4 
(quatro) casas decimais).
Use upper() e colchetes
'''

#essa função compara duas temperaturas e retorna a maior delas
def maior_temperatura(tupla_com_as_temperaturas):
    temperatura1 = tupla_com_as_temperaturas[0]
    temperatura2 = tupla_com_as_temperaturas[2]
    maior = 0
    if tupla_com_as_temperaturas[1] != tupla_com_as_temperaturas[3]:
        if tupla_com_as_temperaturas[1] == 'C':
            #convertendo a tupla_com_as_temperaturas[3] para celsius
            temperatura2 = (tupla_com_as_temperaturas[2] - 32) * (5/9)
        else:
            #convertendo a tupla_com_as_temperaturas[3] para fahrenheit
            temperatura2 = (tupla_com_as_temperaturas[2] * (9/5))  + 32
    if temperatura1 < temperatura2:
        maior = 2    
    return round(tupla_com_as_temperaturas[maior], 4), tupla_com_as_temperaturas[maior + 1]
    
def main():
    #entrada de dados
    print(f'{"="*15}Comparando duas temperaturas{"="*15}')
    temperatura01 = float(input('Digite a primeira temperatura: '))
    escala01 = input('Agora digite a escala ("C" ou "F": ): ').strip().upper()[0]
    temperatura02 = float(input('Digite a segunda temperatura: '))
    escala02 = input('Agora digite a escala ("C" ou "F": ): ').strip().upper()[0]
    temperaturas = (temperatura01, escala01, temperatura02, escala02)

    #processamento
    maior_temp = maior_temperatura(temperaturas)

    #saída
    print(f'A maior temperatura informada foi: {maior_temp[0]} {maior_temp[1]}º.')


if __name__ == '__main__':
    main()
