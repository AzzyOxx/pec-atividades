#início de uma função nomeada "percentual", com dois argumetos
def percentual(valor, porcentagem):
    #retorno da função para porcentagem descontada do "valor"
    return valor * (porcentagem / 100)

#variável "pr", do tipo float, recebe um valor a partir da leitura do teclado
pr = float(input("Preço: "))
#variável "vr_p", do tipo float recebe um valor a partir da leitura do teclado
vr_p = float(input("Percentual: "))
#variável "pr_acres" recebe o valor de "pr" mais o percentual conforme a função "porcentagem"
pr_acres = pr + percentual(pr, vr_p)
#variável "pr_desc" recebe o valor de "pr" menos o percentual conforme a função "porcentagem"
pr_desc = pr - percentual(pr, vr_p)
#imprimir na tela a mensagem com os valores inseridos conforme a formatação
print(f'R${pr} com acréscimo de {vr_p}% fica por R${pr_acres}')
#imprimir na tela a mensagem com os valores inseridos conforme a formatação
print(f'R${pr} com desconto de {vr_p}% fica por R${pr_desc}')

#186-0316
