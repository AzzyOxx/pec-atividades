#Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. Considere exatamente: 
#Áries (21/03 a 19/04); Touro (20/04 a 20/05); Gêmeos (21/05 a 21/06); Câncer (22/06 a 22/07); Leão (23/07 a 
#22/08); Virgem (23/08 a 22/09); Libra (23/09 a 22/10); Escorpião (23/10 a 21/11); Sagitário (22/11 a 21/12); 
#Capricórnio (22/12 a 19/01); Aquário (20/01 a 18/02); Peixes (19/02 a 20/03);

def t_sig(a):
    if a == 1:
        return 'Aquário'
    elif a == 2:
        return 'Peixes'
    elif a == 3:
        return 'Áries'
    elif a == 4:
        return 'Touro'
    elif a == 5:
        return 'Gêmeos'
    elif a == 6:
        return 'Câncer'
    elif a == 7:
        return 'Leão'
    elif a == 8:
        return 'Virgem'
    elif a == 9:
        return 'Libra'
    elif a == 10:
        return 'Escorpião'
    elif a == 11:
        return 'Sagitário'
    else:
        return 'Capricórnio'
    

def sig(d, m ):
    if m == 1:
        if d >= 20:
            print(t_sig(1))
        else:
            print(t_sig(12))
    elif m == 2:
        if d <= 18:
            print(t_sig(1))
        else:
            print(t_sig(2))            
    elif m == 3:
        if d <= 20:
            print(t_sig(2))
        else:
            print(t_sig(3))            
    elif m == 4:
        if d <= 19:
            print(t_sig(3))
        else:
            print(t_sig(4))
    elif m == 5:
        if d <= 20:
            print(t_sig(4))
        else:
            print(t_sig(5))
    elif m == 6:
        if d <= 21:
            print(t_sig(5))
        else:
            print(t_sig(6))
    elif m == 7:
        if d <= 22:
            print(t_sig(6))
        else:
            print(t_sig(7))
    elif m == 8:
        if d <= 22:
            print(t_sig(7))
        else:
            print(t_sig(8))
    elif m == 9:
        if d <= 22:
            print(t_sig(8))
        else:
            print(t_sig(9))
    elif m == 10:
        if d <= 22:
            print(t_sig(9))
        else:
            print(t_sig(10))
    elif m == 11:
        if d <= 21:
            print(t_sig(10))
        else:
            print(t_sig(11))
    elif m == 12:
        if d <= 21:
            print(t_sig(11))
        else:
            print(t_sig(12))    

def main():
    
    dd = int(input('dia que você nasceu: \n'))
    mm = int(input('mês que você nasceu: \n'))
    

    
    sig(dd, mm)
    
if __name__ == '__main__':
    main()


