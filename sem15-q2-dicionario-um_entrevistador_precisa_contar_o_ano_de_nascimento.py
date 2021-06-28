'''
02.Um entrevistador precisa saber o ano de nascimento em que 1000 (mil) pessoas nasceram e, no final, deseja saber a 
quantidade de pessoas que nasceram em cada ano. Crie um dicionário e, a cada valor lido, some 1 (um) na chave 
correspondente ao ano do dicionário. Mostre quantas pessoas nasceram em cada ano exibindo do mais antigo ao mais 
recente.
'''

def main():
    print("Entrevista com mil pessoas: ")
    natalidade_por_ano = {}
    for ano in range(1000):
        ano = int(input('Em que ano o entrevistado nasceu?\n\> '))
        keys = list(natalidade_por_ano.keys())#atualiza a quantidade de chaves
        if ano in keys:
            natalidade_por_ano[ano] = natalidade_por_ano[ano] + 1

        if ano not in keys:
            natalidade_por_ano[ano] = 1

    maior = menor = keys[0]
    for ano in keys:
        if ano > maior:
            maior = ano
        if ano < menor:
            menor = ano
            
    ano_inicial = menor
    ano_final = maior
    print('Resultado da pesquisa: ')
    while ano_inicial <= ano_final:        
        print(f'{ano_inicial}: {natalidade_por_ano[ano_inicial]}')
        ano_inicial += 1
         
if __name__ == '__main__':
    main()
