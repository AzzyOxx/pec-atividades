'''
01.Crie um dicionário e armazene nele os dados de livros: título, isbn, autor e preço. A chave do dicionários será um 
código numérico e sequencial, gerado automaticamente, iniciando pelo número 101 (cento e um). A leitura de uma 
descrição vazia para o título finaliza a leitura. Imprima todos os dados usando o padrão “Nome do Campo: valor”.
Por exemplo:
        Código: 101
        Título: Programação Java para a Web - 1ª Edição
        ISBN: 978-85-7522-238-6
        Autor: Décio H. Luckow
        Preço: 99.00
        ...
        Código: 114
        Título: Novelas, Espelhos e um Pouco de Choro
        ISBN: 85-7480-052-X
        Autor: Thelma Guedes
        Preço: 52.00
'''

#criando o dicionário com as informações dos livros
def recebeDadosLivros():
    livros = {}
    key = 100
    while True:
        key += 1
        title = input().strip()
        if title == '': break 
        isbn = input().strip()
        author = input().strip()
        price = float(input())
        livros[key] = (title, isbn, author, price)

    return livros


def main():
    #entrada
    biblioteca = recebeDadosLivros()

    #saída
    for livro in biblioteca:
        print(f'Código: {livro}')
        print(f'Título: {biblioteca[livro][0]}')
        print(f'ISBN: {biblioteca[livro][1]}')
        print(f'Autor: {biblioteca[livro][2]}')
        print(f'Preço: {biblioteca[livro][3]:.2f}')

if __name__ == '__main__':
    main()
