import turtle

list_of_turtle_shapes = ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']

background = input('please enter a color from the site http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm\n')
tess_color = input('what color is tess?\n')
window = turtle.Screen()
alex = turtle.Turtle()
window.bgcolor(background)
window.title('Hello, Tess!')
tess = turtle.Turtle()
tess.color(tess_color)
tess.pensize(3)

tess.forward(30)
tess.left(120)
tess.forward(90)
for _ in range(4):
    alex.forward(50)
    alex.left(90)


window.mainloop()
