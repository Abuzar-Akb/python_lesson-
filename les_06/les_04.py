import os
import datetime


def hardlopers():
    # try:
    #     with open("hardlopers.txt", "a+") as myfile:
    #     deelnemer = input("registreer deelnemer ")
    #     myfile.write(deelnemer)
    #     myfile.write("\n")
    # except FileNotFoundError:
    #     f = open("hardlopers.txt", "w+")

    if os.path.exists('hardlopers.txt'):
        deelnemer = input("registreer deelnemer ")
        vandaag = datetime.datetime.today()
        datum = vandaag.strftime("%a %d %b %Y")
        tijd = vandaag.strftime("%H:%M:%S")

        deelnamen = (datum + ", " + tijd + ", " + deelnemer + "\n")

        with open("hardlopers.txt", "a+") as f:
            f.write(''.join(deelnamen))
        f.close()
    else:
        f = open("hardlopers.txt", "w+") c
        f.close()


hardlopers()
