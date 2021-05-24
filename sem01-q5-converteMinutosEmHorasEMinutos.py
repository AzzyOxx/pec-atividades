#variável "minutos", do tipo int, recebe um valor a partir da leitura do teclado
minutos = int(input("Digite uma quantidade de minutos: "))
#variável "h" recebe o valor INTEIRO da divisão conforme a fórmula
h = minutos // 60
print(h)
#variável "m" recebe o valor do RESTO da divisão conforme a fórmula
m = minutos % 60
print(m)
#impresão com formatação, f'', e valores contatenados na string conforme indicação das chaves
print(f'{minutos} minuto(s) é equivalente a {h} horas e {m} minutos.')
