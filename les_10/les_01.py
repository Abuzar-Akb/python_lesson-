
def programma(hotelKosten):
    try:
        aantalPersonen = eval(input('Hoeveel mensen gingen er mee?: '))
        if aantalPersonen < 0:
            raise Exception
        elif aantalPersonen == 0:
            raise ZeroDivisionError

        totaal = hotelKosten / aantalPersonen
        print('de kosten zijn {}'.format(totaal))

    except ZeroDivisionError:
        print('Delen door nul kan niet')
    except ValueError:
        print('Gebruik cijfers voor het invoeren van het aantal')
    except Exception:
        print('Negatieve getallen zijn niet toegestaan')
    except:
        print('Onjuiste invoer')


programma(4356)
