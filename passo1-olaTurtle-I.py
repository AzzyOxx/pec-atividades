from turtle import *

def tartaruga():
    
    shape("turtle")
    speed(8)

    color("Purple")
    pensize(7)
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

    done()


def main():
    
    tartaruga()

if __name__ == '__main__':
    main()
