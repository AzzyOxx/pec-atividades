'''
04.Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia o nome do corredor 
e todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final mostre
classificação final em ordem (primeiro o vencedor(a)), como mostrado abaixo:

-------|----------------------|---------------|---------------|---------------
 Ordem |   Nome do Corredor   |  Tempo Total  |  Tempo Médio  | Melhor Volta  
-------|----------------------|---------------|---------------|---------------
   1   |         Eloá         |     719.8     |     72.0      |     66.5      
   2   |    Luiz Henrique     |     725.8     |     72.6      |     65.5      
   3   |       Gabriela       |     729.2     |     72.9      |     65.7      
   4   |        Heitor        |     745.3     |     74.5      |     65.0      
   5   |        Bianca        |     756.6     |     75.7      |     67.4      
   6   |        Joana         |     776.7     |     77.7      |     69.0      
-------|----------------------|---------------|---------------|---------------

'''

def classificacao(cronometragens):
    ranking_corredores = {}
    lugar = 1       
    for num in range(6):
        chave = list(cronometragens.keys())
        melhor_tempo =  sum(cronometragens[chave[0]]), chave[0] 
        for corredor in chave:
            if sum(cronometragens[corredor]) < melhor_tempo[0]:
                melhor_tempo = sum(cronometragens[corredor]), corredor

        ranking_corredores[melhor_tempo[1]] = lugar, melhor_tempo[0], cronometragens[melhor_tempo[1]]
        lugar += 1
        del cronometragens[melhor_tempo[1]]
        

    return ranking_corredores
            
            
    

def desempenho_corredores():
    corredores = {}
    for corredor in range(6):
        nome = input().strip()
        voltas_completas = []
        for volta in range(10):
            tempo = float(input())
            voltas_completas.append(tempo)
        corredores[nome] = voltas_completas

    return corredores
    
def main():
    #entrada
    cronometragem_da_corrida = desempenho_corredores()

    #processsanebto
    ranking = classificacao(cronometragem_da_corrida)
    
    #saída
    print( '-'*7 + '|' + '-'*22 + '|' + '-'*15 + '|' + '-'*15 + '|' + '-'*15 )
    print(f"{'Ordem': ^7}|{'Nome do Corredor': ^22}|{'Tempo Total':^15}|{'Tempo Médio': ^15}|{'Melhor Volta':^15}")
    print( '-'*7 + '|' + '-'*22 + '|' + '-'*15 + '|' + '-'*15 + '|' + '-'*15 )

    for corredor in ranking:
        print(f"{ranking[corredor][0]: ^7}|{corredor: ^22}|{round(ranking[corredor][1], 1):^15}|{round(ranking[corredor][1]/10, 1): ^15}|{min(ranking[corredor][2]):^15}")

    print( '-'*7 + '|' + '-'*22 + '|' + '-'*15 + '|' + '-'*15 + '|' + '-'*15 )        
        

if __name__ == '__main__':
    main()
