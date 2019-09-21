
import datetime

afstandKM = eval(input("wat is de afstand: "))

leeftijd = eval(input("wat is je leeftijd: "))


def standaardPrijs(afstandKM):

    if afstandKM < 0:
        print("prijs is dan dus 0 Euro")
    elif afstandKM > 50:
        print(round(afstandKM * 0.60 + 15, 2))
    else:
        print(afstandKM * 0.80)


standPrijs = standaardPrijs(afstandKM)


def ritprijs(leeftijd, weekendrit, afstandKM):

    if leeftijd < 12 and leeftijd >= 65 and weekendrit == True:
        standPrijs * 0.70
    elif leeftijd < 12 and leeftijd >= 65 and weekendrit == False:
        standPrijs * 0.65
    elif weekendrit == True:
        standPrijs * 0.65


weekNummer = datetime.datetime.today().weekday()

if weekNummer < 5:
    weekend = False
else:
    weekend = True

ritprijs(leeftijd, weekend, afstandKM)
