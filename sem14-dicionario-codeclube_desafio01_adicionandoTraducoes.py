def desafio_AdicionandoTraducoes(sentence):
    textSpeakDictionary = {
        'rs' : 'risos',
        'tmb' : 'também',
        'vc' : 'você',
        'pq' : 'porque',
        'msm' : 'mesmo',
        'q' : 'que',
        'blz': 'beleza',
        'lgl' : 'legal',
        'rlx' : 'relaxa',
        'xau' : 'tchau',
        'qlqr': 'qualquer',
        'fzr' : 'fazer',
        'pd' : 'pode',
        's' : 'sim',
        'n' : 'não'
        }

    #obtém a frase  para tradução
    ##sentence = input('Insira uma frase para traduzir: ').lower()

    #divide a frase em uma lista de palavras
    wordsToTranslate = sentence.split()
    translatedSentence = ''

    #passa por cada palavra da lista
    for word in wordsToTranslate:
        #adiciona a palavra traduzida caso ela exista no dicionário
        if  word in textSpeakDictionary:
            translatedSentence += textSpeakDictionary[word] + ' '
        #mantém a palavra original caso não exista tradução
        else:
            translatedSentence += word + ' '
    #imprime a frase traduzida
    ##print('==>')
    ##print(translatedSentence)
    return translatedSentence


def etapa2_traduzindo_frases():
    textSpeakDictionary = {
        'rs' : 'risos',
        'tmb' : 'também',
        'vc' : 'você'
        }

    #obtém a frase  para tradução
    sentence = input('Insira uma frase para traduzir: ').lower()

    #divide a frase em uma lista de palavras
    wordsToTranslate = sentence.split()
    translatedSentence = ''

    #passa por cada palavra da lista
    for word in wordsToTranslate:
        #adiciona a palavra traduzida caso ela exista no dicionário
        if  word in textSpeakDictionary:
            translatedSentence += textSpeakDictionary[word] + ' '
        #mantém a palavra original caso não exista tradução
        else:
            translatedSentence += word + ' '
    #imprime a frase traduzida
    print('==>')
    print(translatedSentence)


def etapa1_traduzindo_palavras():
    textSpeakDictionary = {
        'rs' : 'risos',
        'tmb' : 'também'
        }

    #imprime o dicionário inteiro
    print('Dicionário = ', textSpeakDictionary)

    #imprime somente o conteúdo relacioando à chave 'rs'
    print('\nrs =', textSpeakDictionary["rs"])

    #texto que pede a entrada do usuário
    key = input('\nO que você gostaria de converter? : ')
    print(key, '=', textSpeakDictionary[key])
    

def main():
    #etapa1_traduzindo_palavras()
    #etapa2_traduzindo_frases()
    
    print(f'{"="*10}Traduzindo uma frase{"="*10}')
    frase = input('Insira uma frase para traduzir: ').lower()
    print(f'==>\n{desafio_AdicionandoTraducoes(frase)}')

    print(f'\n{"="*10}Traduzindo um bloco de frases{"="*10}')
    bloco = ()
    print('Insira as frase para serem traduzidas(Press 0 to stop): ')
    while True:
        frase = input('\>').lower()
        if frase == '0': break
        bloco += frase,        
    print('==>')   
    for frase in bloco:
        print(desafio_AdicionandoTraducoes(frase))
    
    
if __name__ == '__main__':
    main()
