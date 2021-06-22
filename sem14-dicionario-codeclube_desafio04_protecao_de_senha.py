distances = {
    1: ("mercúrio", 91700000),
    2: ("vênus", 41400000),
    3: ("marte", 78300000),
    4: ("júpiter", 628000000),
    5: ("saturno", 1280400000),
    6: ("urano", 2720400000),
    7: ("netuno", 4350400000)
    }


def displayMenu():
    print(f"{'='*13}Planetas distantes{'='*13}")
    print("=" * 44)
    print("Menu:")
    print('Escolha qual planeta você deseja saber a distância até nós:')
    print("  1 = Mercúrio")
    print("  2 = Vênus")
    print("  3 = Marte")
    print("  4 = Júpiter")
    print("  5 = Saturno")
    print("  6 = urano")
    print("  7 = Netuno")
    print("  q = sair")

def planetas_distantes():
    running = True

    displayMenu()

    #repete até que o usuário digite 'q' para sair
    while running == True:

        menuChoice = input(">_").lower()
        
        if menuChoice in '1234567':
            print(f'{distances[int(menuChoice)][0]} tá a {distances[int(menuChoice)][1]} km da Terra.')
            
        #q para sair
        elif menuChoice == 'q':
            running = False

        else:
            print("Escolha inválida!")


passwordDictionary = {
        "programador" : "acesso"    
    }

def main():
    
    print("Programa super secreto")
    print("====================")

    loginAttempts = 0
    while loginAttempts < 3:
        print('Login:')
        name = input("Nome : ").lower()
        password = input("Senha : ").lower()

        if name in passwordDictionary and passwordDictionary[name] == password:
            print("\nBEM-VINDO sr.", name.upper(),'!!')
            print('Acesso liberado ao programa "Planetas Distantes"!!\n')
            planetas_distantes()

        else:
            loginAttempts += 1
            print(f"Acesso negado :(\n({loginAttempts}/3 tentativas).\n")
    print('Acesso negado. Parece que você não possui cadastro no sistema.')            
if __name__ == '__main__':
    main()
