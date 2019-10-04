stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s Hertogenbosch", 'Eindhoven',
            'Weert', 'Roermond', 'Sittard', 'Maastricht']


def inlezen_beginstation(stations):
    while True:
        beginstation = input("Wat is je beginstation? ").capitalize()
        if beginstation in stations:
            return beginstation
        else:
            print("Deze trein komt niet in", beginstation)


def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input("Wat is je eindstation? ").capitalize()
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                return eindstation
        else:
            print("Deze trein komt niet in", eindstation)


def omroepen_reis(stations, beginstation, eindstation):
    stationBeginNummer = stations.index(beginstation)
    stationEindNummer = stations.index(eindstation)
    afstand = stationEindNummer - stationBeginNummer
    ritprijs = 5 * afstand
    print('\nHet beginstation {} is het {}e station in het traject.'.format(
        beginstation, stationBeginNummer+1))
    print('Het eindstation {} is het {}e station in het traject.'.format(
        eindstation, stationEindNummer+1))
    print('De afstand bedraagt {} station(s).'.format(afstand))
    print('De prijs van het kaartje is {} euro.'.format(ritprijs))
    print('\nJij stapt in de trein in: {}'.format(beginstation))
    for station in stations[stationBeginNummer + 1:stationEindNummer]:
        print('- {}'.format(station))
    print('Jij stapt uit in: {}'.format(eindstation))


beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
