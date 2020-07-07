import turtle
import os
import time


# import pygame, math


def koch(tortoise, order, size):
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


# window = turtle.Screen()
# abby = turtle.Turtle()
# koch(abby, 6, 1000)
# window.mainloop()

def recursive_sum(nested_number_list):
    """Returns the total sum of all elements in nested_number_list"""
    total = 0
    for element in nested_number_list:
        if type(element) is list:
            total += recursive_sum(element)
        else:
            total += element
    return total


def recursive_sum2(nested_number_list):
    """Returns the total sum of all elemtens in nesten_number_list"""
    if len(nested_number_list) == 0:
        return 0
    head, *tail = nested_number_list  # assign the first elemten of nesten_number_list
    # to head, and the rest to the tail
    if isinstance(head, list):  # if head is a list
        return recursive_sum2(head) + recursive_sum2(tail)
    else:
        return head + recursive_sum2(tail)


def recursive_max(nested_list):
    """
    Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are emtpy.
    """
    largest = None
    first_time = True
    for element in nested_list:
        if type(element) is list:
            value = recursive_max(element)
        else:
            value = element
        if first_time or value > largest:
            largest = value
            first_time = False
    return largest


def recursion_depth(number):
    print("{}, ".format(number), end="")
    recursion_depth(number + 1)


def fib(n):
    if n <= 1:
        return n
    t = fib(n - 1) + fib(n - 2)
    return t


# t0 = time.process_time()
# n = 35
# result = fib(n)
# t1 = time.process_time()
#
# print("fib ({}) = {}, ({:.2f} secs)".format(n, result, t1 - t0))

def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returms just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix=""):
    """Print recursive listing of contents of path"""
    if prefix == "":
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for file in dirlist:
        print(prefix + file)  # print the line
        fullname = os.path.join(path, file)  # turn name into full pathname
        if os.path.isdir(fullname):  # if a directory, recurse.
            print_files(fullname, prefix + "| ")


# pygame.init()
# surface_size = 1024
# main_surface = pygame.display.set_mode((surface_size, surface_size))
# my_clock = pygame.time.Clock()


def draw_tree(order, theta, size, position, heading, color=(0, 0, 0), depth=0):
    trunk_ratio = 0.29
    trunk = size * trunk_ratio
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u, v) = position
    newposition = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, position, newposition)

    if order > 0:  # Draw another layer of subtrees

        if depth == 0:
            color1 = (255, 0, 0)
            color1 = (0, 0, 255)
        else:
            color1 = color
            color2 = color

        newsize = size * (1 - trunk_ratio)
        draw_tree(order - 1, theta, newsize, newposition, heading - theta, color1, depth + 1)
        draw_tree(order - 1, theta, newsize, newposition, heading + theta, color2, depth + 1)


def gameloop():
    theta = 0
    while True:

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        theta += 0.01

        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size * 0.9, (surface_size // 2, surface_size - 50),
                  math.pi / 2)

        pygame.display.flip()
        my_clock.tick(120)


#
# gameloop()
# pygame.quit()

def function_a(n):  # do things associated with state A
    if n == 0:
        return
    print('a')
    function_b(n - 1)  # proceed to state B


def function_b(n):  # Do things associated with state B
    print('b')
    function_a(n - 1)  # Proceed to state B
