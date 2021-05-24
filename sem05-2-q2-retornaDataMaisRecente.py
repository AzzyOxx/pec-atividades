def data_mais_recente(d, m, a, d1, m1, a1):
    if a > a1:
        return d, m, a
    elif a < a1:
        return d1, m1, a1
    else:
        if m > m1:
            return d, m, a
        elif m < m1:
            return d1, m1, a1
        else:
            if d > d1:
                return d, m, a
            elif d < d1:
                return d1, m1, a1
            else:
                return d1, m1, a1
            
'''       
    #0 mais antigo, 1 mais recente
    # a = 0, a1 = 1
    if a <= a1: #sim
        if m < m1
            return d1 , m1 , a1
        elif m > m1:
            return d , m, a
        elif
        sei la
        elif a < a1 and m < m1:
            return d , m , a
        elif a 
        if d < dn and m < mn and a < a1:
            return d , m , a
        elif d > dn and m <
        else:
            return a - and
        sei la
    else:
        return d , m , a
'''

def main():
    
    dd1 = int(input('dia da primeira data: \n'))
    mm1 = int(input('mês da primeira data: \n'))
    yy1 = int(input('ano da primeira data: \n'))

    dd2 = int(input('dia da segunda data: \n'))
    mm2 = int(input('mês da segunda data: \n'))
    yy2 = int(input('ano da segunda data: \n'))
    
    a, b, c = data_mais_recente(dd1, mm1, yy1, dd2, mm2, yy2)
    
    print(f'{a}/{b}/{c}')
    

if __name__ == '__main__':
    main()
'''
#a é mais recente ou o mesmo ano que a1??
    #se sim, então 
se a <= a1:
    SE m1 < m:
        return 
    a é menos recente ou mesmo ano

se não:
    a é mais recente

professor, gostaria de sugerir que coloque pelo menos ums exemplo de entrada e saída em cada questão
'''
