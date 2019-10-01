def seizoen(maand):
    if 12 <= maand <= 2:
        print("winter")
    elif 3 <= maand <= 5:
        print("lente")
    elif 6 <= maand <= 8:
        print("zomer")
    else:
        print("herfst")


maandNummer = eval(input("maand nummer "))
seizoen(maandNummer)


def seizoen(maand):
    if maand >= 3 and maand <= 5:
        return 'het is lente'
    elif maand >= 9 and maand <= 11:
        return 'het is herfst'
    elif maand >= 6 and maand <= 8:
        return 'het is zommer'
    else:
        return 'het is winter'


maandnummer = int(input('welke maand is het:'))
print(seizoen(maandnummer))
