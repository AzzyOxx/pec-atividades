from turtle import *

#essa função leva a "caneta" pro topo esquerdo e define algumas propriedades da mesma
def posicionando():
    shape("turtle")
    pensize(6)
    speed(11)
    color("Red")

    #levando para o topo esquerdo
    penup()
    backward(250)
    left(90)
    forward(150)
    right(90)

#essa função faz um espaçamento à direita
def espaco():
    penup()
    forward(250)

#essa função desenha algo que lembra uma flor
def flor():
    color("Red")
    pensize(5)
    pendown()
    for cont in range(36):        
        forward(100)
        left(100)

#essa função desenha algo que lembra uma sol   
def sol():
    color("Yellow")
    pensize(1)
    pendown()
    i = 0
    g = 0    
    for cont in range(220):        
        forward(i)
        left(g)
        i += 1
        g+=1

#essa função desenha algo que lembra uma flor        
def flor2():    
    color("Pink")
    pensize(1)
    pendown()
    for cont in range(8):
        for cont in range(360):
            pendown()
            forward(1)
            left(1)
        penup()
        left(45)
        forward(80)
       
def main():
    posicionando()#linha 4
    flor()#linha 23
    espaco()#linha 18
    sol()#linha 32

    #ajustando a posição da "caneta" 
    penup()
    forward(280)    
    left(30)
    
    flor()#linha 23

    #levando a "caneta" para uma área abaixo dos desenhos já feitos
    penup()
    backward(450)
    right(90)
    forward(280)
    left(90)
    forward(280)
    
    flor2()#linha 45
    
    done()

if __name__ == '__main__':
    main()
