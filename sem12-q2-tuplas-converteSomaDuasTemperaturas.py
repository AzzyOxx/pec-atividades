'''
02. Utilizando a definição de valor da temperatura com tupla da questão anterior, desenvolva uma função
que soma duas temperaturas que podem estar em Celsius ou em Fahrenheit. Se as duas temperaturas estiverem
na mesma escala, a resposta deve estar na mesma escala. Se as temperaturas estiverem em escalas diferentes,
a resposta deve ser dada na escala da segunda temperatura. Considere até 4 (quatro) casas decimais.
'''

#soma duas temperaturas, se necessário converte para a escala da primeira temperatura
def soma_temperatura(tupla_com_as_temperaturas):
    temperatura1 = tupla_com_as_temperaturas[0]
    temperatura2 = tupla_com_as_temperaturas[2]
    if tupla_com_as_temperaturas[1] != tupla_com_as_temperaturas[3]:
        if tupla_com_as_temperaturas[3] == 'C':
            #convertendo o tupla_com_as_temperaturas[3] para celsius
            temperatura1 = (tupla_com_as_temperaturas[0] - 32) * (5/9), 'C'
        else:
            #convertendo o tupla_com_as_temperaturas[3] para fahrenheit
            temperatura1 = (tupla_com_as_temperaturas[0] * (9/5))  + 32, 'F'
        soma_temp = round(temperatura1[0] + temperatura2,4) , temperatura1[1]
    else:
        soma_temp = round(temperatura1 + temperatura2, 4), tupla_com_as_temperaturas[1] 
    return soma_temp
    
def main():
    #entrada de dados
    print(f'{"="*15}Soma duas temperaturas{"="*15}')
    temperatura01 = float(input('Digite a primeira temperatura: '))
    escala01 = input('Agora digite a escala ("C" ou "F": ): ').strip().upper()[0]
    temperatura02 = float(input('Digite a segunda temperatura: '))
    escala02 = input('Agora digite a escala ("C" ou "F": ): ').strip().upper()[0]
    temperaturas = (temperatura01, escala01, temperatura02, escala02)

    #processamento
    soma_temp = soma_temperatura(temperaturas)

    #saída
    print(f'A soma das temperatura informadas foi: {soma_temp[0]} {soma_temp[1]}º.')
    
if __name__ == '__main__':
    main()
