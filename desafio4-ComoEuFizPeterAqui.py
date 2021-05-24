#deve conter todas as perguntas do quiz
def quiz():
    print('''
Q1. Se, durante uma corrida de carros, você deixa o segundo colocado pra trás,
qual é a sua colocação após a ultrapassagem?
a - primeiro
b - segundo
c - terceiro
    ''')
    quiz_conf(1)
    print('''
Q2. A mãe de Maria tem cinco filhas: Fafá, Fefê, Fifi, Fofó e? Qual é o nome da quinta filha?
a - Fufú
b - Gagá
c - Maria
    ''')
    quiz_conf(2)
    print("""
Q3. No caminho de casa até o mercado, uma senhora conta 10 árvores a sua direita.
Após as compras, ela volta para casa e conta 10 árvores a sua esquerda.
Quantas árvores ela viu no total nesse dia?
a - 10
b - 20
c - 30
    """)
    quiz_conf(3)
    print('''
Q4. Em uma sala quadrada, temos um gato em cada canto. Cada gato vê outros três gatos. Quantos gatos há no total dentro da sala?
a - 12
b - 9
c - 4
    ''')
    quiz_conf(4)
    print('''
Q5. Fábio foi sozinho até a padaria no centro da cidade.
Durante o percurso, encontrou duas garotas passeando com três cachorros,
que estavam brincando com dois gatos, que, por sua vez, tinham dois donos.
Quantos seres no total foram com Fábio até a padaria?
a - 0
b - 5
c - 9
    ''')
    quiz_conf(5)
    print('''
Q6. Se uma borboleta vive cinco dias e a cada dia ela voa quatro metros, quantos metros ela terá percorrido em uma semana?
a - 20
b - 24
c - 28
    ''')
    quiz_conf(6)
#entrada e processamento01 da resposta   
def quiz_conf(n):
    s = input().lower()    
    if s == 'a' or s == 'b' or s == 'c':
        #processamento da resposta Q1.
        if n == 1:
            if s == 'b':
                certo(0)
            else:
                certo(n)            
        #processamento da resposta Q2.
        if n == 2:
            if s == 'c':
                certo(0)
            else:
                certo(n)                
        #processamento da resposta Q3.
        if n == 3:
            if s == 'a':
                certo(0)
            else:
                certo(n)
        #processamento da resposta Q4.
        if n == 4:
            if s == 'c':
                certo(0)
            else:
                certo(n)
        #processamento da resposta Q5.
        if n == 5:
            if s == 'a':
                certo(0)
            else:
                certo(n)
        #processamento da resposta Q6.
        if n == 6:
            if s == 'a':
                certo(0)
            else:
                certo(n)
    else:        
        certo('n')
#processamento02 da resposta, respostas caso esteja certa ou errada
def certo(n):
    if n == 'n':
        print('Você não escolheu a, b ou c :(') 
    if n == 0:
        print('Isso mesmo, parabéns!!')
        global score
        score = scor(score)
    if n == 1:
        print("Errado, a alternatica correta é a letra 'b'. Pois, se você ultrapassa o segundo colocado, assume o lugar dele, ficando em segundo!")
    if n == 2:
        print("Errado, a resposta correta é 'c', se a mãe de Maria tem cinco filhas, então, podemos enumerar a prole da seguinte forma: \n1 - Fafá, 2 - Fefe, 3 - Fifi, 4 - Fofo e 5 - (mas não menos importante) MARIA.")
    if n == 3:
        print("Nãaaaao, a resposta correta é 'a', são as mesmas dez árvores vistas de diferentes perspectivas.\nNa ida, as árvores estavam à direita da mulher, mas na volta, quando ela estava no sentido contrário da rua, \nas plantas podiam ser vistas à esquerda.")
    if n == 4:
        print("Errado, a resposta correta é 'c', se a sala é um quadrado, logo, possui quatro cantos. \nE já sabemos que em cada um desses cantos há um gato, ou seja, quatro felinos estão na sala. \nPara confirmar essa ideia, ainda sabemos que cada um dos gatos consegue ver os outros três que estão na sala.")
    if n == 5:
        print("Errado, a resposta correta é 'a' zero, basta ler com atenção e interpretar o desafio: se Fábio foi sozinho até a padaria, então ninguém foi junto. \nEle apenas 'encontrou' uma série de seres pelo caminho.")
    if n == 6:
        print("Errado,  a resposta é 'a', se a borboleta vive cinco dias, ela terá morrido antes de uma semana (afinal, uma semana tem sete dias).\nNo entanto, se considerarmos seu tempo de vida, sabemos que, em cinco dias, ela voou 20 metros, pois 5 x 4 = 20.")
#função para incrementa a variável score, que conta os acertos        
def scor(x):
    x += 1
    return x
#função que classifica o desempenho
def pont(p):
    print(f'\n>>>Pontuação: você acertou {p} das 6 questões.')
    if p == 6:
        print('>>> Muito bem!!!')
    else:
        print('>>> tente novamente!!!')

def main():
    print('=' * 10 + 'desafio: Como eu fiz?' + '=' * 10)
    global score
    score = 0
    quiz()
    pont(score)
    print('\n>>>Obrigado por jogar!!S2 S2')

if __name__ == '__main__':
    main()
