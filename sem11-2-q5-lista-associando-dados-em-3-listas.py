'''
5. Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais
alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a 
altura arredondando para duas casas decimais.
'''

def recebedados30():
    num = 30##
    nome = []
    idade = []
    altura = []
    cont = 0
    while cont < num:
        nome_paraInserir =input('Nome do(a) aluno(a): ').strip()
        idade_paraInserir = int(input(f'Idade do(a) {nome_paraInserir}: '))
        altura_paraInserir = float(input(f'Altura do(a) {nome_paraInserir}: '))
        nome.append(nome_paraInserir)
        idade.append(idade_paraInserir)
        altura.append(round(altura_paraInserir, 2))        
        cont += 1
    return nome, idade, altura

def media_aritimetrica(lista):
    tam = len(lista)
    i = 0
    total = 0
    while i < tam:
        total += lista[i]
        i += 1
    return round(total/tam,2)

def alunosMenores(media_alturas, nomes, idades, alturas):
    Nomes_abaixoDaMedia = []
    alturas_abaixoDaMedia = []
    idade_doAluno = []
    tam = len(nomes)
    i = 0
    total = 0
    while i < tam:
        if idades[i] > 13:
            if alturas[i] < media_alturas:
                Nomes_abaixoDaMedia.append(nomes[i])
                alturas_abaixoDaMedia.append(alturas[i])
                idade_doAluno.append(idades[i])
        i += 1
    return Nomes_abaixoDaMedia, alturas_abaixoDaMedia, idade_doAluno
                
def acima_da_media(media, nomes, alturas):
    Nomes_acimaDaMedia = []
    alturas_acimaDaMedia = []
    tam = len(alturas)
    i = 0
    total = 0
    while i < tam:
        if alturas[i] > media:
            Nomes_acimaDaMedia.append(nomes[i])
            alturas_acimaDaMedia.append(alturas[i])
        i += 1
            
    return Nomes_acimaDaMedia, alturas_acimaDaMedia

    
def main():
    nome_alunos, idade_alunos, altura_alunos = recebedados30()
    media_alturas = media_aritimetrica(altura_alunos)
    nome_maior_de13_inferiroAmediaAlt, altura_maior_de13_inferiroAmediaAlt, idade_maior_de13_inferiroAmediaAlt = alunosMenores(media_alturas, nome_alunos, idade_alunos, altura_alunos )
    '''
    print(f'lista dos nomes dos alunos: {nome_alunos}')
    print(f'lista das idades dos alunos: {idade_alunos}')
    print(f'lista das alturas dos alunos: {altura_alunos}')
    print(f'Média das alturas: {media_alturas}')
    print(f'lista dos nomes dos alunos abaixo da média: {nome_maior_de13_inferiroAmediaAlt}')
    print(f'lista das idades dos alunos abaixo da média: {idade_maior_de13_inferiroAmediaAlt}')
    print(f'lista das alturas dos alunos abaixo da média: {altura_maior_de13_inferiroAmediaAlt}')
    
    '''
    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    #print(f'{nome_alunos}')
    #print(f'{idade_alunos}')
    #print(altura_alunos)
    #print(media_alturas)
    tam = len(nome_maior_de13_inferiroAmediaAlt)
    i = 0
    total = 0
    while i < tam:
        print(nome_maior_de13_inferiroAmediaAlt[i])
        #print(f'{atletas_acima_da_mediaAlturas[i]:.2f}')
        i += 1
    
    #print(nome_maior_de13_inferiroAmediaAlt)
    #print(altura_maior_de13_inferiroAmediaAlt)
    #print(idade_maior_de13_inferiroAmediaAlt)
    
    
if __name__ == '__main__':
    main()
