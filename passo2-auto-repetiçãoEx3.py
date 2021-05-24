from turtle import *


def main():
    
    speed(11)
    shape("turtle")

    for cont in range(30):
        forward(5)
        penup()
        forward(5)
        pendown()

    done()

if __name__ == '__main__':
    main()
