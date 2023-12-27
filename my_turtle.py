import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()
...

turtlePen.color('green')


def polygon(n, size=120):
    if n > 2:
        angle = 360 / n

        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)


turtlePen.speed(60)

for i in range(0, 100, 5):
    polygon(3, 10 + i)
    turtlePen.left(20)

...
window.mainloop()
