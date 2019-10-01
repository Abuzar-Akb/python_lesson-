lijst = []
while True:

    getal = eval(input("Geef een getal: "))

    if getal == 0:
        print("er zijn ", len(lijst), "getallen ingevoed, de som is", sum(lijst))

        break
    else:
        lijst.append(getal)
