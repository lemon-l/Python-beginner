# Demo 1

from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()



# Demo 2

from turtle import *

# hideturtle()
penup()
speed(10)
goto(-350, 350)
pendown()

for j in range(5):
    left(60)
    for i in range(9):
        forward(50)
        right(60)
    left(120)
    forward(50)

for k in range(4):
    for j in range(3):
        right(60)
        forward(50)

    for j in range(5):
        left(60)
        begin_fill()
        fillcolor('black')
        for i in range(9):
            forward(50)
            right(60)
        left(120)
        forward(50)
        end_fill()

    for j in range(3):
        left(60)
        forward(50)

    for j in range(5):
        right(60)
        for i in range(9):
            forward(50)
            left(60)
        right(120)
        forward(50)

done()