import random


def toon_aantal_kluizen_vrij():
    bestand = open('kluizen.txt', 'r')
    lijst = bestand.readlines()
    beschikbareKluizen = 12 - len(lijst)
    bestand.close()
    print('Er zijn in totaal nog', beschikbareKluizen, 'kluizen vrij!')


def nieuwe_kluis():
    kluisNummers = ['1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '10', '11', '12']
    bestand = open('kluizen.txt', 'r')
    kluizenLijst = bestand.readlines()

    for kluis in kluizenLijst:
        kluizenLijstSplit = kluis.split(";")
        for kluisNummer in kluizenLijstSplit:
            if kluisNummer in kluisNummers:
                kluisNummers.remove(kluisNummer)

    if len(kluisNummers) > 0:
        while True:
            kluisNummer = random.choice(kluisNummers)
            kluisCode = input('Geef een kluiscode op: ')

            if len(kluisCode) > 3:
                appendKluis = open('kluizen.txt', 'a')
                appendKluis.write('\n{};{}'.format(kluisNummer, kluisCode))
                appendKluis.close()
                print('U heeft kluis {} gekregen, uw code van de kluis is: {} bewaar deze goed!'.format(
                    kluisNummer, kluisCode))
                break
            else:
                print('Uw code is korter dan 4 tekens, probeer het nog eens.')
    else:
        print('Er zijn geen kluizen meer beschikbaar, helaas!')
    bestand.close()


def kluis_openen():
    bestand = open('kluizen.txt', 'r')
    kluizenLijst = bestand.readlines()
    kluisNummer = input('Voer uw kluisnummer in: ')
    kluisCode = input('Voer uw kluiscode in: ')
    kluisCombinatie = kluisNummer + ';' + kluisCode

    for kluis in kluizenLijst:
        kluis = kluis.strip()
        if kluisCombinatie == kluis:
            combinatieCorrect = True
            break
        else:
            combinatieCorrect = False

    if combinatieCorrect == True:
        print('Combinatie is correct, kluis is geopend!')
    else:
        print('Helaas, de combinatie is incorrect. De kluis is niet geopend.')
    bestand.close()


def main():
    while True:
        print('Welkom bij het Bagagekluizen Programma!')
        print('1. Toon het aantal beschikbare kluizen.')
        print('2. Claim een kluis.')
        print('3. Open een kluis.')
        print('4. Sluit.')

        keuze = int(input('Geef een keuze op: '))

        if keuze == 1:
            toon_aantal_kluizen_vrij()
        elif keuze == 2:
            nieuwe_kluis()
        elif keuze == 3:
            kluis_openen()
        elif keuze == 4:
            break
        else:
            print('Ongeldige keuze.')


main()
