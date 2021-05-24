def imc(p, a):
    return p / (a**2)


def class_imc(m):
    if m < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= m < 25:
        return 'Peso normal'
    elif 25 <= m < 30:
        return 'Sobrepeso'
    elif 30 <= m < 35:
        return 'Obeso leve'
    elif 35 <= m < 40:
        return 'Obeso moderado'
    else:
        return 'Obeso mórbido'
    

def main():
    ps = float(input('peso: '))
    at = float(input('altura: '))
    m = imc(ps, at)
    print(m)
    print(class_imc(m))


if __name__ == '__main__':
    main()
