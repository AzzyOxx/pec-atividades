'''
02.Crie um programa que, usando dicionário, crie uma agenda de tamanho fornecido inicialmente pelo usuário. Leia os 
dados de todos os contatos do usuário (nome, cidade, estado, telefone) de forma que a agenda fique completa e por 
fim imprima todos os contatos. Crie um código numérico sequencial para usar como chave do dicionário.
'''

def cria_agenda(qntd):
    contatos = {}
    for pessoa in range(qntd):
        nome = input().strip()
        cidade = input().strip()
        estado = input().strip()
        telefone = input().strip()
        contatos[pessoa] = (nome, cidade, estado, telefone)
    return contatos
    
def main():
    #entrada
    qntd_contatos = int(input())
    agenda_telefonica = cria_agenda(qntd_contatos)

    #saída
    for contato in agenda_telefonica:
        print(f'{agenda_telefonica[contato][0]:<25}{agenda_telefonica[contato][1] + "(" + agenda_telefonica[contato][2] + ")":<30}{agenda_telefonica[contato][3]}')
        
if __name__ == '__main__':
    main()
