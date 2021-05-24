# variável “anos”, do tipo int, recebe um valor a partir da leitura do teclado
anos = int(input('Anos de serviço: '))
#variável “valor_por_ano”, do tipo float,  recebe um valor a partir da leitura do teclado
valor_por_ano = float(input('Valor por ano: '))
#variável “bonus” recebe o resultado da multiplicação entre os valores guardados nas variáveis “anos” e “valor_por_ano”, respectivamente. 
bonus = anos * valor_por_ano
#imprimir na tela, após o processamento, o valor correspondente ao bonus,  com desconto guardado na variável “preco”_com_desconto”
print('Bônus de R$ %5.2f ' % bonus)
