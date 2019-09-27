def gemiddelde():
    zin = input("type in zin in ")

    gemiddelde = (len(zin) - zin.count(' ')) / 2

    print(gemiddelde)


gemiddelde()
