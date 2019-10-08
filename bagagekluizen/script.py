
op = eval(input("kies een optie\n1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Ik geef mijn kluis terug \n"))

kluizen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "12"]


def main(op):

    def beschikbare_kluizen():
        with open('kluizen.txt') as bestand:
            lijnen = bestand.readlines()
            bestand.close()
            return lijnen

    def toon_aantal_kluizen_vrij():
        lijnen = beschikbare_kluizen()
        beschikbareKluizen = 12 - len(lijnen)
        if beschikbareKluizen == 0:
            print("\nSorry alle kluizen zijn vol\n")
        else:
            print("\nEr zijn", beschikbareKluizen, "kluizen vrij\n")

    def nieuwe_kluis():
        lijnen = beschikbare_kluizen()
        for i in lijnen:
            kluis = i.split(";")
            if kluis[0] in kluizen:
                kluizen.remove(kluis[0])
                print("is er in", kluizen)
            else:
                print("niet er in", kluizen)

    if op == 1:
        toon_aantal_kluizen_vrij()
    elif op == 2:
        nieuwe_kluis()
    elif op == 3:
        print("optie 3")
    elif op == 4:
        print("optie 4")
    else:
        print("dit is geen optie")


main(op)
