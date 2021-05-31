from random import *

def nome_do_pet():
    nomes_femininos = ['Malu', 'Mika', 'Tantam', 'Bibinha', 'Soph', 'Hannah' ]
    nomes_masculinos = ['Tantam', 'Nagro', 'Mathaus', 'Pimpim', 'Bolinha', 'Brutos' ]
    
    executa = True
    while executa == True:
        print('''
menu
    s = sortear o nome
    a = adicionar nome
    d = remover nome
    p = imprimir nomes
    q = sair
    ''')
        #    
        menuChoice = input("\n>_").lower()
        #'s' para um sortear um nome
        if menuChoice == 's':
            escolhe_nome = True
            while escolhe_nome == True:
                print('''
Sexo do animal de estimação?
    f = feminino
    m = masculino''')
                sexo = input("\n>_").lower()
                if sexo == 'm':
                    print(f'Aqui está uma sugestão para um pet do sexo masculino:' )
                    print(f'Você deve chamar seu animal de estimação de {choice(nomes_masculinos)}.')
                    print("De nada!")
                    escolhe_nome = False
                    
                elif sexo == 'f':
                    print(f'Aqui está uma sugestão para um pet do sexo femino:' )
                    print(f'Você deve chamar seu animal de estimação de {choice(nomes_femininos)}.')
                    print("De nada!")
                    escolhe_nome = False
                else:
                    print('Você não informou o sexo do pet corretamente. Digite f para feminino ou m para masculino.')


        #'a' para adicionar nome
        elif menuChoice == 'a':
            escolhe_nome = True
            while escolhe_nome == True:
                print('''
Sexo do animal de estimação?
    f = feminino
    m = masculino''')
                sexo = input("\n>_").lower()
                nameToAdd = input('Adicione o nome: ').strip()
                ###
                tam_p = len(nameToAdd)
                itemToAdd = nameToAdd[0].upper()
                iii = 1
                while iii < tam_p:
                    itemToAdd += nameToAdd[iii].lower()
                    iii+=1
                itemToAdd = itemToAdd.strip()
                ###
                if sexo == 'm':
                    
                    #só adiciona um item se ele não estiver na lista
                    tam = len(nomes_masculinos)
                    i = 0
                    tem = False
                    while i < tam:
                        if itemToAdd.lower() == nomes_masculinos[i].lower():                            
                            tem = True
                        i += 1
                        
                    if tem != True:
                        nomes_masculinos.append(itemToAdd)                        
                    else:
                        print("O nome já está na lista!")
                    escolhe_nome = False
                   
                elif sexo == 'f':
                                        
                    #só adiciona um item se ele não estiver na lista
                    tam = len(nomes_femininos)
                    i = 0
                    tem = False
                    while i < tam:
                        if itemToAdd.lower() == nomes_femininos[i].lower():                            
                            tem = True
                        i += 1
                        
                    if tem != True:
                        nomes_femininos.append(itemToAdd)                        
                    else:
                        print("O nome já está na lista!")
                    escolhe_nome = False
                else:
                    print('Você não informou o sexo do pet corretamente. Digite f para feminino ou m para masculino.')

        #'d' para remover um hobby
        elif menuChoice == 'd':

            nameToDelete = input("Inserir o nome a ser removido: ")

            #primeira = itemToDelete[0].lower()
            tam_p = len(nameToDelete)
            itemToDelete = nameToDelete[0].upper()
            iii = 1
            while iii < tam_p:
                itemToDelete += nameToDelete[iii].lower()
                iii+=1
            itemToDelete = itemToDelete.strip() 
            #só remove um item se ele estiver na lista
            ###
            tem = False
            tam_f = len(nomes_femininos)
            i = 0
            while i < tam_f:
                if itemToDelete.lower() == nomes_femininos[i].lower():                            
                    nomes_femininos.remove(itemToDelete)
                    tem = True
                    break
                i += 1
                
            tam_m = len(nomes_masculinos)
            ii = 0
            while ii < tam_m:
                if itemToDelete.lower() == nomes_masculinos[ii].lower():                            
                    nomes_masculinos.remove(itemToDelete)
                    tem = True
                    break
                ii += 1
            if tem == False:
                print("O nome não está na lista!")
            ###
            '''
            if itemToDelete in hobbies:
                hobbies.remove(itemToDelete)
            else:
                print("O nome não está na lista!")
            '''
        #'p' para imprimir a lista de hobbies
        elif menuChoice == 'p':
            print(f'Nomes para pets machos:\n{nomes_masculinos}.\n')
            print(f'Nomes para pets fêmeas:\n{nomes_femininos}.\n')
        #'q' para sair
        elif menuChoice == 'q':

            executa = False
        else:
            print('Escolha uma opção válida!')
    
def main():
    print("Serviço de escolha de nome para animais de estimação")
    print("-"*53)

    nome_do_pet()   
            
if __name__ == '__main__':
    main()

