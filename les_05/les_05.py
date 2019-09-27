# mylist = [4, 5, 3, -81]


def kwadraten_som(grondGetal):
    #     kwadraten = []
    #     for i in grondGetal:
    #         if i > 0:
    #             kwadraten.append(i**2)
    #     return sum((kwadraten))

    #     endsum
    antwoord = 0
    for getal in grondGetal:
        if getal > 0:
            antwoord += getal ** 2

    return (antwoord)


# print(kwadraten_som(mylist))
