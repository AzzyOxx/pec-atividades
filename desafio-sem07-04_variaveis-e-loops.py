from turtle import *
import random

def posicionando():
    shape("turtle")
    pensize(5)
    speed(11)

    #levando para o topo esquerdo
    penup()
    backward(450)
    left(90)
    forward(150)
    right(90)

def espaco():
    penup()
    forward(200)
    
def figuras_planas():
    lado = 3
    tam = 100
    for cont in range(5):
        a = random.choice(["Blue", "Red", "Yellow", "Green", "Purple", "Brown", "Pink", "Orange"])
        color(a)
        pendown()        
        angulo = 360 / lado
        for cont in range(lado):        
            forward(tam)
            left(angulo)
        tam -= 15
        espaco()
        lado += 1
        
    pendown()
    a = random.choice(["Blue", "Red", "Yellow", "Green", "Purple", "Brown", "Pink", "Orange"])
    color(a)
    for cont in range(360):        
        forward(1)
        left(1)
           
def main():
    posicionando()
    figuras_planas()
    
    done()

if __name__ == '__main__':
    main()
