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
