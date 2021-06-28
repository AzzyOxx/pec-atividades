'''
01.Escreva um programa que leia um texto e calcula a frequência relativa de cada letra no texto. Desconsidere a 
diferença entre maiúsculas e minúsculas mas considere caracteres acentuados. Por exemplo, para a frase:
Se, a princípio, a ideia não é absurda, então não há esperança 
para ela. (Albert Einstein)
Retorna o dicionário:
{'S': 4, 'E': 10, 'A': 15, 'P': 4, 'R': 5, 'I': 7, 'N': 7, 'C': 
2, 'O': 4, 'D': 2, 'B': 2, 'U': 1, 'T': 3, 'H': 1, 'L': 2}
'''

def conta_caracteres(frase):
    aparece_caractere = {}
        
    for char in frase:#corre todos os caracteres da frase
        keys = list(aparece_caractere.keys())#atualiza a quantidade de chaves
        if char in keys:
            aparece_caractere[char] = aparece_caractere[char] + 1

        if char not in keys:
            
            aparece_caractere[char] = int(1)

    return aparece_caractere


def retira_acentuacao(sentence):
    for char in sentence:
        if char in 'áàâã':
            sentence = sentence.replace(char,'a')
        if char in 'éê':
            sentence = sentence.replace(char,'e')
        if char in 'í':
            sentence = sentence.replace(char,'i')
        if char in 'óôõ':
            sentence = sentence.replace(char,'o')
        if char in 'úü':
            sentence = sentence.replace(char,'u')
        if char in 'ç':
            sentence = sentence.replace(char,'c')

    return sentence.upper()

    
def retira_pontucao(sentence):
    #remove a pontuação da frase
    for char in ' ?!.,()-_":':
        sentence = sentence.replace(char,'')

    sentence = retira_acentuacao(sentence.lower())
    
    return sentence


def main():
    #entrada
    frase = input('Digite uma frase: ').upper().strip()#caixa alta
    
    #processamento
    frase_sem_pontuacao_ou_acento = retira_pontucao(frase)
    caracteres = conta_caracteres(frase_sem_pontuacao_ou_acento)
    print('Frequência relativa de cada letra no texto: ')
    print(caracteres)

if __name__ == "__main__":
    main()
