leeftijd = int(input("Geef je leeftijd: "))
paspoort = input("Heb je een nederlandse paspoort JA/NEE: ").lower()

if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Sorry je mag niet stemmen!")
