#variável "qtd_cavalos", do tipo int, recebe um valor a partir da leitura do teclado
qtd_cavalos = int(input("Quantidade de cavalos no haras: "))
#variável "ferraduras" recebe o valor da multiplicação do valores guardado  na variável "qtd_cavalos" por 4.
ferraduras = qtd_cavalos * 4
#impressão do valor das "ferradura"s com uma formatação para melhor compreensão
print(f'São necessários {ferraduras} ferraduras para o haras.')
