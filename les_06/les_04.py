import datetime


def hardlopers():
    while True:
        deelnemer = input("registreer deelnemer ")
        vandaag = datetime.datetime.today()
        datum = vandaag.strftime("%a %d %b %Y")
        tijd = vandaag.strftime("%H:%M:%S")

        deelnamen = (datum + ", " + tijd + ", " + deelnemer + "\n")
        print(deelnamen)
        with open("hardlopers.txt", "a") as f:
            f.write(deelnamen)


hardlopers()
