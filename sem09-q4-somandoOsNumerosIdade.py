'''
03. O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um 
programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8 
dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989 
e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).
'''

def numero_da_sorte(idade):
    i = 0
    total = 0    
    while i <= (len(idade)-1):
        cont = int(idade[i])
        total += cont
        i += 1
    return total

def main():
    idade = input('Idade: ').strip()
    print(f'O número {numero_da_sorte(idade)} é o seu número da sorte!!')
    
if __name__ == '__main__':
    main()

