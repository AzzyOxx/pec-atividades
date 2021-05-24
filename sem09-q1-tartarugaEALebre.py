'''
01. A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair n sua frente. 
A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto. Faça um programa que 
leia quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até que a lebre alcance 
a tartaruga. Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.
'''


def lebre_passaCoelhinho(vantagem):
    dist_coelho = vantagem
    dist_lebre = 0
    mnts = 0
    while dist_lebre < dist_coelho:#<=
        dist_coelho += 1
        dist_lebre += 10
        mnts += 1
    return mnts, dist_coelho, dist_lebre
        
def main():
    dist_coelho = float(input('Quantos metros a tartaruga saiu na frente? '))
    #dist_coelho = float(input())
    mnts, dist_coelho2, dist_lebre = lebre_passaCoelhinho(dist_coelho)
    
    print(f'Com essa vantagem, a lebre vai precisar de {mnts} minuto(s), após o início da corrida, para alcançar a tartaruga.')

if __name__ == '__main__':
    main()
