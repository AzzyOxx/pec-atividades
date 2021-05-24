#variável "dias", do tipo int, recebe um valor a partir da leitura do teclado.
dias = int(input("Quantidade de dias alugados: "))
#variável "km", do tipo float, recebe um valor a partir da leitura do teclado.
km = float(input("Quantos km foram percorridos: "))
#variável "total" recebe o valor do aluguel conforme a fórmula que calcula a taxa sobre a quantidade de dias e quilômetros rodados
total = (dias * 60) + (km * 0.15)
print(total)
#impressão do valor final formatado para melhor compreenssão
print(f'O total a pagar pelo aluguel é de R$ {total:.2f}')
