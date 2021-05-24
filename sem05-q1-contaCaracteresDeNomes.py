# Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “C” para casado e “S” para 
# solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) 
# nome(s) lido(s).

'''
def main():
    nome = input('Seu nome: ').strip()
    est_civil = input('Seu estado civil:(S- solteiro / C - casado) ').strip().lower()
    if est_civil == 'c':
        nome2 = input('Nome do cônjuge: ').strip()
        nome = nome + nome2
    print(len(nome))

if __name__ == '__main__':
    main()
'''

def main():
    
    nome = input('Seu nome: ').strip()
    #nome = input()#.strip()

    est_civil = input('Seu estado civil:(S- solteiro / C - casado) ').strip().lower()
    #est_civil = int(input())
    if est_civil == 1:

        nome2 = input('Nome do cônjuge: ').strip()
        #nome2 = input()#.strip()
        nome = nome + nome2
    print(len(nome))
    
if __name__ == '__main__':
    main()
