#imprime uma mensagem na tela
print("Demonstração de divisão inteira(//) e resto (%).")
#variável "dividendo", do tipo int, recebe um valor a partir da leitura do teclado
dividendo = int(input("Digite o dividendo: "))
#variável "divisor", do tipo int, recebe um valor a partir da leitura do teclado
divisor = int(input("Digite o divisor: "))
#variável "quociente" recebe o valor INTEIRO do resultado da divisão entre os valores guardados nas variáveis "dividendo" e "divisor"
quociente = dividendo // divisor
#variável "resto" recebe o valor do 'RESTO' da divisão entre os valores guardados nas variáveis "dividendo" e "divisor"
resto = dividendo % divisor
#
print(f'{dividendo} dividido por {divisor}')
print(f' é igual a {quociente} e resto {resto}.')
