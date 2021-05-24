#início de uma função nomeada "minutos_para_horas", com um argumetos
def minutos_para_horas(qtd_minutos):
    #variável "horas" recebe o valor passado como argumento e dividido,divisão inteira, por 60 
    horas = qtd_minutos // 60
    print(horas)
    #variável "minutos" recebe o valor passado como argumento e dividido, divisão modular, por 60 
    minutos = qtd_minutos % 60
    print(minutos)
    #retorno da função 
    return f'{horas}h{minutos}min'

#variável "minutos", recebe um valor a partir da leitura do teclado
minutos = int(input('Quantidade de minutos: '))
#variável "horas", o retorno da função "minutos_para_horas" com a passagem do valor de "minutos" como argumento
horas = minutos_para_horas(minutos)
#imprimir na tela a mensagem a inserção do valor de "horas" concatenado conforme a formatação
print(f'{minutos} minutos são equivalentes a {horas}')
