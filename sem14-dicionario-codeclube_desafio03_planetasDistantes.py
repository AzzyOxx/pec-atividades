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

distances = {
    1: ("mercúrio", 91700000),
    2: ("vênus", 41400000),
    3: ("marte", 78300000),
    4: ("júpiter", 628000000),
    5: ("saturno", 1280400000),
    6: ("urano", 2720400000),
    7: ("netuno", 4350400000)
    }

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
