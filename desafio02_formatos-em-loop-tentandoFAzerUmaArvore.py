from turtle import *

#essa função leva a "caneta" pro topo esquerdo e define algumas propriedades da mesma
def posicionando():
    shape("turtle")
    pensize(5)
    speed(11)
    #levando para o topo esquerdo
    penup()
    backward(250)
    left(90)
    forward(150)
    right(90)

#essa função faz um espaçamento à direita    
def espaco():
    penup()
    forward(200)
    
def pentagono():
    pendown()
    for cont in range(5):        
        forward(80)
        left(72)
    
def hexagono():
    pendown()
    for cont in range(6):        
        forward(70)
        left(60)
        
def circulo():
    pensize(1)
    pendown()
    n = 0
    d=0
    while d < 3:
        for cont in range(360):
            n+=1
            #d = n
            #d += d * 100
            forward(n*0.01)
            right(fibonacci(n)*0.001)
            #forward((fibonacci(cont)/1000))
            #right(1/1000)
        d += 1
    
        
def fibonacci(n):
    fib = 0
    f1= 0
    f2 = 1
    while n-1 > 0:        
        fib = f1 + f2
        #print(fib ,end = ',')
        f2 = f1
        f1 = fib
        n -= 1
    return fib
'''
def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == '__main__':
    main()
'''
def main():
    
    posicionando()#linha 4
    #pentagono()#linha 20
    #espaco()#linha 16
    #hexagono()#linha 26
    #espaco()#linha 16
    circulo()#linha 32
    #espaco()
    #fibonacci(360)
    done()

if __name__ == '__main__':
    main()
