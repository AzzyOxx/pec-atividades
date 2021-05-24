#variável "valor", do tipo float, recebe um valor a partir da leitura do teclado
valor = float(input('Valor de geladeira: '))
#variável "desconto", do tipo float, recebe um valor a partir da leitura do teclado
desconto = float(input('Percentual do desconto: '))
#variável "fator" recebe o valor da porcentagem convertida em decimais, conforme a fórmula
fator = 1 - desconto / 100
print(fator)
#variável "valor" recebe o valor com o desconto
valor = valor * fator
#mensagem final ao usuário imprimindo o valor com o desconto
print(f'A geladeira com {desconto}% de desconto fica por {valor: .2f}')
