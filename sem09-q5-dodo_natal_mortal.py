'''
. O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha 
Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6% 
dos animais dos animais vivos no começo do ano morreram e o número de 
animais nascidos ao longo do ano que sobreviveram foi de 1% da população 
inicial.
Escreva um programa que leia a população de aves no início do ano 1600 e 
imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população 
por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução 
quanto a população total cai para menos de 10% da população original.
'''

def main():
    populacao_original = int(input('Qual era a população em 1600? '))
    ano = 1600
    populacao_atual = populacao_original
    nascidos_sobreviventes = 0
    while populacao_atual >= 0.1 * populacao_original:
        nascidos_sobreviventes = 0.01 * populacao_atual
        mortos = 0.06 * populacao_atual
        populacao_atual = (populacao_atual - mortos) + nascidos_sobreviventes        
        print(f'Ano do cáculo: {ano}\nNascidos desse ano que sobreviveram: {nascidos_sobreviventes:.0f}\nMortes nesse ano: {mortos:.0f}\nPopulação atual: {populacao_atual:.0f}.\n')
        ano += 1
        
if __name__ == '__main__':
    main()
