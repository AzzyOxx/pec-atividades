#inicio de uma função denominada "area_quadrado", com um argumento
def area_quadrado(lado):
    #retorno da função, multiplicação do argumento por ele mesmo.
    return lado * lado

#inicio de uma função denominada "perimetro_quadrado", com um argumento
def perimetro_quadrado(lado):
    #retorno da função
    return lado * 4

#variável "valor_lado", do tipo float, recebe um valor a partir da leitura do teclado
valor_lado = float(input('Lado do quadrado: '))
#imprimir na tela mensagem concatenada com o retorno da função "area_quadrado" com o valor da variável |"valor_lado" sendo passado como argumento
print('Área do quadrado:', area_quadrado(valor_lado))
#imprimir na tela mensagem concatenada com o retorno da função "perimetro_quadrado" com o valor da variável "valor_lado" sendo passado como argumento
print('Perímetro do quadrado: ', perimetro_quadrado(valor_lado))
