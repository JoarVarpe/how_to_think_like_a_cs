import turtle


def draw_multicolor_square(animal, size):
    """Make animal draw a multi-color square of given size."""
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)


# window = turtle.Screen()
# window.bgcolor("lightgreen")

# tess = turtle.Turtle()
# tess.pensize(3)

size = 20
# tess.speed(10)
number = 20


def draw(number, size):
    for _ in range(20):
        draw_multicolor_square(tess, size)
        size += 10
        tess.forward(10)
        tess.right(18)


# draw(number, size)

# window.mainloop()

def final_amount(p, r, n, t):
    """
    Apply the compound interst formula to p
     to produce the final amount
    :param p: principal amount(initial investment)
    :param r: annual nominal interest rate(as decimal)
    :param n: number of times the interest is compounded per year
    :param t: number of years
    :return: a
    """
    a = p * (1 + r / n) ** (n * t)
    return a


# to_invest = float(input("How much do you want to invest?"))
# fnl = final_amount(to_invest, 0.10, 12, 5)
# print("At the end of the period you'll have", fnl)

def all_odd(xs: list) -> bool:
    """Return True if the entire list of integers consists of odd numbers"""
    count = 0
    for value in xs:
        if value % 2 == 1:
            count += 1
    return count == len(xs)


def at_least_three_odd(xs: list) -> bool:
    count = 0
    for value in xs:
        if value % 2 == 1:
            count += 1
        if count >= 3:
            return True
    return False



