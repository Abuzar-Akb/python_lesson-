import random


def monopolyworp():

    dubbel = 0

    while dubbel < 4:
        dobbelsteen = random.randint(1, 6)
        dobbelsteen2 = random.randint(1, 6)

        som = dobbelsteen + dobbelsteen2

        if dubbel == 3:
            status = "gevangenis"
        else:
            status = "dubbel"

        if dobbelsteen == dobbelsteen2:
            print(dobbelsteen, "+", dobbelsteen2, "=", som, status)
            dubbel += 1
        else:
            print(dobbelsteen, "+", dobbelsteen2, "=", som)


monopolyworp()
