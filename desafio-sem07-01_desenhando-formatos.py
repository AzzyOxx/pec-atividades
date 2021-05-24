from turtle import *

# essa função desenha um triangulo, um quadrado e um pentágono
def figuras_planas():
    #definindos propriedades da 'caneta'
    shape("turtle")
    pensize(8)
    speed(6)    
    
    #levando a "caneta" para o topo esquerdo
    penup()
    backward(250)
    left(90)
    forward(150)
    
    #triangulo
    color("Blue")
    pendown()
    right(90)
    i = 0
    while i <= 2:
        forward(117)
        left(120)
        i+=1    

    #quadrado
    penup()
    color("Red")
    forward(150)
    pendown()
    i = 0
    while i <= 3:    
        forward(100)
        left(90)
        i+=1
    
    #pentágono
    penup()
    color("Yellow")
    forward(150)
    pendown()
    i = 0
    while i <= 4:
        forward(65)
        left(72)
        i+=1
    
    #posicionando a "caneta em uma área abaixo dos desenhos já feitos"
    penup()
    backward(300)
    right(90)
    forward(200)    
    
def casa():
    #triangulo
    color("Brown")
    pendown()
    left(90)
    i = 0
    while i <= 2:
        forward(117)
        left(120)
        i+=1
        
    #telhado    
    forward(415)
    left(120)
    forward(117)
    left(60)
    forward(298)
    left(60)
    forward(117)

    #paredes
    color("Yellow")
    left(120)
    right(90)
    forward(117)
    left(90)
    forward(117)
    left(90)
    forward(117)
    right(90)
    color("Brown")
    forward(298)
    color("Yellow")
    right(90)
    forward(117)
    right(90)

    #porta
    forward(160)
    right(90)
    forward(80)
    right(90)
    forward(45)
    right(90)
    forward(80)
    right(90)
    forward(298-(160-45))

    #chão
    color("Green")
    forward(415)
    backward(900)
    
def main():
    figuras_planas()#linha 4
    casa()#linha 54
    
    done()

if __name__ == '__main__':
    main()
