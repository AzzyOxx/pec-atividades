#início da função denominada "eh_par", com um argumento
def eh_par(numero):
    # retorno da função com valores booleanos, confrome expressão
    return numero % 2 == 0

#realiazar impressão das frases concatenadas com o retorno gerado pela função "eh_par" chamada de dentro do print.
print('2 é par?', eh_par(2))
##realiazar impressão das frases concatenadas com o retorno gerado pela função "eh_par" chamada de dentro do print.
print('3 é par?', eh_par(3))
##realiazar impressão das frases concatenadas com o retorno gerado pela função "eh_par" chamada de dentro do print.
print('5 é ímpar?', not eh_par(5))
