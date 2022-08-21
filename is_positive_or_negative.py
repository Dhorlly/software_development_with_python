def inspect(x):
    """
    Function that determines if a number is postive or negative
    >>> inspect(5)
    5 is a positive number
    """
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is a positve number")
    elif x < 0:
        print(x, "is a negative number")
    else:
        print(x, "is unlike anything I've ever seen")

inspect(0)
inspect(5)
inspect(-10)
