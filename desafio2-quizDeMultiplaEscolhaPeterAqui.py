def quiz():
    print('''
Q1. Se, durante uma corrida de carros, você deixa o segundo colocado pra trás,
qual é a sua colocação após a ultrapassagem?
a - primeiro
b - segundo
c - terceiro
    ''')
    s = input().lower()
    y = 'Isso mesmo, parabéns!!'
    n = "Errado, a alternatica correta é a letra 'b'. Pois, se você ultrapassa o segundo colocado, assume o lugar dele, ficando em segundo!"
    if s == 'a':
        print(n)
    elif s == 'b':
        print(y)
    elif s == 'c':
        print(n)
    else:
        print('Você não escolheu a, b ou c :(')    
    a = '\n'
    print(a)

    print('''
Q2. A mãe de Maria tem cinco filhas: Fafá, Fefê, Fifi, Fofó e? Qual é o nome da quinta filha?
a - Fufú
b - Gagá
c - Maria
    ''')
    s = input().lower()
    n = "Errado, a resposta correta é 'c', se a mãe de Maria tem cinco filhas, então, podemos enumerar a prole da seguinte forma: \n1 - Fafá, 2 - Fefe, 3 - Fifi, 4 - Fofo e 5 - (mas não menos importante) MARIA."
    if s == 'a':
        print(n)
    elif s == 'b':
        print(n)
    elif s == 'c':
        print(y)
    else:
        print('Você não escolheu a, b ou c :(')
    print(a)
    
    print("""
Q3. No caminho de casa até o mercado, uma senhora conta 10 árvores a sua direita.
Após as compras, ela volta para casa e conta 10 árvores a sua esquerda.
Quantas árvores ela viu no total nesse dia?
a - 10
b - 20
c - 30
    """)
    s = input().lower()
    n = "Nãaaaao, a resposta correta é 'a', são as mesmas dez árvores vistas de diferentes perspectivas.\nNa ida, as árvores estavam à direita da mulher, mas na volta, quando ela estava no sentido contrário da rua, \nas plantas podiam ser vistas à esquerda."
    if s == 'a':
        print(y)
    elif s == 'b':
        print(n)
    elif s == 'c':
        print(n)
    else:
        print('Você não escolheu a, b ou c :(')
    print(a)

    print('''
Q4. Em uma sala quadrada, temos um gato em cada canto. Cada gato vê outros três gatos. Quantos gatos há no total dentro da sala?
a - 12
b - 9
c - 4
    ''')
    s = input().lower()
    n = "Errado, a resposta correta é 'c', se a sala é um quadrado, logo, possui quatro cantos. \nE já sabemos que em cada um desses cantos há um gato, ou seja, quatro felinos estão na sala. \nPara confirmar essa ideia, ainda sabemos que cada um dos gatos consegue ver os outros três que estão na sala."
    if s == 'a':
        print(n)
    elif s == 'b':
        print(n)
    elif s == 'c':
        print(y)
    else:
        print('Você não escolheu a, b ou c :(')
    print(a)
    
    print('''
Q5. Fábio foi sozinho até a padaria no centro da cidade.
Durante o percurso, encontrou duas garotas passeando com três cachorros,
que estavam brincando com dois gatos, que, por sua vez, tinham dois donos.
Quantos seres no total foram com Fábio até a padaria?
a - 0
b - 5
c - 9
    ''')
    s = input().lower()
    n =  "Errado, a resposta correta é 'a' zero, basta ler com atenção e interpretar o desafio: se Fábio foi sozinho até a padaria, então ninguém foi junto. \nEle apenas 'encontrou' uma série de seres pelo caminho."
    if s == 'a':
        print(y)
    elif s == 'b':
        print(n)
    elif s == 'c':
        print(n)
    else:
        print('Você não escolheu a, b ou c :(')
    print(a)
    
    print('''
Q6. Se uma borboleta vive cinco dias e a cada dia ela voa quatro metros, quantos metros ela terá percorrido em uma semana?
a - 20
b - 24
c - 28
    ''')
    s = input().lower()
    n = "Errado,  a resposta é 'a', se a borboleta vive cinco dias, ela terá morrido antes de uma semana (afinal, uma semana tem sete dias).\nNo entanto, se considerarmos seu tempo de vida, sabemos que, em cinco dias, ela voou 20 metros, pois 5 x 4 = 20."
    if s == 'a':
        print(y)
    elif s == 'b':
        print(n)
    elif s == 'c':
        print(n)
    else:
        print('Você não escolheu a, b ou c :(')
    print(a)

def main():
    print('=' * 10 + 'desafio: Quiz de multipla escolha' + '=' * 10 + '=' * 10)
    quiz()

if __name__ == '__main__':
    main()
