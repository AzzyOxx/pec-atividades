'''
02. Escreva um programa que, para um número indeterminado de pessoas:
    a. leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag) 
    e não deve ser considerada;
    b. calcule e escreva o número de pessoas;
    c. calcule e escreva a idade média do grupo;
    d. calcule e escreva a menor idade e a maior idade.
'''

def media_idade(lista, pessoas):
    i = pessoas - 1
    #print(i)
    soma = 0
    while i >= 0:
        soma += lista[i]
        i -= 1        
        
    return soma / pessoas

def maior_menor(lista, tam):
    i = tam - 1
    maior = 0
    menor = lista[i]

    while i >= 0:
        if lista[i] > maior:
            maior = lista[i]
        if lista [i] < menor:
            menor = lista[i]
        i -= 1

    return maior, menor
    
    
def main():
    lista = []
    pessoas = 0
    while True:
        idade = int(input('Digite a idade de alguém: '))
        if idade == 0 : break
        else:
            lista.append(idade)
            pessoas += 1
    if pessoas != 0:    
        media = media_idade(lista, pessoas)
        maior, menor = maior_menor(lista, pessoas)
        #print(lista)
        #print(pessoas, media, maior, menor)
        print(f'O número de idades inseridas foi: {pessoas}.')
        print(f'A idade média do grupo é: {media:.2f} anos.')
        print(f'A menor idade inserida foi: {menor}.')
        print(f'A maior idade inserida foi: {maior}.')
        
    else:
        pass

if __name__ == '__main__':
    main()

    '''
    total = 0
    media_idade = 0
    pessoas = 0
    maior_idade = 0
    menor_idade = 0
    
    while True:
        idade = int(input())
        if idade == 0: break
        else:
            total += idade
            pessoas += 1

            if pessoas == 1:
                menor_idade = idade
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                    menor_idade = idade
    
    media_idade = total / pessoas

    print(pessoas, media_idade, maior_idade, menor_idade )
    '''

'''
lista = ['o carro', 'peire', 123, 111]
>>> lista
['o carro', 'peire', 123, 111]
>>> nova_lista = ['pedra', lista]
>>> nova_lista
['pedra', ['o carro', 'peire', 123, 111]]
>>> lista[0]
'o carro'
>>> lista[2]
123
>>> lista[0,1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lista[0,1]
TypeError: list indices must be integers or slices, not tuple
>>> lista[0][1]
' '
>>> nova_lista[1][2]
123
'''
