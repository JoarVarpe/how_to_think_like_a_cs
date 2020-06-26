import turtle
import math

window = turtle.Screen()
window.bgcolor('green')

poly = turtle.Turtle()
poly.shape('turtle')
poly.color('light green')


# 1
def make_square(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def many_small_squares(turtle):
    size = 20
    for _ in range(5):
        make_square(turtle, size)
        turtle.penup()
        turtle.forward(2 * size)
        turtle.pendown()


# 2
def squares_outside_squares(turtle):
    initial_size = 20
    size = initial_size
    for _ in range(5):
        make_square(turtle, size)
        turtle.penup()
        turtle.left(-90)
        turtle.forward(initial_size / 2)
        turtle.left(-90)
        turtle.forward(initial_size / 2)
        turtle.left(180)
        turtle.pendown()
        size += 20


# 3
def draw_poly(turtle, n, size):
    if n == 0:
        return "Can't have {} corners".format(n)
    for _ in range(n):
        turtle.forward(size)
        turtle.left(360 / n)


# 4
def draw_pretty_pattern_squares(turtle, size, n):
    turtle.speed(10)
    for _ in range(n):
        turtle.hideturtle()
        make_square(turtle, size)
        turtle.left(360 / n)


# 5 draw_spiral(poly, 99, 90), draw_spiral(poly, 99, 89)
def draw_spiral(turtle, n, degree):
    turtle.speed(20)
    initial_length = 5
    length = initial_length
    for _ in range(n):
        turtle.right(degree)
        turtle.forward(length)
        length += initial_length


# 6
def draw_equitriangle(turtle, size):
    draw_poly(turtle, 3, size)


# 7
def sum_to(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum


# 8
def area_of_circle(r):
    return 3.14 * r ** 2


# 9
def draw_n_odd_sided_star(turtle, n, size):
    for _ in range(n):
        turtle.forward(size)
        turtle.right(720 / n)


# 10
def draw_n_m_odd_sided_stars(turtle, n, m, size):
    for _ in range(n):
        draw_n_odd_sided_star(turtle, m, size)
        turtle.penup()
        turtle.forward(350)
        turtle.right(720 / n)
        turtle.pendown()


# 1
def turn_clockwise(input: str) -> str or None:
    clockwise_dict = {"N": "E", "E": "S", "S": "W", "W": "N"}
    if input not in clockwise_dict:
        return None
    return clockwise_dict[input]


# 2
def day_name(input: int) -> str or None:
    day_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
                4: "Friday", 5: "Saturday", 6: "Sunday"}
    if input in range(6):
        return day_dict[input]


# 3
def day_num(input: str) -> int or None:
    day_dict_reverse = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
                        "Friday": 4, "Saturday": 5, "Sunday": 6}
    if input not in day_dict_reverse:
        return
    return day_dict_reverse[input]


# 4
def day_add(day: str, days_to_add: int) -> str or None:
    try:
        number = day_num(day) + days_to_add
        print(number)
        return day_name(number % 7)
    except TypeError:
        return


# 5 works for negative since the python % always return a number having the same sign as the denominator
# -5 / 4 = -1.25 --> floor(-1.25) = -2
# -5 / 4 = (-2 x 4 + 3) % 4 = 3

# 6
def days_in_month(month: str) -> int or None:
    days_in_month_dict = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
                          "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
                          "November": 30, "December": 31}
    if month in days_in_month_dict:
        return days_in_month_dict[month]


# 7, # 8
def to_secs(h: float, m: float, s: float) -> int or None:
    try:
        total_seconds = math.floor(h * 3600 + m * 60 + s)
        return total_seconds
    except TypeError:
        return


# 9

def to_secs_inverse(s: int) -> int or None:
    try:
        hours = math.floor(s / 3600)
        minutes = math.floor((s - hours * 3600) / 60)
        seconds = s - hours * 3600 - minutes * 60
        return hours, minutes, seconds
    except TypeError:
        return


# 10
# 3 % 4 == 0 fails, since the whole number remainder when dividing 3 by 4 is 3.
# 3 / 4 == 0 fails, since 3 divided by 4 is 0.75
# 3 // 4 == 0 doesn't fail since this is the floored result of dividing 3 by 4.
# 3 + 4 * 2 == 14 fails since multiplications are done before additions

# 11
def compare(a: float, b: float) -> int:
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


# 12
def hypotenuse(k1: float, k2: float) -> float:
    hyp = (k1 ** 2 + k2 ** 2) ** 0.5
    return hyp


# 13
def slope(x1: int, y1: int, x2: int, y2: int) -> float:
    x_value = x2 - x1
    y_value = y2 - y1
    the_slope = y_value / x_value
    return the_slope


def intercept(x1: int, y1: int, x2: int, y2: int) -> float:
    point = (x1, y1)
    y_value = - slope(x1, y1, x2, y2) * point[0] + point[1]
    return y_value


# 14
def is_even(n: int) -> bool or None:
    try:
        if n % 2 == 0:
            return True
        return False
    except TypeError:
        return


# 15
def is_odd(n: int) -> bool or None:
    try:
        if n % 2 == 1:
            return True
        elif is_even(n):
            return False
    except TypeError:
        return


# 16
def is_factor(factor_of: int, number: int) -> bool:
    try:
        if number % factor_of == 0:
            return True
        return False
    except TypeError:
        return False


# 17
def is_multiple(factor_of: int, target: int) -> bool:
    try:
        if is_factor(target, factor_of):
            return True
        return False
    except TypeError:
        return False


# 18
def fahrenheit_to_celcius(temperature_in_fahrenheit: float) -> float:
    return (temperature_in_fahrenheit - 32) * (5 / 9)


# 19
def celcius_to_fahrenheit(temperature_in_celcius: float) -> float:
    return 9/5 * temperature_in_celcius + 32

# window.mainloop()
