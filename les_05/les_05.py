mylist = [4, 5, 3, -81]


def kwadraten_som(grondGetal):
    # kwadraten = []
    # for i in grondGetal:
    #     if i > 0:
    #         kwadraten.append(i**2)
    # return sum((kwadraten))
    antwoord = 0
    for nummer in grondGetal:
        if nummer > 0:
            antwoord += nummer**2
    return antwoord


print(kwadraten_som(mylist))
