'''
Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais 
telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes opções:
    1 - Incluir Novo Nome
    2 - Incluir Telefone
    3 - Excluir Telefone
    4 - Excluir Nome
    5 - Mostrar Agenda
    0 - Fim do Programa
    ========================
    Digite sua opção:

incluir_novo_nome: acrescenta um nome novo na agenda, com um ou mais telefones. Ela deve receber como 
argumentos o nome e os telefones.
incluir_telefone: acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, 
você deve perguntar se a pessoa deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o 
novo nome.
excluir_telefone: exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, 
ela deve ser excluída da agenda.
excluir_nome: exclui uma pessoa da agenda. 
mostrar_agenda: essa função mostra todos os nomes e telefones na agenda.
'''

def mostrar_agenda():
    for cont in agenda:
        print(f'Nome: {cont}')
        print(f'  Telefone(s):')
        qntd_num = 1
        for num in agenda[cont]:
            print(f'    {qntd_num}. {num}')
            qntd_num += 1
    
def excluir_nome():
    nome = input().strip()
    if nome in agenda:
        del agenda[nome]
    else:
        print(f'{nome} não está na agenda.')
        
def excluir_telefone():
    nome = input().strip()
    telefone = input().strip()
    nao_excluir = []
    if nome in agenda:
        for cont in agenda[nome]:
            if cont != telefone:
                nao_excluir.append(cont)
        agenda[nome] = nao_excluir

def incluir_telefone():
    nome = input().strip()
    fone = input().strip()
    if nome in agenda:
        agenda[nome].append(fone)
    else:
        adicionar = input().lower().strip()
        if adicionar == 's':
            agenda[nome] = [fone]

def incluir_novo_nome():
    nome = input().strip()
    fone = input().strip()
    if nome not in agenda:
        agenda[nome] = [fone]
    else:
        print('Nome já existe na agenda.')

agenda = {}

def main():
    running = True
    #repete até que o usuário digite 'q' para sair
    while running == True:
    
        menuChoice = int(input())
        
        #1 para incluir novo nome
        if menuChoice == 1:
            incluir_novo_nome()

        #2 para incluir telefone
        elif menuChoice == 2:
            incluir_telefone()

        #3 para excluir telefone
        elif menuChoice == 3:
            excluir_telefone()

        #4 para excluir nome
        elif menuChoice == 4:
            excluir_nome()

        #5 para mostrar agenda
        elif menuChoice == 5:
            mostrar_agenda()
            
        #0 para sair
        elif menuChoice == 0:
            running = False

        

if __name__ == '__main__':
    main()
