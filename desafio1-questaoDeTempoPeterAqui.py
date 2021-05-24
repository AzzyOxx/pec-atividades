def quiz():
    s = input('Se, durante uma corrida de carros, você deixa o segundo colocado pra trás,\nqual é a sua colocação após a ultrapassagem?(Ex: 3 ou terceiro) \n').lower()    
    if s == '2' or s == "segundo":
        print("Isso mesmo, parabéns!!")
    else:
        print("Errado, a resposta é: segundo, se você ultrapassa o segundo colocado, assume o lugar dele, ficando em segundo!")
    a = '\n'
    print(a)

    s = input("A mãe de Maria tem cinco filhas: Fafá, Fefê, Fifi, Fofó e? Qual é o nome da quinta filha?\n").lower()
    if s == 'maria':
        print("Isso mesmo, parabéns!!")
    else:
        print("Errado, a resposta é: Maria, se a mãe de Maria tem cinco filhas, então, podemos enumerar a prole da seguinte forma: \n1 - Fafá, 2 - Fefe, 3 - Fifi, 4 - Fofo e 5 - (mas não menos importante) MARIA.")
    print(a)

    s = input("No caminho de casa até o mercado, uma senhora conta 10 árvores a sua direita.\nApós as compras, ela volta para casa e conta 10 árvores a sua esquerda. \nQuantas árvores ela viu no total nesse dia?\n").lower()
    if s == '10' or s == 'dez':
        print("Isso mesmo, parabéns!!")
    else:
        print("Nãaaaao, a resposta é: 10, são as mesmas dez árvores vistas de diferentes perspectivas.\nNa ida, as árvores estavam à direita da mulher, mas na volta, quando ela estava no sentido contrário da rua, \nas plantas podiam ser vistas à esquerda.")
    print(a)

    s = input('Em uma sala quadrada, temos um gato em cada canto. Cada gato vê outros três gatos. \nQuantos gatos há no total dentro da sala?\n').lower()
    if s == 'quatro' or s == '4':
        print("Isso mesmo, parabéns!!")
    else:
        print("Errado, a resposta é: quatro, se a sala é um quadrado, logo, possui quatro cantos. \nE já sabemos que em cada um desses cantos há um gato, ou seja, quatro felinos estão na sala. \nPara confirmar essa ideia, ainda sabemos que cada um dos gatos consegue ver os outros três que estão na sala")
    print(a)

    s = input('Fábio foi sozinho até a padaria no centro da cidade. \nDurante o percurso, encontrou duas garotas passeando com três cachorros, que estavam brincando com dois gatos, que, por sua vez, tinham dois donos. \nQuantos seres no total foram com Fábio até a padaria?\n').lower()
    if s == '0' or s == 'zero' or s == 'nenhum' or s == 'nenhuma':
        print("Isso mesmo, parabéns!!")
    else:
        print('Errado, a resposta é: zero, basta ler com atenção e interpretar o desafio: se Fábio foi sozinho até a padaria, então ninguém foi junto. \nEle apenas "encontrou" uma série de seres pelo caminho')
    print(a)

    s = input("Se uma borboleta vive cinco dias e a cada dia ela voa quatro metros, quantos metros ela terá percorrido em uma semana?\n").lower()
    if s == '20' or s == 'vinte':
        print("Isso mesmo, parabéns!!")
    else:
        print('Errado,  a resposta é: 20, se a borboleta vive cinco dias, ela terá morrido antes de uma semana (afinal, uma semana tem sete dias).\nNo entanto, se considerarmos seu tempo de vida, sabemos que, em cinco dias, ela voou 20 metros, pois 5 x 4 = 20')
    print(a)
#função principal
def main():
    print('=' * 10 + 'desafio: Questao de Tempo' + '=' * 10 + '\n')
    quiz()

if __name__ == '__main__':
    main()
