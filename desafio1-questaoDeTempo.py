"""
print("no Python, qual é o nome )

Print()
print(":)" *100)
voce tem 3 chances para tentar adivinha qa nuero rá srtead e 1 10
"""
pont = 0
s = int(input("Quantas copas do mundo a seleção brasileira já conquistou? "))
if s == 5:
    print("Parabens você acertou!!\n:) :) :)\n")
    pont += 1
else:
    print("Que pena, você errou!!!\n:( :( :(\n")

s = int(input("Em que ano Pedro Álvares Cabral descobriu o Brasil?? "))
if s == 1500:
    print("Parabens você acertou!!\n:) :) :)\n")
    pont += 1
else:
    print("Que pena, você errou!!!\n:( :( :(\n")

s = input("Qual foi o campeão do brasileirão 2020? ")
if s == 'flamengo':
    print("Parabens você acertou!!\n:) :) :)")
    pont += 1
else:
    print("Que pena, você errou!!!\n:( :( :(")
print(f'Sua pontuação: {pont}/3.')

print("="*50)
print("Bônus: Jogo da forca\n")
a1 , a2, a3, a4, a5, = "_", "_", "_", "_", "_"
print(">>> Palavra: ",a1 , a2, a3, a2, a4, a5, a2)
palavra = 'a'
while palavra != 'laranja':
    d = input('\nDigite uma letra(apenas minúscula): ')
    if d == 'l' or d == 'a' or d == 'r' or d == 'n' or d == 'j':
        print(":)"*4)
        print('muito bem!!')
        if d == 'l':
            a1 = 'l'
        if d == 'a':
            a2 = 'a'
        if d == 'r':
            a3 = 'r'
        if d == 'n':
            a4 = 'n'
        if d == 'j':
            a5 = 'j'
    else:
        print(":(" *4 )
        print("Não foi nessa vez!!")
    print("\n>>> Palavra: ",a1, a2, a3, a2, a4, a5, a2)
    palavra = a1+a2+a3+a2+a4+a5+a2

print("Parabens, você acertou a palavra!!")
fim = input()
