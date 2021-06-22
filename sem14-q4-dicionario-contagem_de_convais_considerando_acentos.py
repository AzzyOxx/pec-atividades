'''
04.Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, 
onde a chave é a vogal considerada. Inclua as vogais com acentos na contagem.
'''
def conta_vogais(frase):
    vogais = {}
    tem = 0
    for char in 'AÂÃÁaáàâã':
        for letra in frase:
            if letra == char:
                tem += 1
    vogais['A'] = tem

    tem = 0
    for char in 'EÊÉeéê':
        for letra in frase:
            if letra == char:
                tem += 1
    vogais['E'] = tem

    tem = 0
    for char in 'IÍií':
        for letra in frase:
            if letra == char:
                tem += 1
    vogais['I'] = tem

    tem = 0
    for char in 'OÔÓÕoóôõ':
        for letra in frase:
            if letra == char:
                tem += 1
    vogais['O'] = tem

    tem = 0
    for char in 'UÚuú':
        for letra in frase:
            if letra == char:
                tem += 1
    vogais['U'] = tem

    return vogais

def main():
    #entrada
    frase = input().strip()

    #processamento
    vogais = conta_vogais(frase)

    #saída
    for vogal in vogais:
        print(f'{vogal}: {vogais[vogal]}')
        
if __name__ == '__main__':
    main()
