#Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou 
#o valor booleano False (falso) caso contrário.

#função retorna valores booleanos caso seja impar(true) ou par(false)
def eh_impar(n):
    return n % 2 != 0

#processamento do valor recebido na função n
def par_ou_impar(n):
    if n == True:
        return 'ímpar'
    else:
        return 'par'

try:#função principal
    def main():
    
        #n = int(input())
        n = int(input('Digite um número: '))
        #variável 'c' que recebe o valor da função chamada eh_impar() 
        c = eh_impar(n)
        print(f'{n} é impar?? {c}')
        #imprimir na tela resultado final caso seja ímpar ou par
        #print(eh_impar(n))
        print(f'O número {n} é um número {par_ou_impar(c)}.')
    # função inicial
    if __name__ == '__main__':
        main()

#caso não seja inserido um número
except:
    print('Você não digitou um número! Por favor digite um número inteiro.')
    #chamando a função principal de novo, se as entradas não corresponderem ao esperado
    main()
