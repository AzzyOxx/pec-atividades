#variável "lado_menor", do tipo float, recebe um valor a partir da leitura do teclado
lado_menor = float(input("Lado menor do terreno: "))

print(lado_menor)
a = int(input())

#variável "lado_maior", do tipo float, recebe um valor a partir da leitura do teclado
lado_maior = float(input("Lado maior do terreno: "))

print(lado_maior)
a = int(input())

#variável "area" recebe o valor da multiplicação entre os valores guardados  nas variáveis "lado_maior" e "lado_menor"
area = lado_menor * lado_maior

print(area)
a = int(input())

#variável "perimetro" recebe o valor do perimetro conforme a fórmula
perimetro = (2 * lado_menor) + (2 * lado_maior)

print(perimetro)
a = int(input())

#impresão do valor da "area" com uma formatação para melhor compreenssão
print(f'Área do terreno: {area}')
#impresão do valor da "perimetro" com uma formatação para melhor compreenssão
print(f'Perímetro do terreno: {perimetro}')
