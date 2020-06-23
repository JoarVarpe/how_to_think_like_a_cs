import turtle

# 11 make house from list of instructions

distance = 100
short_distance = ((distance ** 2) / 2) ** 0.5
long_distance = (2 * (distance ** 2)) ** 0.5
list_of_house_cords = [(90, distance), (45, short_distance), (90, short_distance),
                       (135, distance), (-135, long_distance), (135, distance),
                       (135, long_distance), (135, distance)]
window = turtle.Screen()
tess = turtle.Turtle()
tess.color('green')
tess.shape('turtle')
window.bgcolor('light green')


def move_turtle(list, turtle):
    for c in list:
        turtle.left(c[0])
        turtle.forward(c[1])

move_turtle(list_of_house_cords, tess)
window.mainloop()