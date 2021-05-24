from turtle import *

def figuras_planas():
    
    shape("turtle")
    speed(6)#
    import random
    pensize(1)
    i=0
    
    while i <= 250:
        #a = random.choice(["Blue", "Red", "Yellow", "Green", "Purple", "Brown", "Pink", "Orange"])
        #color(a)
        #f = random.randrange(1, 360)
        f = random.randrange(1, 360)
        g = random.randrange(1, 40)
        d = random.randrange(1, 2)
        e = random.randrange(1, 3)
        t = random.randrange(1, 50)
        pendown()
        if d == 1:
            right(f)
        if d == 2:
            left(f)
        if e == 1:
            penup()
        
        forward(t)
        i+= 1
    while i <= 250:
        #a = random.choice(["Blue", "Red", "Yellow", "Green", "Purple", "Brown", "Pink", "Orange"])
        #color(a)
        #f = random.randrange(1, 360)
        f = random.randrange(1, 360)
        g = random.randrange(1, 40)
        d = random.randrange(1, 2)
        e = random.randrange(1, 3)
        t = random.randrange(1, 50)
        pendown()
        if d == 1:
            right(f)
        if d == 2:
            left(f)
        if e == 1:
            penup()
        
        forward(t)
        i+= 1

        while i <= 250:
            #a = random.choice(["Blue", "Red", "Yellow", "Green", "Purple", "Brown", "Pink", "Orange"])
            #color(a)
            #f = random.randrange(1, 360)
            f = random.randrange(1, 360)
            g = random.randrange(1, 40)
            d = random.randrange(1, 2)
            e = random.randrange(1, 3)
            t = random.randrange(1, 50)
            pendown()
            if d == 1:
                right(f)
            if d == 2:
                left(f)
            if e == 1:
                penup()
            
            forward(t)
            i+= 1
    
    #levando para o topo esquerdo
    penup()
    backward(250)
    left(90)
    forward(150)
    
    #triangula
    pendown()
    right(90)
    color("Blue")
    pensize(10)
    a = 0
    tamtr = 117
    while a <= 35:
        ii = 0        
        while ii <= 2:
            if ii == 0:
                forward(tamtr)
                left(120)
                ii += 1
            elif ii == 1: 
                tamtr -= 1
                forward(tamtr)
                left(120)                
                ii += 1
            else:
                tamtr -= 1
                forward(tamtr)
                left(120)
                tamtr -= 1
                ii += 1
                
        speed(8)        
        a += 1
         
                
    right(90)
    forward(a-3)
    left(90)

    


        
           
    '''    
        
        
        
        p += 3
        #tamtr -= 1
        speed(1)
        left(90)
        forward(2)
        right(90)
        forward(2)
        i+=1
    '''
                
    

    #quadrado
    penup()
    #left(120)
    forward(150)
    pendown()
    i = 0
    while i <= 3:    
        forward(100)
        left(90)
        i+=1
    

    #pentágono
    penup()
    forward(150)
    pendown()
    i = 0
    while i <= 4:
        forward(65)
        left(72)
        i+=1
    
    
    #left(72)
    penup()
    backward(300)
    right(90)
    forward(200)
    
    
    
    
    
    
    

    
    '''
    color("Red")
    pensize(8)
    right(90)
    forward(100)
    left(90)
    forward(50)

    color("Orange")
    pensize(3)
    penup()
    forward(50)
    pendown()
    forward(50)
    '''
    
    #done()#
def casa():
    #triangulo
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
    left(120)
    right(90)
    forward(117)
    left(90)
    forward(117)
    left(90)
    forward(117)
    right(90)
    forward(298)
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
    forward(415)
    backward(900)
    
    
    
    

    
    
    

def main():
    
    figuras_planas()
    casa()
    done()

if __name__ == '__main__':
    main()
