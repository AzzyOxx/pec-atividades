#variável "n", do tipo int, recebe um valor a partir da leitura do teclado
n = int(input("Digite um número entre 100 e 999: "))
#variável "unidade" recebe o valor do "resto" da divisão do valor guardado em n por 10
unidade = n % 10

print(unidade)
a = int(input())

# o valor da variável "n" é atualizado pelo valor inteiro da divisão de "n" por 10
n = n // 10

print(n)
a = int(input())


#variável "dezena" recebe o valor do resto da divisão do novo valor de "n" por 10
dezena = n % 10

print(dezena)
a = int(input())


# o valor da variável "n" é atualizado pelo valor inteiro da divisão de "n" por 10
n = n // 10

print(n)
a = int(input())


#variável "centena recebe o valor do resto da divisão de "n" por 10
centena = n % 10

print(centena)
a = int(input())


#imprimir na tela os valores processados, inseridos na mensagem conforme ordenados
print(f"unidade: {unidade}, dezena: {dezena}, centena: {centena}.")
