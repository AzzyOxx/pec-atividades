'''
#outra forma de fazer...
def ident(n, s):
    if s == 1:
        print(f'Ilmo Sr. {n}')
    elif s == 2:
        print(f'Ilma Sra. {n}')
    else:
        print('Você não digitou um valor válido!!')
        
def main():
    try:
        n = input('Qual é o seu nome?\n').strip()
        s = int(input("Qual é o seu sexo?(1 = masc ou 2 = fem)\n"))
        ident(n, s)
    except:
        print('Você não digitou um valor válido!!')
    
if __name__ == '__main__':
    main()
'''
#Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome prece)dido da mensagem “Ilmo 
# Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro 
# 1 para identificar masculino e 2 para identificar feminino.


#função que processa as entradas
def ident(n, s):
    #caso seja masculino
    if s == 1:
        print(f'Ilmo Sr. {n}')
    #caso seja feminino
    elif s == 2:
        print(f'Ilma Sra. {n}')
    #caso digite um int diferente de 1 ou 2
    else:
        print('Você não digitou um valor válido!!')
        #chamando a função principal de novo, se as entradas não corresponderem ao esperado
        main()

try:
    # função principal
    def main():
        n = input('Qual é o seu nome?\n').strip()
        s = int(input("Qual é o seu sexo?(1 = masc ou 2 = fem)\n"))
        #chamando a função de processamento
        ident(n, s)

    # função inicial
    if __name__ == '__main__':
        main()
#caso seja inserido um valor inválido
except:
    print('Você não digitou um valor válido!!')
    #chamando a função principal de novo, se as entradas não corresponderem ao esperado
    main()

