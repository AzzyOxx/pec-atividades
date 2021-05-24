#início da função nomeada "troca"
def trocar(x1, x2):
    #retorno da função com os valores trocados
    return x2, x1
#variável n1, do tipo int, recebe um valor a partir da leitura do teclado
n1 = int(input('Primeiro número: '))
#variável n2, do tipo int, recebe um valor a partir da leitura do teclado
n2 = int(input('Segundo número: '))
#chamando a função "troca" passando n1 e n2 como argumentos e alocando os valores nos mesmos
n1, n2 = trocar(n1, n2)
#imprimir na tela a mensagem concatenada com os valores inseridos conforme a formatação
print(f'Primeiro {n1}; Segundo {n2}.')
