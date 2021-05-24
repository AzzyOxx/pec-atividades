#variável “preco”, do tipo float, recebe o valor do preço a partir da leitura do teclado
preco = float(input("Digite o preço: "))
#variável “preco_com_desconto” recebe o valor da variável “preco” multiplicado por 0.90
preco_com_desconto = preco * 0.90
#atualização do valor atribuído para a variável “preco_com_desconto”, por meio da função “round”,limitando a saída para 2 casas decimais após a virgula
preco_com_desconto = round(preco_com_desconto, 2)
#saída final, após o precessamento, do valor do preço com desconto guardado na variável “preco_com_desconto”
print("Preço com desconto: ", preco_com_desconto)
