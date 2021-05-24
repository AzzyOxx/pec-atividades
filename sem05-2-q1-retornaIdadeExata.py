def idade(d, m, a, dn, mn, an):
    if d < dn and m <= mn and a > an:
        return (a - an) - 1
    elif d >= dn and m >= mn and a > an:
        return a - an
    else:
        return 0
    
   
    


def main():
    
    try:
        dd = int(input('Que dia é hoje?\n'))
        mm = int(input('Em que mês estamos?\n'))
        yy = int(input('Em que ano estamos?\n'))

        d_nasc = int(input('Em que dia você nasceu?\n'))
        m_nasc = int(input('Em que mês você nasceu?\n'))
        a_nasc = int(input('Em que ano você nasceu?\n'))
        
        d = idade(dd, mm, yy, d_nasc, m_nasc, a_nasc)
        
        print(d)
    except:
        print()

if __name__ == '__main__':
    main()
