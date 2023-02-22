from turtle import *

def polygon(side,distance):
    for i in range(side):
        forward(distance) #fd()
        left(360/side)    #lt()
bgcolor("black")
color("yellow")
for i in range(3,11):
    polygon(3,i*10)
    bk(5)
    #polygon(i,100)
# polygon(3,100)
# polygon(4,100)
# polygon(5,100)
# polygon(6,100)
# polygon(7,100)
# polygon(8,100)
# polygon(9,100)
# polygon(10,100)


hideturtle()
mainloop()