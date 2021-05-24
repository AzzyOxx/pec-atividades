#a variável "n", do tipo int, recebe um valor a partir da leituraa do teclado
n = int(input("Digite um número: "))
#impressão na tela com a funçao f''(com formatação) do dobro do valor guardado em "n"
print(f'O dobro de {n} vale {n*2}.')
#impressão na tela com a funçao f''(com formatação) do triplo do valor guardado em "n"
print(f'O triplo de {n} vale {n*3}.')
#impressão na tela com a funçao f''(com formatação) da raiz do valor guardado em "n" conforme a fórmula (n**1/2)
print(f'A raiz quadrada de {n} vale {n ** (1/2):.2f}')
