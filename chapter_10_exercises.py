import turtle, math, sys, os

window = turtle.Screen()
abra = turtle.Turtle()


def koch(tortoise: turtle.Turtle(), order: int, size: int) -> None:
    """
    make the turtle tortoise draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """
    if order == 0:
        tortoise.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(tortoise, order - 1, size / 3)
            tortoise.left(angle)


def koch_snowflake(tortoise: turtle.Turtle(), order: int, size: int) -> None:
    """
    Make a snowflake of Koch fractals of 'order' and 'size'.
    Leave the turtle facing start direction.
    """
    tortoise.hideturtle()
    for angle in [-120, -120, -120]:
        koch(tortoise, order, size)
        tortoise.left(angle)


# TODO revisit cesaro so that the lengths are the same with increasing order....
def cesaro(tortoise: turtle.Turtle(), order: int, size: float, angle_tear: int) -> None:
    """
    Make a cesaro torn line fractal of 'order', 'size' and 'tear angle' given by the user
    """
    experimental_list = [angle_tear / 2 - 90, -180 - angle_tear, - 90 + angle_tear / 2, 0]
    if order == 0:
        tortoise.forward(size)
    else:

        for angle in experimental_list:
            cesaro(tortoise, order - 1, size / 2, angle_tear)
            tortoise.left(angle)
    # else:
    #     for angle in experimental_list:
    #         cesaro(tortoise, order - 1, size / 2, angle_tear)
    #         tortoise.left(angle)


def cesaro_square(tortoise: turtle.Turtle(), order: int, size: int, angle_tear: int) -> None:
    """
    Make a cesaro torn line fractal square of 'order', 'size' and 'tear angle' given by the user
    """
    for angle in [-90, -90, -90, -90]:
        cesaro(tortoise, order, size, angle_tear)
        tortoise.left(angle)


def test_cesaros():
    turtle_size = 10
    abra.speed(20)
    list_of_cords = [window.window_height() / 2 - turtle_size / 2,
                     window.window_height() / 2 - turtle_size / 2 - 75,
                     window.window_height() / 2 - turtle_size / 2 - 150,
                     window.window_height() / 2 - turtle_size / 2 - 225]

    for i in range(len(list_of_cords)):
        abra.penup()
        abra.goto(turtle_size / 2 - window.window_width() / 2, list_of_cords[i])
        abra.pendown()
        cesaro(abra, i, 100, 10)


def make_triangle(tortoise: turtle.Turtle(), size: float) -> None:
    for angle in [120, 120, 120]:
        tortoise.forward(size)
        tortoise.left(angle)


# TODO Try to make the triangles total outer area the same for each
def sierpinski(tortoise: turtle.Turtle(), order: int, size: float) -> None:
    print(order)
    if order == 0:
        make_triangle(tortoise, size)
    else:

        sierpinski(tortoise, order - 1, size / 3)
        abra.penup()
        abra.forward((size * ((2 ** (order - 1)) / (3 ** order))))
        abra.pendown()
        sierpinski(tortoise, order - 1, size / 3)
        abra.penup()
        abra.left(120)
        abra.forward((size * ((2 ** (order - 1)) / (3 ** order))))

        abra.left(-120)
        abra.pendown()
        sierpinski(tortoise, order - 1, size / 3)
        tortoise.penup()
        tortoise.left(-120)
        abra.forward((size * ((2 ** (order - 1)) / (3 ** order))))

        tortoise.left(120)
        tortoise.pendown()


list_of_colors = ["red", "green", "orange"]


def next_color(tortoise: turtle.Turtle()) -> None:
    if tortoise.color()[0] not in list_of_colors:
        tortoise.color(list_of_colors[0])
    else:
        try:
            tortoise.color(list_of_colors[list_of_colors.index(tortoise.color()[0]) + 1])
        except IndexError:
            tortoise.color(list_of_colors[0])
    print(tortoise.color())


# TODO find a more elegant way of solving this one V
def color_sierpinski(tortoise: turtle.Turtle(), order: int, size: float,
                     starting_order: int, color_change_depth=-1) -> None:
    if -1 < color_change_depth:
        if (starting_order - order - 1) == color_change_depth:
            next_color(tortoise)
            print("changing color to {}".format(tortoise.color()[0]))
        if order == 0:
            make_triangle(tortoise, size)
        else:

            color_sierpinski(tortoise, order - 1, size / 3, starting_order, color_change_depth)
            abra.penup()
            abra.forward((size * ((2 ** (order - 1)) / (3 ** order))))
            abra.pendown()
            color_sierpinski(tortoise, order - 1, size / 3, starting_order, color_change_depth)
            abra.penup()
            abra.left(120)
            abra.forward((size * ((2 ** (order - 1)) / (3 ** order))))
            abra.left(-120)
            abra.pendown()
            color_sierpinski(tortoise, order - 1, size / 3, starting_order, color_change_depth)
            tortoise.penup()
            tortoise.left(-120)
            abra.forward((size * ((2 ** (order - 1)) / (3 ** order))))
            tortoise.left(120)
            tortoise.pendown()
    else:
        sierpinski(tortoise, order, size)


def recursive_min(nested_list: list) -> int:
    """
    Find the minimum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are emtpy.
    """
    smallest = None
    first_time = True
    for element in nested_list:
        if type(element) is list:
            value = recursive_min(element)
        else:
            value = element
        if first_time or value < smallest:
            smallest = value
            first_time = False
    return smallest


def count(nested_list: list, target: int) -> int:
    """Returns the total appearances of a target in nested_number_list"""
    total = 0
    for element in nested_list:
        if type(element) is list:
            total += count(element, target)
        elif element == target:
            total += 1
    return total


def flatten(nested_list: list) -> list:
    new_list = []
    for element in nested_list:
        if type(element) is list:
            new_list += flatten(element)
        else:
            new_list.append(element)
    return new_list


def fibonacci_no_recursion(n: int) -> int:
    list_of_start = [0, 1, 1]
    a, b = list_of_start[1], list_of_start[2]
    loops = 2
    if n < 3:
        return list_of_start[n]
    else:
        while loops < n:
            temp = b
            b = a + b
            a = temp
            loops += 1
    return b


# TODO 9, 10, 11 s172 i how to think om jeg gidder.

abra.speed(30)
# sierpinski(abra, 1, 500)
# abra.forward(500 / 3)
# sierpinski(abra, 2, 500)
# abra.forward(500 / 9)
# sierpinski(abra, 3, 500)
# abra.forward(500 * 4 / 27)
# sierpinski(abra, 4, 500)
# abra.forward(500 * 8 / 54)
# sierpinski(abra, 5, 500)
# color_sierpinski(abra, 5, 3000, 5, 0)
# next_color(abra)
# print(recursive_min([[2, 3, 7], [1, 2], -7, [-1, -4, -7]]))
# print(flatten([[2, 3, 7], [1, 2], -7, [-1, -4, -7]]))
# print(count([[2, 3, 7], [1, 2], -7, [-1, -4, -7], -1], -1))
# print(fibonacci_no_recursion(200))
limit = sys.getrecursionlimit()
print(limit)
window.mainloop()
