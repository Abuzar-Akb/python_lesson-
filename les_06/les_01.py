def convert(celsius):
    return(celsius * 1.8) + 32


def table():
    for i in range(-30, 41):
        print("{:7}".format(round(convert(i), 2)), "{:7}".format(i))


table()
