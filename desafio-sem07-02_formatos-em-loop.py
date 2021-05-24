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
    pendown()
    for cont in range(360):        
        forward(1)
        left(1)
        
def main():
    
    posicionando()#linha 4
    pentagono()#linha 20
    espaco()#linha 16
    hexagono()#linha 26
    espaco()#linha 16
    circulo()#linha 32
    
    done()

if __name__ == '__main__':
    main()
