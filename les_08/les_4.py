def ticker(filename):

    bedrijven = {}

    with open(filename) as bestand:
        for lijn in bestand:
            [key, val] = lijn.split(":")
            bedrijven[key] = val

    bedrijf = input("Enter Company name: ").upper()

    for key, val in bedrijven.items():
        if key == bedrijf:
            print("Ticker symbol:", val)

    tick = input("Enter Ticker symbol: ").upper()

    for key, val in bedrijven.items():
        if val.strip() == tick:
            print("Company name:", key)


ticker('ticker.txt')
