'''
02.Faça um programa que receba a temperatura média de cada mês do ano. A temperatura pode ser informada em graus
Celsius, Fahrenheit ou Kelvin. Após isto, calcule a média anual das temperaturas e mostre, em Kelvin, todas as
temperaturas acima da média anual e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 –
Fevereiro, ... ).
'''

def preenche_matriz(linhas, colunas):
    matriz = [] #lista vazia
    mes = 1
    for lin in range(linhas):
        linha = [] # cada linha é uma lista (vetor)
        for col in range(colunas):
            if col == 0:
                n = mes
                mes += 1
            elif col == 1:
                n = float(input('temperatura: '))
            else:
                n = input('escala: ')[0].upper().strip()                
            linha.append(n)
        # insere a linha na matriz
        matriz.append(linha)
    return matriz

''' essa função monta a matriz bidimensional no formato dos livros de matemática
def imprime_matriz_indice(matriz):
    for i_linha in range(len(matriz)):
        print('|', end = '')
        for i_coluna in range(len(matriz[i_linha])):
            #print(f'{matriz[i_linha][i_coluna]:3d}', end = ' ')
            print(f'{matriz[i_linha][i_coluna]}', end = ' ')
        print('|')
'''

#vamos converter tudo para Celseius, para depois somar e calcular a média
def media_anualTemperatura(matriz):                         
    soma_de_temperaturas = 0
    new_matriz = []
    for linha in matriz:
        temperatura = linha[1]
        if linha[2] != 'K':
            if linha[2] == 'C':
                #convertendo o tupla_com_as_temperaturas[3] para celsius
                temperatura = temperatura + 273.15
            if linha[2] == 'F':
                temperatura = ((temperatura - 32) *( 5/9 )) + 273.15
        soma_de_temperaturas += temperatura
        new_matriz.append([linha[0], temperatura, 'K'])

    return (soma_de_temperaturas / 12), new_matriz

def acimaMediaTempsMes(matriz, media):
    lista_dos_acimaMediaIndice = []
    for linha in matriz:
        if linha[1] > media:
            lista_dos_acimaMediaIndice.append(linha)
    return lista_dos_acimaMediaIndice

def mes_literal(mes):
    lista_mes = [ 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return lista_mes[mes-1]

def main():
    #entrada de dados
    matriz_mes_temperatura = preenche_matriz( 12, 3 )
    
    #processamento
    mediaTemperaturas, temperaturas_convertidasKelvin = media_anualTemperatura(matriz_mes_temperatura)
    mesesComTemperaturasAcimaMedia = acimaMediaTempsMes(temperaturas_convertidasKelvin, mediaTemperaturas)

    #saída
    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{round(mediaTemperaturas, 2)}K')
    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')    
    for linha in mesesComTemperaturasAcimaMedia:
        print(f'{mes_literal(linha[0])}: {round(linha[1], 2)}{linha[2]}')
    
if __name__ == '__main__':
    
    main()
