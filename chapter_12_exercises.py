def readposint():
    the_input = input("Write a positive integer -> ")
    try:
        check = int(the_input)
        if check > 0:
            return "{} is a positive integer".format(check)
        else:
            return "{} is not a positive integer".format(check)

    except ValueError:
        try:
            check = float(the_input)
            return "{} is a float".format(check)
        except ValueError:
            return "Not a number"


print(readposint())
