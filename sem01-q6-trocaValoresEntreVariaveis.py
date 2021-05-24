#variável "valor_a", do tipo int, recebe um valor a partir da leitura do teclado
valor_a = int(input("Valor da variável A: "))
#variável "valor_b", do tipo int, recebe um valor a partir da leitura do teclado
valor_b = int(input("Valor da variável B: "))
#a variável "auxiliar" recebe o mesmo valor que está guardado na variável "valor_a"
auxiliar = valor_a
#a variável "valor_a" atualiza o seu valor recebendo o valor da variável "valor_b"
valor_a = valor_b
#a variável "valor_b" atualiza o seu valor recebendo o valor da variável "auxiliar"
valor_b = auxiliar
#impresão com formatação, f'', e valores contatenados na string conforme indicação das chaves
print(f"Valor da variável A: {valor_a}")
print(f"Valor da variável B: {valor_b}")
