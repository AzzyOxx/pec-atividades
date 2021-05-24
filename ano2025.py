print("-"*7 + "Antes de mais nada; Desculpe as gambiarras professor!!! :):):)" + "-"*7)
print("Professor, ainda não deu pra entregar pelo git.\nEspero que possa considerar.:) :)\n\n")
#print("--------Digite 0(zero) para encerrar--------\n\n")

a = 1
while a != 0:
    print('''Escolha o número da página do desafio a ser corrigida: 
         3 (Desafio: Dinheiro no bolso)
         4 (Desafio: Mudando datas)
         8.1 (Desafio: O ano 3000!)
         8.2 (Desafio: Sua idade em anos de cachorro)
    ''')
    b=float(input("= "))
    if b == 3:
        print("-"*15 + "Desafio: Dinheiro no bolso" + "-"*15)
        #print(f'\n\nCobrando R$ 12,50 por lavagem, 8 carros totalizariam R$ {8*12.5} reais!\n\n')
        print("\n\nCobrando R$ 12,50 por lavagem, 12 carros totalizariam R$ %.2f reais!!\n\n"%(12*12.5))

    if b == 4:
        print("-"*15 + "Desafio: Mudando datas" + "-"*15)

        print(f'\nUma pessoa nascida em 1998 terá {2025-1998} anos em 2025.\n')
        print(f'Por fim, uma pessoa nascida hoje, 28/03/2021, completará {2050-2021} anos no dia 28/03/2050.\n')

        
    if b == 8.1:
        print("-"*15 + "Desafio: O ano 3000!" + "-"*15)
        ano1= int(input("\nEm que ano você nasceu?\n"))
        ano2= int(input("Para qual ano você quer saber sua idade?\n"))
        idade = ano2 - ano1
        print(f'No ano {ano2} você terá {idade} anos!\n')
        

    if b == 8.2:
        print("-"*15 + "Desafio: Sua idade em anos de cachorro" + "-"*15)

        ano1 = int(input("\nQuantos anos você tem?\n"))
        print(f'Se você fosse um cachorro, você teria {7*ano1} anos!!')

        print('''
  '0'_____'
     || ||
        ''')

              
        
    print("="*60)
    print('Continuar? (0 = não)')
    a=int(input("="))


