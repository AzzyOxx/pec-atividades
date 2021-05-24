#início da função "inverter", com um argumento
def inverter(numero):
    #variável "u" receber o valor da divisão, resto, do valor passado por argumento por 10
    u = numero % 10
    print(u)
    #variável "numero" atualiza 0 seu valor com a divisão, divisãi inteira, do seu próprio valor por 10
    numero = numero // 10
    print(numero)
    #variável "d" recebe o resto da divisão da variável "numero" por 10
    d = numero % 10
    print(d)
    #variável "numero" atualiza 0 seu valor com a divisão, divisãi inteira, do seu próprio valor por 10
    numero = numero // 10
    print(numero)
    #variável "c" recebe o resto da divisão da variável "numero" por 10
    c = numero % 10
    print(c)
    #variável "numero" atualiza 0 seu valor com a divisão, divisãi inteira, do seu próprio valor por 10
    numero = numero // 10
    print(numero)
    #variável "m" recebe o resto da divisão da variável "numero" por 10
    m = numero % 10
    print(m)
    #variável "numero_invertido" recebe o valor resultante da fórmula
    numero_invertido = (u*1000) + (d*100) + (c * 10) + m
    
    #retorno da função
    return numero_invertido

#variável "n" recebe um valor, do tipo int, a partir da leitura do teclado
n = int(input("Digite um número entre 1000 e 9999: "))
#imprimir na tela a mensagem concatenada com os valores inseridos conforme a ordem da formatação
print(f'o inverso de {n} é {inverter(n)}')
